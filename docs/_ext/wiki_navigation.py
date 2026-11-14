"""Group the automatic sidebar by page type and explicit stub metadata."""

from pathlib import PurePosixPath
from urllib.parse import urljoin, urlsplit


def add_navigation_groups(app, pagename, templatename, context, doctree):
    """Keep Sphinx's rendered titles and links, including math and active states."""
    documents = {
        app.builder.get_target_uri(name): name
        for name in app.env.found_docs
        if PurePosixPath(name).parent.as_posix() in {"articles", "theorems"}
    }
    page_uri = app.builder.get_target_uri(pagename)

    def group_navigation(navigation):
        groups = {"Articles": [], "Theorems": [], "Stubs": []}
        for item in navigation.select("li.toctree-l1"):
            link = item.find("a", href=True)
            if link is None:
                continue
            target = urlsplit(urljoin(page_uri, link["href"])).path
            name = documents.get(target)
            if name is None:
                continue
            stub = app.env.metadata.get(name, {}).get("stub", False)
            if str(stub).strip().lower() == "true":
                group = "Stubs"
            else:
                group = "Articles" if name.startswith("articles/") else "Theorems"
            groups[group].append((name, item))

        return [
            {
                "title": title,
                "current": any("current" in item.get("class", []) for _, item in entries),
                "entries": [
                    str(item) for name, item in sorted(
                        entries, key=lambda entry: (PurePosixPath(entry[0]).name, entry[0])
                    )
                ],
            }
            for title, entries in groups.items()
        ]

    context["group_wiki_navigation"] = group_navigation


def setup(app):
    app.connect("html-page-context", add_navigation_groups)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
