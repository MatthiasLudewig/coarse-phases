# Writing and reviewing articles

The source is ordinary Markdown with MyST directives and LaTeX mathematics.
Use the **Edit on GitHub** link to propose a change to the current page.

## Editorial conventions

- Put canonical statements in `reference/`; put motivation and applications in
  the subject directories. State all hypotheses and distinguish definitions,
  established results, conjectures, and physical interpretations.
- In this wiki, *coarse space* means *bornological coarse space*. A coarse map
  is controlled and proper. Spell out other conventions when they first arise.
- Use unique, descriptive labels: `def-coarse-space`, `thm-lattice-line`,
  `eq-fermi-projection`. Keep them stable as the text evolves. The displayed
  statement numbers are project-wide and may change when articles are inserted.
- Add each new article to the toctree in `index.md`. Link it to the relevant
  reference statements and related articles.
- Add original sources to the reading list and BibTeX file. Check bibliographic
  details and the hypotheses of cited results against those sources.

## Statements and references

Write a labelled statement using a theorem directive:

````markdown
```{prf:definition} Example title
:label: def-your-new-concept

Your mathematical definition, with $x\in X$ for inline mathematics.
```

See {prf:ref}`def-your-new-concept`.
````

Use `{ref}` for labelled headings, `{eq}` for equations, and ordinary Markdown
links to other `.md` files. The strict build reports unresolved targets.

## One statement body, one canonical label

The body of {prf:ref}`def-coarse-space` lives in `_snippets/coarse-space.inc.md`.
The reference page wraps its include in a labelled `prf:definition`. The
[expository page](../geometry/coarse-spaces.md) wraps the same include in an
unnumbered admonition. Changing the fragment updates both displays.

Fragments must not contain canonical labels. They are excluded from standalone
page discovery, and the explanatory restatement does not consume a theorem
number. Relative include paths are resolved from the including document.

## Collapsible proofs

Use a native dropdown around the proof. It starts closed and also works without
JavaScript:

`````markdown
````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Your proof goes here.
```
````
`````

See {prf:ref}`thm-lattice-line` for a working example. For a technical remark,
use an admonition with `:class: dropdown`; `sphinx-togglebutton` supplies its
expand/collapse button. Do not attach that class directly to `prf:proof`:
its generated HTML differs from a titled admonition.

## Review in GitHub

Create a branch and pull request. GitHub Actions builds the site, checks that
invalid references and duplicate theorem labels fail, and exercises the browser
interactions. Download `wiki-html` from the run to inspect the rendered draft.

The principal author reviews mathematical correctness and decides when to
merge. AI-assisted additions follow the same review process. While the
repository is private on GitHub Free, this is a manual editorial rule; enforce
it with branch protection when the repository becomes public.

## Future features

Backlinks, semantic dependency graphs, automatic statement indexes, and a
site-wide proof switch are not implemented in this initial version. Keep
identifiers stable so these features can be added later.
