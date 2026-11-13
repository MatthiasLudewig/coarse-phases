# Project brief: A mathematical wiki for coarse geometry and topological phases

**Status:** Infrastructure and first requested article collection drafted; mathematical review pending
**Last updated:** 10 November 2026
**Purpose of this document:** Record the intended features, the agreed technical direction, the implementation plan, and decisions that remain open. This specifies the intended system. See `SETUP.md` for implementation status. The editorial decision of 6 November 2026 replaces the original definition-fragment architecture.

## 1. Project vision

Create a public, wiki-style mathematical knowledge base developing and disseminating a **coarse-geometric framework for topological phases**.

The intended site should be similar in spirit to **nLab**, but focused on this research area. It should function both as:

- a **reference** containing precise mathematical definitions, propositions, theorems, proofs, examples, and literature references; and
- an **expository resource** providing motivation, explanations, conceptual relationships, and connections to topological phases.

Initially, one principal author will create and maintain the content, possibly with a handful of invited colleagues. The contribution model should be able to expand later. AI assistance, especially **Codex**, is expected to help draft, organize, cross-link, and maintain pages, subject to mathematical review before publication.

Key design goals:

1. Markdown and LaTeX-based authoring, with files remaining portable and editable outside the website.
2. Strong, stable cross-references between mathematical objects, not only between pages.
3. Two mathematical page types: regular articles and standalone theorem pages, with or without proofs.
4. Definitions written directly in their owning articles, with stable links from other pages; informal accounts of results can link to full formal statements on theorem pages.
5. Collapsible proofs; readable mathematical typesetting; configurable appearance and navigation.
6. Git version history, controlled contributions, automated checks, and low-maintenance hosting.
7. A structure that can later support backlinks, indexes of mathematical objects, and a graph of conceptual dependencies.

## 2. Selected technical direction

The current decision is to use **Sphinx + MyST Markdown + GitHub**, rather than MediaWiki or a permanently running file-backed wiki server.

| Role | Proposed component | Status |
|---|---|---|
| Source of truth | Ordinary Markdown (`.md`) files in Git | Chosen |
| Repository and collaboration | GitHub | Chosen |
| Static website generator | Sphinx | Chosen |
| Markdown dialect | MyST Parser (LaTeX and Sphinx directives) | Chosen |
| Mathematical theorem environments | `sphinx-proof` | Proposed as part of initial setup |
| Collapsible proofs | `sphinx-togglebutton` (optionally `sphinx-design`) | Proposed |
| Commutative diagrams and TikZ graphics | `sphinxcontrib.tikz`, TeX, and `pdf2svg` | SVG rendering during the GitHub Actions build |
| HTML theme | PyData Sphinx Theme | Preferred starting point; not final |
| Automatic build and validation | GitHub Actions | Chosen |
| Public website hosting | GitHub Pages | Preferred initial hosting |
| Custom URL | Subdomain of existing personal website | Possible later; undecided |
| AI-supported editing | Codex commits and pushes the author's workspace edits directly to `main` | Author's decision of 10 November 2026 |
| MySQL/PHP | Not required for this Sphinx website | Not needed |

**Important distinction:** Sphinx is a *static-site generator*, not a live wiki server. The public site displays pre-generated HTML. Browser-based editing normally follows an **Edit this page → GitHub** link, rather than happening inside the published website itself.

### Architecture

```text
Author, colleague, or Codex
            |
            v
GitHub repository (Markdown source, images, config, workflow)
            |
            | push to main: build and validate; publish only when enabled
            v
GitHub Actions (temporary build machine)
            |
            v
Sphinx + MyST + extensions
  - parse Markdown and LaTeX
  - resolve and check cross-references
  - render definitions, theorems, proofs
  - compile TikZ and tikzcd diagrams to SVG
  - produce HTML, CSS, JavaScript, search index
            |
            v
GitHub Pages (static hosting)
            |
            v
Public reader's web browser
```

Sphinx runs **when triggered by GitHub Actions**, not whenever a visitor opens a page. Visitors receive the generated HTML. MathJax may render mathematics on the visitor's device. TikZ and `tikzcd` diagrams are compiled to SVG during the build and displayed as images. Sphinx supports incremental local builds, though hosted CI jobs may perform clean builds; performance is not expected to be an obstacle for an initial, modest-sized wiki.

