# Coarse Geometry and Topological Phases

A mathematical wiki built with **Sphinx, MyST Markdown, and the PyData theme**.
The first requested collection contains 15 topic articles, three stubs, and three standalone theorem pages with proofs.
Unreviewed mathematical pages retain `Agent-generated, not reviewed yet`.

## Content model

There are two kinds of mathematical pages:

- **Articles** combine definitions, motivation, examples, and discussion. Each
  definition is written directly in its owning article. References point to its
  label and open that complete article; definitions are not included as shared
  fragments in other pages.
- **Theorem pages** contain full formal statements, with or without proofs.
  Longer proofs may include intermediate lemmas and supporting arguments.
  Articles can state the idea informally and link to the theorem page.

Both types are standalone. Theorems and short proofs can also stay directly in
articles when this keeps the exposition clear. This architecture supersedes the
original definition/exposition split and shared-fragment design.

Statements have descriptive headings without visible numbering. Definitions
and self-contained arguments do not need literature citations; nontrivial
results used without proof link directly to public papers, including arXiv
preprints.

## Drafting and previewing

The repository starts **private**. Sphinx runs on **GitHub Actions**; contributors
do not need to install Python or Sphinx on their computers.

1. Edit a Markdown page in `docs/` in this workspace or in GitHub's browser editor.
2. Commit and push completed changes directly to **`main`**.
   Routine work in this workspace does not require a pull request or a separate merge approval.
3. Wait for **Wiki checks**. In its Actions run, download the `wiki-html` artifact.
4. Refresh the fixed local preview as described below, or extract the entire ZIP
   and open `index.html` in your browser. Follow links,
   inspect equations, and expand proofs. The `wiki-screenshots` artifact contains
   desktop, dark-mode, and mobile screenshots from the browser checks.
5. Repair any failed checks and review the mathematics before publication.
   Saving a draft on `main` does not mark it as reviewed.
   A build success only verifies the website's structure and tested interactions.

This direct-push workflow follows the author's decision of 10 November 2026.
Pull requests remain available when explicitly requested or for future collaboration.

Direct file previews support browsing and proofs. Sphinx search works best over
HTTP, such as the eventual Pages site; MathJax rendering needs internet access.
Artifacts expire after seven days; rerun a workflow to generate a fresh preview.

### Fixed local HTML folder

Always refresh the local preview in **`.preview/html/`**. Open
`.preview/html/index.html` once and keep that browser tab: later updates
overwrite the same files, so refreshing the browser shows the new build.
Do not create a new dated preview folder for each edit.

After **Wiki checks** succeeds, use its Actions run ID:

```bash
python3 scripts/update_preview.py --run RUN_ID
```

This helper requires Python 3 and an authenticated GitHub CLI (`gh`), but no
local Sphinx installation. It downloads the successful run's `wiki-html`
artifact into a temporary directory before replacing files in `.preview/html/`,
removes obsolete generated files, and records the run and commit in
`.preview/html/.build-info.json`. The preview stays out of Git. Refresh only
after the command finishes; a failed download leaves the previous preview intact.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/articles/` | Regular articles, including their own labelled definitions |
| `docs/theorems/` | Standalone formal results and optional proofs |
| `docs/about/authoring.md` | Authoring conventions and syntax illustrations |
| `docs/bibliography/` | Literature references for the articles as they are drafted |
| `docs/conf.py`, `docs/_static/custom.css` | Sphinx configuration and appearance |
| `.github/workflows/build-and-deploy.yml` | Validation, previews, optional deployment |
| `scripts/update_preview.py` | Refresh the fixed `.preview/html/` folder from a successful CI run |
| `tests/` | Build-failure checks and browser acceptance checks |

`input/` contains local research material and is deliberately ignored by Git.
`coarse_geometry_topological_phases_wiki_project_brief.md` records the
requirements, including the revised architecture of 6 November 2026;
implementation status and remaining decisions are in
[`SETUP.md`](SETUP.md).

## Publishing later

Publication is disabled by default. When the author requests publication:

1. Review the draft, choose a licence, and make this repository public.
2. Under **Settings → Pages**, choose **GitHub Actions** as the publishing source.
3. Under **Settings → Secrets and variables → Actions → Variables**, create the
   repository variable `ENABLE_PAGES` with value `true`.
4. Run **Build and deploy wiki** on `main`, or push a change to `main`.

The workflow deploys only from `main`, only for a public repository, and only
when `ENABLE_PAGES` is `true`. Pull requests never deploy. The expected URL is
<https://matthiasludewig.github.io/coarse-phases/>; it is not live during drafting.

On GitHub Free, Pages and enforced branch protection require a public repository.
The current sole-author workflow uses direct pushes to `main`.
Revisit branch protection and review requirements when preparing publication or inviting collaborators.
See [Pages eligibility](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Build details

CI uses Python 3.13 and pinned dependencies. Its strict build command is:

```bash
python -m sphinx -b html -n -W --keep-going docs docs/_build/html
```

Warnings fail the build. Tests also deliberately introduce a duplicate theorem
label and unresolved references in temporary copies and require those builds to
fail. Chromium checks the site's navigation, search, edit URLs, and mobile layout,
as well as the actual articles' review warnings, mathematical rendering, and links.
Separate temporary fixtures check links to definitions in full articles,
standalone theorems with and without proofs, inline results, proof expansion,
and MathJax. Fixtures are never included in the preview artifacts.
No external link checker blocks ordinary
edits on temporary failures at literature sites.

## Licence

No reuse licence has been selected yet. Choose one before wider publication.
