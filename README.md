# Coarse Geometry and Topological Phases

A mathematical wiki built with **Sphinx, MyST Markdown, and the PyData theme**.
The first five interconnected articles are drafts for the author's review.

## Drafting and previewing

The repository starts **private**. Sphinx runs on **GitHub Actions**; contributors
do not need to install Python or Sphinx on their computers.

1. Open a Markdown page in `docs/` on GitHub and select the pencil to edit it.
2. Commit the change to a **new branch** and open a pull request.
3. Wait for **Wiki checks**. In its Actions run, download the `wiki-html` artifact.
4. Extract the entire ZIP, then open `index.html` in your browser. Follow links,
   inspect equations, and expand proofs. The `wiki-screenshots` artifact contains
   desktop, dark-mode, and mobile screenshots from the browser checks.
5. Review the mathematics and merge when satisfied. A build success only verifies
   the website's structure and tested interactions.

Direct file previews support browsing and proofs. Sphinx search works best over
HTTP, such as the eventual Pages site; MathJax rendering needs internet access.
Artifacts expire after seven days; rerun a workflow to generate a fresh preview.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/reference/` | Canonical definitions and results with stable labels |
| `docs/geometry/`, `algebras/`, `phases/` | Explanations and connections |
| `docs/_snippets/` | Shared statement bodies, excluded as standalone pages |
| `docs/about/authoring.md` | Authoring conventions and working examples |
| `docs/bibliography/` | Reading list and portable BibTeX records |
| `docs/conf.py`, `docs/_static/custom.css` | Sphinx configuration and appearance |
| `.github/workflows/build-and-deploy.yml` | Validation, previews, optional deployment |
| `tests/` | Build-failure checks and browser acceptance checks |

`input/` contains local research material and is deliberately ignored by Git.
The original `coarse_geometry_topological_phases_wiki_project_brief.md` records
the requirements; implementation status and remaining decisions are in
[`SETUP.md`](SETUP.md).

## Publishing later

Publication is disabled by default. When the author requests publication:

1. Review the draft, choose a licence, and make this repository public.
2. Under **Settings → Pages**, choose **GitHub Actions** as the publishing source.
3. Under **Settings → Secrets and variables → Actions → Variables**, create the
   repository variable `ENABLE_PAGES` with value `true`.
4. Run **Build and deploy wiki** on `main`, or merge an approved change into `main`.

The workflow deploys only from `main`, only for a public repository, and only
when `ENABLE_PAGES` is `true`. Pull requests never deploy. The expected URL is
<https://matthiasludewig.github.io/coarse-phases/>; it is not live during drafting.

On GitHub Free, Pages and enforced branch protection require a public repository.
Until then, follow the pull-request review procedure manually. After publication,
protect `main`, require `Wiki checks`, disable force pushes and deletion, and
require reviews once a second reviewer is available. A pull-request author cannot
approve their own pull request, so a mandatory approval can block a sole author.
See [Pages eligibility](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Build details

CI uses Python 3.13 and pinned dependencies. Its strict build command is:

```bash
python -m sphinx -b html -n -W --keep-going docs docs/_build/html
```

Warnings fail the build. Tests also deliberately introduce a duplicate theorem
label and unresolved references in temporary copies and require those builds to
fail. Chromium checks navigation, canonical links, proof expansion, MathJax,
search, edit URLs, and mobile layout. No external link checker blocks ordinary
edits on temporary failures at literature sites.

## Licence

No reuse licence has been selected yet. Choose one before wider publication.
