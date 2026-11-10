# Setup and editorial decisions

## Current architecture — 6 November 2026

There are two mathematical page types:

1. **Regular articles** in `docs/articles/`: definitions are written directly in
   their owning articles, together with motivation, examples, and discussion.
   Other pages link to labels in those articles and load the whole target page.
2. **Standalone theorem pages** in `docs/theorems/`: full formal statements,
   with or without proofs. These pages may develop long arguments with
   intermediate lemmas. Articles can explain results informally and link to
   the theorem pages. Short theorems and proofs can also remain in articles.

This decision replaces the original separation of canonical definition pages
and expository articles, and the reuse of definitions through include fragments.
There is no transclusion of mathematical statements between pages.

The five sample mathematical articles, shared definition fragment, and sample
bibliography records have been removed. The author's requested replacement
collection is now drafted: 15 articles, three stubs, and three theorem pages
with proofs.
Unreviewed agent-authored pages retain the warning `Agent-generated, not reviewed yet`.
Coverage and mathematical qualifications are in `docs/about/draft-review.md`.

## Saving work — 10 November 2026

The author works in this workspace and requested that completed edits be committed and pushed directly to `main`.
Routine changes no longer require a pull request or a separate merge approval.
GitHub Actions checks each push, and the fixed HTML preview is refreshed from a successful run.
Mathematical review remains separate from saving drafts, and publication remains disabled until requested.

## Infrastructure retained

- Private repository: `MatthiasLudewig/coarse-phases`.
- Sphinx/MyST, pinned dependencies, PyData theme, MathJax, and custom styling.
- TikZ and `tikzcd` diagrams through `sphinxcontrib.tikz`. Standalone `{tikz}`
  directives compile to SVG on GitHub Actions using TeX and `pdf2svg`; no local
  TeX installation is required for authoring or viewing the HTML preview.
  The authoring guide documents the `cd` library and plain-text alternatives.
- Full sidebar navigation, GitHub edit links, search, and light/dark modes.
- Standalone articles and theorem pages use ordinary MyST headings and
  `sphinx-proof` labels. No new page-rendering extension is needed.
- Optional native `sphinx-design` dropdowns for proofs and `sphinx-togglebutton`
  for titled technical remarks.
- Strict builds and browser checks on GitHub Actions. Reader checks exercise
  the actual articles on desktop and mobile, including their mathematics and
  review warnings. Additional interaction checks use temporary test fixtures
  that never enter the website preview or its search/navigation.
- Downloadable HTML and screenshot artifacts. Pages deployment stays disabled.

## Deliberately pending

- Mathematical review of the requested article collection and its proof pages.
- Public visibility, enabling Pages, and verification of the live site.
- Branch protection, unavailable for this private repository on GitHub Free.
- A reuse licence, invited contributors, and any custom domain.
- Bibliography automation, backlinks, dependency graphs, automatic object
  indexes, and a global proof switch.

Statement directives use `:nonumber:`: definitions, propositions, theorems, and
related statements have descriptive headings without visible numbers. Stable
labels still support links between articles.

Definitions, self-contained arguments, and well-known textbook material do not
carry literature citations. Nontrivial results used without proof link directly
to public papers, including arXiv preprints. Private notes are not cited.
