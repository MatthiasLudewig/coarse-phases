# Project brief: A mathematical wiki for coarse geometry and topological phases

**Status:** Planning / architecture selected  
**Last updated:** 4 November 2026  
**Purpose of this document:** Record the intended features, the agreed technical direction, the implementation plan, and decisions that remain open. This is a specification and starting point for implementation, **not** a claim that the repository or website has already been created.

## 1. Project vision

Create a public, wiki-style mathematical knowledge base developing and disseminating a **coarse-geometric framework for topological phases**.

The intended site should be similar in spirit to **nLab**, but focused on this research area. It should function both as:

- a **reference** containing precise mathematical definitions, propositions, theorems, proofs, examples, and literature references; and
- an **expository resource** providing motivation, explanations, conceptual relationships, and connections to topological phases.

Initially, one principal author will create and maintain the content, possibly with a handful of invited colleagues. The contribution model should be able to expand later. AI assistance, especially **Codex**, is expected to help draft, organize, cross-link, and maintain pages, subject to mathematical review before publication.

Key design goals:

1. Markdown and LaTeX-based authoring, with files remaining portable and editable outside the website.
2. Strong, stable cross-references between mathematical objects, not only between pages.
3. Separation between formal mathematical statements and explanatory articles.
4. Reuse of centrally maintained definitions or propositions in different expository contexts.
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
| HTML theme | PyData Sphinx Theme | Preferred starting point; not final |
| Automatic build and validation | GitHub Actions | Chosen |
| Public website hosting | GitHub Pages | Preferred initial hosting |
| Custom URL | Subdomain of existing personal website | Possible later; undecided |
| AI-supported editing | Codex working on the Git repository, using pull requests | Intended workflow |
| MySQL/PHP | Not required for this Sphinx website | Not needed |

**Important distinction:** Sphinx is a *static-site generator*, not a live wiki server. The public site displays pre-generated HTML. Browser-based editing normally follows an **Edit this page → GitHub** link, rather than happening inside the published website itself.

### Architecture

```text
Author, colleague, or Codex
            |
            v
GitHub repository (Markdown source, images, config, workflow)
            |
            | pull request: build and validate; merge to main: publish
            v
GitHub Actions (temporary build machine)
            |
            v
Sphinx + MyST + extensions
  - parse Markdown and LaTeX
  - resolve and check cross-references
  - render definitions, theorems, proofs
  - produce HTML, CSS, JavaScript, search index
            |
            v
GitHub Pages (static hosting)
            |
            v
Public reader's web browser
```

Sphinx runs **when triggered by GitHub Actions**, not whenever a visitor opens a page. Visitors receive the generated HTML. MathJax may render mathematics on the visitor's device. Sphinx supports incremental local builds, though hosted CI jobs may perform clean builds; performance is not expected to be an obstacle for an initial, modest-sized wiki.

### URLs

For a GitHub account `USERNAME` and repository `coarse-phases`, the usual GitHub Pages project URL would be:

`https://USERNAME.github.io/coarse-phases/`

Later the website could use a subdomain such as `https://wiki.example.org/` by configuring the GitHub Pages custom domain and the corresponding DNS record. The existing personal website and its MySQL database can remain unchanged.

## 3. Content architecture

Use two related layers of content:

- **Formal layer:** Canonical definitions, propositions, theorems, lemmas, proofs, and constructions, each with stable identifiers when appropriate.
- **Expository layer:** Articles explaining the significance and use of these formal objects, with examples, motivations, relationships, and physical interpretations.

Suggested initial topics include coarse spaces, controlled sets, coarse maps and equivalences, Roe algebras, K-theory, and connections to topological phases. The precise topic taxonomy and terminology should be chosen by the author.

Suggested repository layout (illustrative):

