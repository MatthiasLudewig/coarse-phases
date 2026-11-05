# Working on this wiki

- Read the project brief and `docs/about/authoring.md` before changing content.
- Use MyST Markdown. Keep formal statements in `docs/reference/` and exposition
  in the subject directories. Preserve existing semantic labels and URLs.
- Here, "coarse space" abbreviates **bornological coarse space**. State the
  bornology, and distinguish controlled maps from proper, controlled coarse maps.
- Reusable fragments contain statement bodies, never canonical labels. A label
  is declared once. Expository restatements use an unnumbered admonition.
- Mathematical content is a draft until the principal author reviews it. Verify
  literature citations against original sources. Passing CI is not mathematical
  verification. Do not invent references, claims of completeness, or reviews.
- Make changes on a branch and submit a pull request. Do not merge mathematical
  drafts, make the repository public, or enable Pages without the author's request.
- Sphinx builds and browser checks run on GitHub Actions. Do not require a local
  Sphinx installation. Local source editing and viewing downloaded HTML are fine.
- Keep `input/`, local environments, credentials, and generated builds out of Git.
- Keep the build check named `Wiki checks` stable for future branch protection.
- Do not run Homebrew installs, upgrades, or cleanup for ordinary wiki work.