### URLs

For a GitHub account `USERNAME` and repository `coarse-phases`, the usual GitHub Pages project URL would be:

`https://USERNAME.github.io/coarse-phases/`

Later the website could use a subdomain such as `https://wiki.example.org/` by configuring the GitHub Pages custom domain and the corresponding DNS record. The existing personal website and its MySQL database can remain unchanged.

## 3. Content architecture

Use two kinds of mathematical pages, both readable and navigable as standalone
pages:

- **Regular articles:** motivation, definitions, examples, and discussion of a
  topic. Each definition is written directly in its owning article. For example,
  a future *Bornological coarse space* article can define coarse structure,
  bornological space, and bornological coarse space with individual labels.
- **Theorem pages:** full formal statements, with or without proofs. A theorem
  page can develop a long proof through intermediate lemmas and sections, and
  links to prerequisite definitions and the motivating articles.

An article can explain a result informally and link to its theorem page for the
full statement and any proof. Theorems and short proofs are also allowed directly
in articles; a separate page is an option for keeping longer arguments out of the
main exposition, not a requirement for every result.

A reference to a definition or theorem loads the complete owning page and moves
to its labelled target. Do not transclude definitions or theorem pages into other
articles. The previous separate definition-reference layer and shared-fragment
idea have been retired.

The homepage, authoring guide, and bibliography support these two mathematical page types.
The initial sample articles have been deleted.
Their replacement follows `input/requested_articles.txt`: 15 topic articles, three stubs, and three standalone theorem pages with proofs.
Every agent-authored article, stub, and theorem page carries the warning **Agent-generated, not reviewed yet** until the author reviews it.

```text
coarse-phases/
├── README.md
├── AGENTS.md
├── SETUP.md
├── requirements.txt
├── constraints.txt
├── .github/workflows/build-and-deploy.yml
├── tests/                       # Test fixtures stay outside the published site
└── docs/
    ├── conf.py
    ├── index.md
    ├── articles/                # Topic articles with their own definitions
    ├── theorems/                # Standalone results and optional proofs
    ├── about/authoring.md
    ├── bibliography/
    ├── _static/custom.css
    └── _templates/
```

Use descriptive filenames. Add topic subdirectories later if they are useful,
while preserving URLs and semantic identifiers of retained content.

## 4. Mathematical writing and cross-references

Write prose with one sentence per source line, without hard wrapping within a sentence, throughout the wiki.
Put display-math `$$` delimiters on their own lines with no blank lines separating the display from surrounding prose, including inside directives and list items.
When a display interrupts a sentence, keep each surrounding prose portion on one line.
Keep inline mathematics in `$...$`, paragraph breaks between paragraphs, and structural spacing required by MyST targets and directives.

Use the shared mathematical macros defined in `docs/_ext/wiki_macros.py` throughout articles and theorem pages.
The same definitions configure MathJax and the TikZ LaTeX preamble, including script capitals through `mathrsfs`.
The authoring guide lists the calligraphic, script, number-system, operator, and category commands.

Use MyST Markdown for prose and LaTeX mathematics, with `sphinx-proof` for
statements. A definition is authored directly in the appropriate article:

````markdown
(article-bornological-coarse-space)=
# Bornological coarse space

Motivation and related definitions.

```{prf:definition} Bornological coarse space
:nonumber:
:label: def-bornological-coarse-space

The full definition goes here, directly in the article.
```
````

Another article links to it using:

```markdown
See {prf:ref}`bornological coarse space <def-bornological-coarse-space>`.
```

This opens the complete article at the definition. A heading reference such as
`{ref}` with `article-bornological-coarse-space` links to the article's top-level
heading. Equations and intermediate lemmas can also have their own stable labels.

A theorem page should have a descriptive title, a complete statement with all
hypotheses, links to prerequisite articles, and either a proof or an explicit
note that no proof is supplied on the page. An omitted proof is not a claim that
a result is unproved. Distinguish established results from conjectures.

Statements have descriptive headings without visible numbers. Add
`:nonumber:` to definitions, propositions, theorems, and related statement
directives; keep their stable labels for descriptive internal links.