```text
coarse-phases/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── build-and-deploy.yml
└── docs/
    ├── conf.py
    ├── index.md
    ├── geometry/
    │   ├── coarse-spaces.md
    │   └── coarse-maps.md
    ├── algebras/
    │   └── roe-algebras.md
    ├── phases/
    │   └── introduction.md
    ├── reference/
    │   └── coarse-space.md
    ├── _snippets/
    │   └── coarse-space.inc.md
    ├── _static/
    │   └── custom.css
    └── bibliography/
        └── references.bib
```

The directory structure is a proposal, not a constraint. Keep page URLs and semantic identifiers reasonably stable when reorganizing the site.

## 4. Mathematical writing and cross-references

Use MyST Markdown for prose and LaTeX mathematics, with the `sphinx-proof` extension for formal statements.

Example in a canonical article:

````markdown
```{prf:definition} Coarse space
:label: def-coarse-space

A **coarse space** is a pair $(X,\mathcal E)$, where
$X$ is a set and $\mathcal E$ is a coarse structure on $X$.
```
````

Another article can refer to it using:

```markdown
See {prf:ref}`def-coarse-space` for the definition.
```

Other available cross-references include labelled headings, equations, figures, theorems, and propositions. This is stronger than ordinary links between Markdown files because references are resolved and checked during the build.

### Rules for labels

- **Every canonical label must be unique across the complete Sphinx project.**
- Prefer descriptive identifiers such as `def-coarse-space`, `prop-coarse-invariance`, and `eq-controlled-entourage`.
- Labels should remain stable even when articles move or displayed theorem numbers change.
- A repeated labelled block inserted into several documents creates duplicate targets and must be avoided.
- The CI build should treat Sphinx warnings as failures. If necessary, add a dedicated label-uniqueness check for cases not caught by standard warnings.

Proposed build command:

```bash
sphinx-build -b html -n -W --keep-going docs docs/_build/html
```

Here `-n` requests stricter reference checking, `-W` treats warnings as failures, and `--keep-going` reports more than one problem in a build. These checks catch many structural errors; **they do not verify mathematical correctness**.

### Modular statements and inclusion

MyST supports the `{include}` directive. This allows a formal statement to be maintained once in a separate Markdown fragment and displayed in an explanatory article.

For example, `docs/_snippets/coarse-space.inc.md` might contain only the **body** of a definition, without a label. A canonical page can wrap that content in a *labelled* definition; an explanatory page can reuse the same body in an *unlabelled* box or quote.

Canonical page (illustrative):

`````markdown
# Coarse space

````{prf:definition} Coarse space
:label: def-coarse-space

```{include} ../_snippets/coarse-space.inc.md
```
````
`````

The underlying principle is **one source for the statement, one canonical label**. If the same text is displayed on multiple pages, avoid repeating the labelled directive. The canonical occurrence should be the target of stable citations and links. Numbering of repeated unlabelled displays must be tested and configured deliberately.

Fragments in `docs/_snippets/` should not become standalone public pages; configure Sphinx's source discovery appropriately. Inclusion does **not** create a full mathematical-object database or automatically understand logical dependencies.

## 5. Proofs and reader interactions

The site should render formal results prominently while allowing proofs to be collapsed by default.

A possible proof block is:

````markdown
```{prf:proof}
:class: dropdown

Detailed proof goes here.
```
````

This uses `sphinx-proof` and `sphinx-togglebutton`. The exact presentation should be tested with the selected theme and extension versions. A future **Show all / Hide all proofs** switch would require additional custom JavaScript.

Also desirable:

- responsive layout on desktop and mobile;
- left navigation across subject areas;
- central, readable mathematical article column;
- right-hand table of contents and **Edit this page** link;
- customizable colors, fonts, article width, theorem boxes, and dark mode;
- optional collapsible examples and technical remarks via `sphinx-design`.

**PyData Sphinx Theme** is the current preferred starting point, but the exact visual layout is not yet fixed.

## 6. Editing and collaboration

Initially the principal author will be the primary contributor. Selected colleagues may be granted access; outside contributions can be considered later.

