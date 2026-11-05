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
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
]
myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence"]
myst_heading_anchors = 3
exclude_patterns = ["_build", "_snippets/**", "Thumbs.db", ".DS_Store"]
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
togglebutton_hint = "Show details"
togglebutton_hint_hide = "Hide details"
