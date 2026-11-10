"""Make pdf2svg diagrams follow the surrounding font size and theme colors."""

from copy import deepcopy
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET


SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)

# TeX points are 1/72.27 inch; pdf2svg coordinates are PDF points, 1/72 inch.
BASE_FONT_PDF_POINTS = 12 * 72 / 72.27
NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
SEGMENT = re.compile(
    rf"\s*M\s*({NUMBER})[\s,]+({NUMBER})\s*L\s*"
    rf"({NUMBER})[\s,]+({NUMBER})\s*"
)
URL_REFERENCE = re.compile(r"url\(\s*(['\"]?)#([^\s)'\"]+)\1\s*\)")
IMAGE_TAG = re.compile(r"<img\b(?:[^>\"']|\"[^\"]*\"|'[^']*')*>", re.I)
IMAGE_PATH = re.compile(r"(?:^|/)_images/(tikz-[0-9a-f]+\.svg)$")


def _solid_color(value, white=False):
    """Recognize opaque black/white without changing alpha or other colors."""
    value = re.sub(r"\s+", "", value).lower()
    if white:
        return value in {"white", "#fff", "#ffffff", "#ffff", "#ffffffff",
                         "rgb(255,255,255)", "rgb(100%,100%,100%)",
                         "rgba(255,255,255,1)", "rgba(100%,100%,100%,1)"}
    return value in {"black", "#000", "#000000", "#000f", "#000000ff",
                     "rgb(0,0,0)", "rgb(0%,0%,0%)",
                     "rgba(0,0,0,1)", "rgba(0%,0%,0%,1)"}


def _style_items(element):
    return [part.partition(":") for part in element.get("style", "").split(";")
            if part.strip()]


def _property(element, name, default=""):
    value = element.get(name, default)
    for key, separator, content in _style_items(element):
        if separator and key.strip().lower() == name:
            value = content.strip()
    return value


def _set_property(element, name, value):
    items = _style_items(element)
    if any(key.strip().lower() == name for key, _, _ in items):
        element.set("style", ";".join(
            f"{key}:{value if key.strip().lower() == name else content}"
            for key, _, content in items
        ))
    else:
        element.set(name, value)


def _equality_masks(root):
    """Turn TikZ's white overpaint in straight double lines into clear gaps.

    Limit this to adjacent black/white paths with identical geometry and a
    narrower white stroke. Other authored white paint remains unchanged.
    """
    existing_ids = {node.get("id") for node in root.iter() if node.get("id")}
    defs = root.find(f"{{{SVG}}}defs")
    for parent in list(root.iter()):
        previous = None
        for inner in list(parent):
            outer = previous
            previous = inner
            if (outer is None or outer.tag != f"{{{SVG}}}path"
                    or inner.tag != outer.tag
                    or _property(outer, "fill") != "none"
                    or _property(inner, "fill") != "none"
                    or not _solid_color(_property(outer, "stroke"))
                    or not _solid_color(_property(inner, "stroke"), white=True)
                    or outer.get("d") != inner.get("d")
                    or outer.get("transform") != inner.get("transform")
                    or outer.get("mask") or inner.get("mask")):
                continue
            try:
                outer_width = float(_property(outer, "stroke-width"))
                inner_width = float(_property(inner, "stroke-width"))
            except ValueError:
                continue
            segment = SEGMENT.fullmatch(inner.get("d", ""))
            if not segment or not 0 < inner_width < outer_width:
                continue
            # Preserve all stroke geometry and opaque overpaint semantics.
            attributes = ("stroke-linecap", "stroke-linejoin", "stroke-dasharray",
                          "stroke-dashoffset", "stroke-miterlimit", "clip-path")
            if any(_property(outer, name) != _property(inner, name) for name in attributes):
                continue
            if any(_property(path, name, "1") != "1"
                   for path in (outer, inner) for name in ("opacity", "stroke-opacity")):
                continue

            x1, y1, x2, y2 = map(float, segment.groups())
            bounds = {
                "x": str(min(x1, x2) - outer_width),
                "y": str(min(y1, y2) - outer_width),
                "width": str(abs(x2 - x1) + 2 * outer_width),
                "height": str(abs(y2 - y1) + 2 * outer_width),
            }
            mask_id = "wiki-equality-mask"
            number = 0
            while mask_id in existing_ids:
                number += 1
                mask_id = f"wiki-equality-mask-{number}"
            existing_ids.add(mask_id)
            mask = ET.Element(f"{{{SVG}}}mask", {
                "id": mask_id, "maskUnits": "userSpaceOnUse",
                "maskContentUnits": "userSpaceOnUse", "mask-type": "luminance",
                **bounds,
            })
            ET.SubElement(mask, f"{{{SVG}}}rect", {**bounds, "fill": "white"})
            cutout = deepcopy(inner)
            # The mask is in the outer path's local coordinates. Its transform
            # is applied once by that path, not again inside the mask.
            cutout.attrib.pop("transform", None)
            cutout.attrib.pop("id", None)
            _set_property(cutout, "stroke", "black")
            mask.append(cutout)
            if defs is None:
                defs = ET.Element(f"{{{SVG}}}defs")
                root.insert(0, defs)
            defs.append(mask)
            outer.set("mask", f"url(#{mask_id})")
            parent.remove(inner)
            previous = None


