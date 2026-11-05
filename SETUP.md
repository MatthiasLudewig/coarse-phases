# Setup and editorial decisions

## Implemented in the initial draft

- Private repository: `MatthiasLudewig/coarse-phases`.
- Sphinx/MyST project, pinned dependencies, PyData theme, MathJax, and custom CSS.
- Five connected mathematical articles, with distinct reference and exposition
  layers, a reading list, and an authoring guide.
- A definition body included in two places with one canonical label; its
  expository restatement is an unnumbered admonition.
- A theorem with a proof in a native, initially collapsed `sphinx-design`
  dropdown containing `prf:proof`. This avoids assuming that a bare proof node
  has the title structure expected by `sphinx-togglebutton`.
- GitHub edit links, search, navigation, light/dark themes, and responsive layout.
- GitHub-hosted strict builds, negative build tests, browser checks, downloadable
  HTML, and screenshot artifacts. Logs and checks are attached to the pull request.
- Pages workflow prepared but gated off during private drafting.

## Author review before the first merge

- Check the bornological convention and terminology in the five starter pages.
- Review all statements, proofs, hypotheses, and physical interpretations.
- Decide whether to expand the initial topic list using the local research notes.
- Theorem numbering currently uses Sphinx's project-wide sequence (no section
  prefix). Cite semantic labels rather than displayed numbers.

## Deliberately pending

- Mathematical approval and merge of the initial draft.
- Public visibility, enabling Pages, and verification of the live site.
- Branch protection: not available for this private repository on GitHub Free.
- A reuse licence, invited collaborators, and any custom domain.
- Bibliography automation. BibTeX is retained for later use; the current reading
  list uses explicit, checked links rather than a citation extension.
- Backlinks, dependency graphs, automatic object indexes, and a global proof
  toggle are future work, as described in the project brief.
