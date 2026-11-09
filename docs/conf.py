"""Configuration for the GitHub-hosted mathematical wiki."""

import os

project = "Coarse Geometry and Topological Phases"
author = "Matthias Ludewig and contributors"
copyright = "2026, Matthias Ludewig and contributors"
language = "en"
root_doc = "index"
source_suffix = {".md": "markdown"}

extensions = [
    "myst_parser",
    "sphinx_proof",
    "sphinx_togglebutton",
    "sphinx_design",
    "sphinxcontrib.tikz",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
]
myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence"]
myst_heading_anchors = 3
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
nitpicky = True
numfig_secnum_depth = 0
html_theme = "pydata_sphinx_theme"
html_title = project
html_static_path = ["_static"]
html_css_files = ["custom.css"]
templates_path = ["_templates"]
html_show_sourcelink = False
html_sidebars = {"**": ["global-navigation.html"]}
html_theme_options = {
    "logo": {"text": "Coarse geometry & topological phases"},
    "show_nav_level": 2,
    "navigation_depth": 2,
    "show_toc_level": 2,
    "use_edit_page_button": True,
    "navbar_center": [],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/MatthiasLudewig/coarse-phases",
            "icon": "fa-brands fa-github",
        }
    ],
    "announcement": "Working draft — mathematical review in progress.",
}
html_context = {
    "github_user": "MatthiasLudewig",
    "github_repo": "coarse-phases",
    # A PR preview edits that PR's branch. Published pages edit main.
    "github_version": os.environ.get("WIKI_EDIT_BRANCH", "main"),
    "doc_path": "docs",
    "default_mode": "light",
}
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"
# Compile diagram directives on the CI runner; readers receive ordinary SVGs.
latex_engine = "pdflatex"
tikz_proc_suite = "pdf2svg"
tikz_latex_preamble = r"\usepackage{amsmath,amssymb}"
togglebutton_hint = "Show details"
togglebutton_hint_hide = "Hide details"


def unique_statement_anchors(app, pagename, templatename, context, doctree):
    """Keep the statement anchor, without duplicating it on its heading."""
    from html import escape
    from sphinx_proof.nodes import unenumerable_node

    if doctree is None:
        return
    # sphinx-proof 0.4.0 needs the duplicate title ID during HTML translation.
    # Remove it only after translation, leaving the outer statement ID intact.
    for statement in doctree.findall(unenumerable_node):
        for label in statement.get("ids", []):
            context["body"] = context["body"].replace(
                f'<p class="admonition-title" id="{escape(label, quote=True)}">',
                '<p class="admonition-title">',
                1,
            )


def setup(app):
    app.connect("html-page-context", unique_statement_anchors)