Italicize terms where they are defined, including definitions given in running
prose. Use $Y_E$ for the $E$-fattening of $Y$, with its defining equation on
the Coarse space page unnumbered and preceded by the ordinary target
`(def-fattening)=`. Use descriptive `{ref}` links to this target. Use
$X_{\langle E\rangle}$ for the space with coarse structure generated by $E$.

The exposition should be self-contained. Do not attach literature citations
to definitions, arguments proved on the page, or well-known textbook material.
For a nontrivial result used without proof, cite a publicly available paper
and link directly to it beside the claim; publication on arXiv suffices.
Do not cite private notes or inaccessible manuscripts. The bibliography lists
only public papers actually cited in the articles.

### Commutative diagrams and TikZ

Author diagrams in standalone MyST `{tikz}` directives. For a commutative
diagram, set `:libs: cd`, provide a plain-text `:alt:` description, and include
the full `\begin{tikzcd}...\end{tikzcd}` environment. Do not place TikZ source in
`$$...$$` or `{math}` blocks. Other TikZ diagrams and libraries use the same
directive; see `docs/about/authoring.md` for syntax.

The GitHub Actions build uses `sphinxcontrib.tikz`, TeX, and `pdf2svg` to produce
SVG images. Authors and readers can use the generated HTML without installing
TeX locally.

### Labels and linking rules

- Every canonical label must be unique across the complete project.
- Prefer descriptive identifiers such as `def-coarse-structure`,
  `thm-descriptive-result`, and `eq-controlled-entourage`.
- Preserve labels when retained articles move or their headings change.
- Write each definition once in its owning article, not in an include fragment.
- An informal description of a result links to its full statement; do not copy
  the formal statement into multiple pages or embed a theorem page as a fragment.
- References are ordinary links to standalone pages, not popup definitions.

The strict build command is:

```bash
python -m sphinx -b html -n -W --keep-going docs docs/_build/html
```

Warnings fail the build. Checks cover duplicate labels and unresolved references,
but do not verify mathematical correctness. Automated mathematical interaction
tests use temporary fixtures outside the published documentation; the site itself
must not retain demonstration articles solely for testing.

## 5. Proofs and reader interactions

The site should render formal results prominently while allowing proofs to be collapsed by default.

An optional collapsible proof block is:

