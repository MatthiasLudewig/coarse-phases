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

The five sample mathematical articles, shared definition fragment, and sample bibliography records have been removed.
The current collection contains 38 article pages, including 22 marked as stubs, and two theorem pages with proofs.
Unreviewed agent-authored pages retain the warning `Agent-generated, not reviewed yet`.

## Saving work — 10 November 2026

The author works in this workspace and requested that completed edits be committed and pushed directly to `main`.
Routine changes no longer require a pull request or a separate merge approval.
GitHub Actions checks each push, and the fixed HTML preview is refreshed from a successful run.
Mathematical review remains separate from saving drafts.

## Publication — 13 November 2026

The author requested publication of the wiki on GitHub Pages.
The repository is public, Pages uses GitHub Actions, and the repository variable `ENABLE_PAGES` is `true`.
Successful builds of `main` publish at <https://matthiasludewig.github.io/coarse-phases/>.
Both **Wiki checks** and **Publish approved main branch** must succeed for an update to go live.
Existing mathematical review warnings remain in place; publication does not constitute mathematical review.
The direct-push workflow remains in use, and drafts that should stay outside the live site can use a branch and pull request.

## Infrastructure retained

- Public repository: `MatthiasLudewig/coarse-phases`.
- Sphinx/MyST, pinned dependencies, PyData theme, MathJax, and custom styling.
- TikZ and `tikzcd` diagrams through `sphinxcontrib.tikz`. Standalone `{tikz}`
  directives compile to SVG on GitHub Actions using TeX and `pdf2svg`; no local
  TeX installation is required for authoring or viewing the HTML preview.
  The authoring guide documents the `cd` library and plain-text alternatives.
- Automatic sidebar navigation under **Articles**, **Theorems**, and **Stubs**, as requested on 14 November 2026.
  Pages marked `stub: true` in YAML front matter appear only in the final group; pages without the field remain in their regular group.
  Each list is sorted by filename, and all page URLs and search entries are retained.
- GitHub edit links, search, and light/dark modes.
- Standalone articles and theorem pages use ordinary MyST headings and
  `sphinx-proof` labels. No new page-rendering extension is needed.
- Optional native `sphinx-design` dropdowns for proofs and `sphinx-togglebutton`
  for titled technical remarks.
- Strict builds and browser checks on GitHub Actions. Reader checks exercise
  the actual articles on desktop and mobile, including their mathematics and
  review warnings. Additional interaction checks use temporary test fixtures
  that never enter the website preview or its search/navigation.
- Downloadable HTML and screenshot artifacts, plus GitHub Pages deployment after successful checks on `main`.

## Deliberately pending

- Mathematical review of the requested article collection and its proof pages.
- Branch protection and collaboration requirements for future contributors.
- A reuse licence, invited contributors, and any custom domain.
- Bibliography automation, backlinks, dependency graphs, automatic object
  indexes, and a global proof switch.

Statement directives use `:nonumber:`: definitions, propositions, theorems, and
related statements have descriptive headings without visible numbers. Stable
labels still support links between articles.

Definitions, self-contained arguments, and well-known textbook material do not
carry literature citations. Nontrivial results used without proof link directly
to public papers, including arXiv preprints. Private notes are not cited.
