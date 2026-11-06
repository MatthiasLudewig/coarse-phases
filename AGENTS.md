# Working on this wiki

- Read the project brief and `docs/about/authoring.md` before changing content.
  The editorial architecture was revised by the author on 6 November 2026.
- Use MyST Markdown and two mathematical page types: regular articles in
  `docs/articles/` and standalone theorem pages in `docs/theorems/`. Both are
  complete, independently navigable pages. Preserve labels and URLs of retained
  content; the initial demonstration articles have intentionally been deleted.
- Put each definition directly in its owning article, alongside motivation,
  related definitions, examples, and discussion. For example, the Coarse space
  article defines coarse structure, bornological space, and bornological coarse
  space, each with its own stable label.
- Refer to definitions using ordinary cross-document links to those labels.
  Following a link must load the whole owning article at the target. Do not
  transclude definitions or maintain separate shared definition fragments.
- An article may informally describe a result and link to a theorem page holding
  the full formal statement. Theorem pages may have a proof or omit it, and can
  contain prerequisite links, intermediate lemmas, and long arguments. State
  whether a proof is supplied or omitted; never invent one to fill a template.
- Short theorems and proofs are also allowed within articles. A separate theorem
  page is an editorial option for keeping articles concise, not a requirement
  for every result. Avoid duplicating the same formal statement on both pages.
- Give standalone theorem pages a descriptive title, an explicit statement with
  all hypotheses, and links to the relevant articles. Keep page and statement
  labels unique. Do not embed theorem pages into articles as fragments.
- Here, "coarse space" abbreviates **bornological coarse space**. State the
  bornology, and distinguish controlled maps from proper, controlled coarse maps.
- The sample articles and their sample bibliography have been removed. The first
  requested collection is now drafted from `input/requested_articles.txt` and the
  supplied mathematical sources. Keep the exact warning
  `Agent-generated, not reviewed yet` on every agent-authored article, stub, and
  theorem page until the author has reviewed it. See `docs/about/draft-review.md`
  for source conventions and mathematical qualifications requiring review.
- Test-only fixtures belong under `tests/` or in temporary build directories,
  never in the published documentation or its navigation.
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