`````markdown
````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Detailed proof goes here.
```
````
`````

This uses `sphinx-proof` inside a native `sphinx-design` dropdown. Long theorem
pages can use ordinary sections for intermediate lemmas and stages of a proof;
collapsing the entire argument is not required. `sphinx-togglebutton` remains
available for titled technical remarks. A future global proof switch would need
additional implementation.

Also desirable:

- responsive layout on desktop and mobile;
- left navigation listing all articles followed by all theorem pages;
- central, readable mathematical article column;
- right-hand table of contents and **Edit this page** link;
- customizable colors, fonts, article width, theorem boxes, and dark mode;
- optional collapsible examples and technical remarks via `sphinx-design`.

**PyData Sphinx Theme** is the current preferred starting point, but the exact visual layout is not yet fixed.

## 6. Editing and collaboration

Initially the principal author will be the primary contributor. Selected colleagues may be granted access; outside contributions can be considered later.

On 10 November 2026, the author chose a direct-push workflow for work in this workspace:

1. An author or Codex edits `.md` files locally or in GitHub's browser editor.
2. Codex commits and pushes completed changes directly to **`main`**, without requiring a pull request or a separate merge approval.
3. GitHub Actions runs Sphinx and browser checks after each push; Codex repairs failures and refreshes the fixed local preview from a successful run.
4. Saving a draft does not mark the mathematics as reviewed; the author reviews mathematical claims, notation, references, and the rendered output before publication.
5. Publication remains disabled until explicitly requested by the author.
6. Once publication is enabled, successful builds of `main` publish the updated site to GitHub Pages.

A theme-provided **Edit this page** link can lead from a public article to its source on GitHub. This is not a built-in, direct on-site editor; contributors generally need a GitHub account to propose changes. The PyData Sphinx Theme supports configuring source-edit links through `html_theme_options` and `html_context`.

Pull requests remain available when explicitly requested or when collaborators need a separate review process.
Revisit branch protection when preparing publication or inviting collaborators.

### Codex policy

Codex may help to:

- draft articles from supplied mathematical material and instructions;
- create or revise definitions, examples, and expository explanations;
- add cross-references and navigation links;
- search for existing terms and labels before creating new ones;
- identify missing links, duplications, and structural inconsistencies;
- run Sphinx builds and propose repairs;
- commit and push completed workspace edits to `main`, using pull requests only when requested or needed for collaboration.

Codex should **not** be given an unrestricted autonomous publishing role initially. Automatically passing a build test does not certify that a theorem, argument, citation, or physical interpretation is correct. Literature references should be checked against original sources.

## 7. Building, error reporting, and publication

GitHub Actions is a workflow system configured with YAML files in `.github/workflows/`. A workflow can run:

- when a pull request is opened or updated: **validate** only;
- when a change reaches `main`: **validate**, and deploy only when publication is enabled;
- optionally, when launched manually from the repository's Actions tab.

A build job typically performs:

```text
Check out repository
→ Set up Python
→ Install requirements.txt
→ Install TeX and pdf2svg for TikZ diagrams
→ sphinx-build -b html -n -W --keep-going ...
→ On main only, upload generated HTML as a Pages artifact
→ Deploy to GitHub Pages
```

GitHub Pages should be configured with **GitHub Actions** as its publishing source. Use GitHub's official Pages actions (configuration, artifact upload, and deployment) rather than relying on a continuously running Sphinx installation.

**Where to find failures:** In the GitHub repository's **Actions** tab and in the checks attached to a pull request. Logs show Sphinx warnings/errors and the files involved. A failed build should prevent deployment; the previously successful published version remains available.

Builds and browser checks run on GitHub Actions. Edit source locally and download
the generated HTML for review; a local Sphinx installation is not required.
No Python installation is required on the existing PHP hosting package.

## 8. Configuration

The implemented configuration is in `docs/conf.py`. Website dependencies and
transitive version pins are in `requirements.txt` and `constraints.txt`.

The extensions are MyST Parser, sphinx-proof, sphinx-togglebutton, sphinx-design,
sphinxcontrib.tikz, MathJax, and Sphinx's GitHub Pages support. TikZ diagrams use
the SVG output mode, with TeX and `pdf2svg` installed on the GitHub Actions runner.
The theme is PyData. The configuration
uses the actual `MatthiasLudewig/coarse-phases` repository and links preview edits
to the branch used for that build; the normal workspace preview and published pages link edits to `main`.

`docs/index.md` supplies navigation.
Its hidden glob toctrees automatically list all pages in `docs/articles/` under **Articles**, followed by all pages in `docs/theorems/` under **Theorem pages**, in filename order.
Stubs belong to the article list, and adding or removing files requires no menu edit.
Only the sidebar displays these two lists; the homepage contains the introduction and links to the authoring guide and bibliography.
The first requested collection is drafted.
There is no shared definition-fragment directory or special source exclusion
for one. Keep generated `_build` directories excluded from source discovery.

GitHub Actions performs the build and browser checks. Publication is gated on a
public repository, the `main` branch, and `ENABLE_PAGES=true`; it is disabled
throughout private drafting.

## 9. Hosting, cost, and portability

Drafting takes place in the **private GitHub repository**, with builds and downloadable previews produced by GitHub Actions. Publication is disabled. When the author requests publication, the intended arrangement is a public repository with GitHub Pages, subject to GitHub's quotas and service conditions. Sphinx and its discussed extensions/themes are open source. AI-assisted Codex usage is subject to the user's ChatGPT/Codex plan and usage limits.

No additional MySQL database, PHP environment, or VPS is needed for the public static site.

If the source must remain private at publication, review the relevant GitHub plan/Pages restrictions and alternatives. The generated HTML can alternatively be deployed to the user's **existing personal webspace**, independently of its current PHP/MySQL site. A custom subdomain can be attached to GitHub Pages without moving the homepage.

The Markdown source remains portable. The Sphinx-specific directive syntax is not necessarily rendered correctly by generic Markdown wiki engines, so portability is high for prose/data but not completely universal for mathematical environments.

## 10. Features to consider later (not part of the initial build)

- **Backlinks:** display pages that cite or link to the current definition or theorem.
- **Semantic relationships:** distinguish links such as *depends on*, *generalizes*, *equivalent to*, *example of*, or *used in proof of*.
- **Dependency graph:** generate navigable visual graphs from explicit metadata/references.
- **Automatic indexes:** all definitions, theorems, conjectures, examples, and open problems.
- **Bibliography management:** consistent BibTeX/DOI citations, possibly via a Sphinx citation extension.
- **Improved editing UI:** a Git-backed front end for less technically experienced contributors, if the GitHub workflow becomes a barrier.
- **Global proof toggle:** a JavaScript control to open or close all proofs on a page.

These are achievable with extensions or custom development but should not be mistaken for built-in capabilities of a fresh Sphinx installation.

## 11. Established decisions and remaining choices

The repository is `MatthiasLudewig/coarse-phases`, private during drafting.
The site title is **Coarse Geometry and Topological Phases**. PyData is the
current theme; its HTML layout can be changed later. The two mathematical page
types and definition ownership rules are specified above and in the authoring
guide.
Builds run on GitHub Actions, and completed workspace changes are committed and pushed directly to `main`.
Mathematical review remains a separate step before publication.

Remaining choices:

1. **Article review and taxonomy:** review the first requested collection and
   refine its navigation as the wiki grows.
2. **Publication timing and domain:** the author decides when to make the
   repository public and enable Pages, and whether to use a custom subdomain.
3. **Editorial refinements:** presentation details can be adjusted as the first
   articles are reviewed; retain unnumbered statements and stable labels.
4. **Bibliography and licensing:** citation format and licence for reuse of the
   mathematical exposition.
5. **Visual design:** further PyData layout and styling changes.
6. **Contributors:** access and review arrangements for invited colleagues.

## 12. Implementation and acceptance criteria

The private repository and initial Sphinx infrastructure have been created.
The original five demonstration articles and definition fragment have been
removed following the author's revised editorial decision.

Article collection and remaining steps:

- [x] Receive the author's list of articles to draft.
- [x] Draft regular articles with their own labelled definitions.
- [x] Add standalone theorem pages where a full statement or longer proof is
      useful; include intermediate lemmas as needed. Proofs are optional.
- [x] Link informal discussions to full results and prerequisite definitions.
- [ ] Review the mathematics and rendered output before publication.
- [ ] Decide on a licence and eventual public visibility.
- [ ] Enable Pages and verify the live site when publication is requested.
- [ ] Revisit branch protection and collaboration requirements when preparing publication or inviting contributors.

Acceptance criteria: readers can navigate to full articles, follow links to
labelled definitions in those articles, and open standalone theorem pages with
or without proofs. Articles can retain short results and proofs. Longer theorem
pages can organize arguments using intermediate lemmas. Mathematical content is
not transcluded between pages.
The author's workspace edits are committed and pushed directly to `main`; pull requests remain available for collaboration.
GitHub checks the build, and the author reviews the mathematics before publication.
After publication is explicitly enabled, successful builds of `main` produce the public static site.

## 13. Reference documentation

- Sphinx: <https://www.sphinx-doc.org/>
- Sphinx deployment tutorial: <https://www.sphinx-doc.org/en/master/tutorial/deploying.html>
- MyST Parser: <https://myst-parser.readthedocs.io/>
- MyST include directive: <https://myst-parser.readthedocs.io/en/latest/faq/index.html>
- sphinx-proof: <https://sphinx-proof.readthedocs.io/en/latest/>
- sphinx-togglebutton: <https://sphinx-togglebutton.readthedocs.io/>
- sphinx-design: <https://sphinx-design.readthedocs.io/>
- PyData Sphinx Theme: <https://pydata-sphinx-theme.readthedocs.io/>
- GitHub Pages deployment: <https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages>
- GitHub Pages publishing source: <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>
- GitHub branch protection: <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>

---

*This document records the current requirements, including the revised editorial architecture of 6 November 2026. See `SETUP.md` for the current implementation state.*