def _theme_paint(element):
    # Black/white inside masks controls opacity and must not follow the theme.
    if element.tag == f"{{{SVG}}}mask":
        return
    for name in ("fill", "stroke"):
        if name in element.attrib and _solid_color(element.get(name)):
            element.set(name, "currentColor")
    if "style" in element.attrib:
        element.set("style", ";".join(
            f"{key}:{'currentColor' if key.strip().lower() in ('fill', 'stroke') and _solid_color(value) else value}"
            for key, _, value in _style_items(element)
        ))
    for child in element:
        _theme_paint(child)


def _prefix_ids(root, prefix):
    mapping = {node.get("id"): f"{prefix}-{node.get('id')}"
               for node in root.iter() if node.get("id")}

    def references(value):
        return URL_REFERENCE.sub(
            lambda match: f"url(#{mapping.get(match.group(2), match.group(2))})", value
        )

    for node in root.iter():
        for name, value in list(node.attrib.items()):
            if name == "id":
                value = mapping[value]
            elif name in ("href", f"{{{XLINK}}}href") and value.startswith("#"):
                value = "#" + mapping.get(value[1:], value[1:])
            elif name in ("aria-labelledby", "aria-describedby"):
                value = " ".join(mapping.get(part, part) for part in value.split())
            node.set(name, references(value))
        if node.tag == f"{{{SVG}}}style" and node.text:
            node.text = references(node.text)
    return set(mapping.values())


def prepare_svg(text, prefix, alt, scale=""):
    """Prepare one occurrence of a pdf2svg image without requiring Sphinx."""
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.-]*", prefix):
        raise ValueError("Invalid TikZ SVG identifier prefix")
    root = ET.fromstring(text)
    if root.tag != f"{{{SVG}}}svg":
        raise ValueError("TikZ output is not an SVG document")
    viewbox = [float(value) for value in re.split(r"[\s,]+", root.get("viewBox", "").strip())]
    if len(viewbox) != 4 or not (viewbox[2] > 0 and viewbox[3] > 0):
        raise ValueError("TikZ SVG has no positive viewBox dimensions")
    if scale and (not re.fullmatch(rf"{NUMBER}%", scale) or float(scale[:-1]) <= 0):
        raise ValueError("TikZ SVG scale must be a positive percentage")
    root.set("width", scale or f"{viewbox[2] / BASE_FONT_PDF_POINTS:.8g}em")
    root.set("height", f"{viewbox[3] / BASE_FONT_PDF_POINTS:.8g}em")
    _equality_masks(root)
    _theme_paint(root)
    root.attrib.setdefault("fill", "currentColor")
    ids = _prefix_ids(root, prefix)
    root.set("class", " ".join(filter(None, [root.get("class"), "wiki-tikz-svg"])))
    root.set("role", "img")
    root.set("aria-label", alt)
    root.set("focusable", "false")
    title_id = f"{prefix}-title"
    while title_id in ids:
        title_id += "-title"
    title = ET.Element(f"{{{SVG}}}title", {"id": title_id})
    title.text = alt
    root.insert(0, title)
    return ET.tostring(root, encoding="unicode")


class _ImageAttributes(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.attrs = dict(attrs)


def inline_tikz(app, pagename, templatename, context, doctree):
    """Keep upstream figure markup and replace only its generated SVG image."""
    occurrence = 0
    page_id = sha256(pagename.encode()).hexdigest()[:16]

    def replace(match):
        nonlocal occurrence
        parser = _ImageAttributes(convert_charrefs=True)
        parser.feed(match.group())
        attributes = parser.attrs
        source = IMAGE_PATH.search(urlsplit(attributes.get("src", "")).path)
        if source is None:
            return match.group()
        occurrence += 1
        image = Path(app.builder.outdir) / "_images" / source.group(1)
        try:
            return prepare_svg(
                image.read_text(encoding="utf-8"), f"wiki-tikz-{page_id}-{occurrence}",
                attributes.get("alt", "Figure made with TikZ"), attributes.get("width", ""),
            )
        except (OSError, ValueError, ET.ParseError) as error:
            from sphinx.errors import SphinxError
            raise SphinxError(f"Cannot prepare TikZ SVG {image.name} on {pagename}: {error}") from error

    context["body"] = IMAGE_TAG.sub(replace, context.get("body", ""))


def setup(app):
    app.connect("html-page-context", inline_tikz)
    return {"version": "1", "parallel_read_safe": True, "parallel_write_safe": True}