Recommended editorial workflow:

1. An author or Codex edits `.md` files locally or in GitHub's browser editor.
2. Changes are submitted as a **pull request** rather than pushed directly to the publication branch.
3. GitHub Actions runs Sphinx and displays success or failure checks on the pull request.
4. The author reviews mathematical claims, notation, references, and the rendered output, then approves or revises the change.
5. An approved pull request is merged into `main`.
6. A successful build of `main` automatically publishes the updated site to GitHub Pages.

A theme-provided **Edit this page** link can lead from a public article to its source on GitHub. This is not a built-in, direct on-site editor; contributors generally need a GitHub account to propose changes. The PyData Sphinx Theme supports configuring source-edit links through `html_theme_options` and `html_context`.

Set a repository branch protection rule so that required build checks and, when collaborators are involved, review requirements must pass before merging. Direct pushes to `main` should be restricted for a reliable approval process.

### Codex policy

Codex may help to:

- draft articles from the author's notes and instructions;
- create or revise definitions, examples, and expository explanations;
- add cross-references and navigation links;
- search for existing terms and labels before creating new ones;
- identify missing links, duplications, and structural inconsistencies;
- run Sphinx builds and propose repairs;
- create pull requests for editorial approval.

Codex should **not** be given an unrestricted autonomous publishing role initially. Automatically passing a build test does not certify that a theorem, argument, citation, or physical interpretation is correct. Literature references should be checked against original sources.

## 7. Building, error reporting, and publication

GitHub Actions is a workflow system configured with YAML files in `.github/workflows/`. A workflow can run:

- when a pull request is opened or updated: **validate** only;
- when a change reaches `main`: **validate and deploy**;
- optionally, when launched manually from the repository's Actions tab.

A build job typically performs:

```text
Check out repository
→ Set up Python
→ Install requirements.txt
→ sphinx-build -b html -n -W --keep-going ...
→ On main only, upload generated HTML as a Pages artifact
→ Deploy to GitHub Pages
```

GitHub Pages should be configured with **GitHub Actions** as its publishing source. Use GitHub's official Pages actions (configuration, artifact upload, and deployment) rather than relying on a continuously running Sphinx installation.

**Where to find failures:** In the GitHub repository's **Actions** tab and in the checks attached to a pull request. Logs show Sphinx warnings/errors and the files involved. A failed build should prevent deployment; the previously successful published version remains available.

For optional local testing, install the project dependencies and run the same `sphinx-build` command locally. No Python installation is required on the existing PHP hosting package.

## 8. Minimum configuration to implement

Suggested `requirements.txt` (initially unpinned for the prototype; **pin tested versions** before stabilizing deployment):

```text
sphinx
myst-parser
sphinx-proof
sphinx-togglebutton
sphinx-design
pydata-sphinx-theme
```

Illustrative `docs/conf.py`:

```python
project = "Coarse Geometry and Topological Phases"

extensions = [
    "myst_parser",
    "sphinx_proof",
    "sphinx_togglebutton",
    "sphinx_design",
    "sphinx.ext.mathjax",
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
]

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
}
html_context = {
    "github_user": "USERNAME",
    "github_repo": "coarse-phases",
    "github_version": "main",
    "doc_path": "docs",
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]
exclude_patterns = ["_build", "_snippets/**"]
nitpicky = True
```

The `USERNAME`, repository name, and actual theme settings must be updated. The configuration is a **starting point**, not yet tested against a created repository. A Sphinx `toctree` in `docs/index.md` should define the initial navigation. A proper deployment workflow YAML must be added and tested.

## 9. Hosting, cost, and portability

The intended starting arrangement uses a **public GitHub repository + GitHub Actions + GitHub Pages**, which can operate under free GitHub offerings for normal public-project use, subject to GitHub's current quotas and service conditions. Sphinx and its discussed extensions/themes are open source. AI-assisted Codex usage is subject to the user's ChatGPT/Codex plan and usage limits.

No additional MySQL database, PHP environment, or VPS is needed for the public static site.

If a private repository is needed later, review the relevant GitHub plan/Pages restrictions and alternatives. The generated HTML can alternatively be deployed to the user's **existing personal webspace**, independently of its current PHP/MySQL site. A custom subdomain can be attached to GitHub Pages without moving the homepage.

The Markdown source remains portable. The Sphinx-specific directive syntax is not necessarily rendered correctly by generic Markdown wiki engines, so portability is high for prose/data but not completely universal for mathematical environments.

## 10. Features to consider later (not part of the initial build)

- **Backlinks:** display pages that cite or link to the current definition or theorem.
- **Semantic relationships:** distinguish links such as *depends on*, *generalizes*, *equivalent to*, *example of*, or *used in proof of*.
- **Dependency graph:** generate navigable visual graphs from explicit metadata/references.
- **Automatic indexes:** all definitions, theorems, conjectures, examples, and open problems.
- **Bibliography management:** consistent BibTeX/DOI citations, possibly via a Sphinx citation extension.
- **Improved editing UI:** a Git-backed front end for less technically experienced contributors, if the GitHub workflow becomes a barrier.
- **Advanced diagrams:** reliable handling of commutative diagrams and TikZ-derived graphics (probably by pre-rendering SVG for content not supported directly by browser-side MathJax).
- **Global proof toggle:** a JavaScript control to open or close all proofs on a page.

These are achievable with extensions or custom development but should not be mistaken for built-in capabilities of a fresh Sphinx installation.

## 11. Decisions still open

1. **Repository identity:** GitHub user/organization and repository name; no actual account or repository has yet been created as part of this plan.
2. **Repository visibility:** public from the start, or private during drafting and public later? Public is simplest for free GitHub Pages hosting.
3. **Domain:** keep the GitHub URL initially or configure a subdomain of the existing personal website.
4. **Site name and scope:** final public title, mathematical taxonomy, and initial entry list.
5. **Editorial conventions:** theorem numbering, identifier conventions, proof style, language, and treatment of conjectures versus established results.
6. **Bibliography and licensing:** citation format and licence for reuse of the mathematical exposition.
7. **Theme:** final PyData layout and detailed visual design.
8. **Initial contributors:** account/access and review rules for invited colleagues.

## 12. Recommended implementation sequence

- [ ] Create a GitHub repository (initially public if free Pages hosting is desired).
- [ ] Add the Sphinx project skeleton, MyST configuration, `requirements.txt`, `.gitignore`, and a GitHub Actions workflow.
- [ ] Choose a minimal `index.md` navigation structure.
- [ ] Create **five interconnected example articles**, sufficient to test definitions, theorems, proofs, references, reusable fragments, and LaTeX rendering.
- [ ] Add at least one proof collapsed by default and one canonical definition reused in an explanatory article without duplicated labels.
- [ ] Confirm that duplicate labels or unresolved references produce an actionable failed build.
- [ ] Configure GitHub Pages deployment and verify the live example site.
- [ ] Enable branch protection and pull-request review procedures.
- [ ] Add an **Edit this page** link and basic custom CSS.
- [ ] Ask Codex to propose a test article through a pull request; inspect the build log and review flow.
- [ ] Decide on a custom domain, bibliography workflow, and licence before wider publication.

**Prototype acceptance criteria:** A reader can browse a public mathematical article, navigate to another article, follow a link to a specific labelled theorem/definition, expand a proof, and open an edit link. A contributor can propose a Markdown edit; GitHub Actions validates it; the author can review it; and an approved merge publishes an updated static site without modifying the existing personal homepage.

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

*This document summarizes current project requirements and proposed implementation details. It can be placed in the future repository as `PROJECT_BRIEF.md` or supplied directly to Codex as the implementation specification.*
