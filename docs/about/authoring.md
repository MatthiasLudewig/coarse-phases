# Writing and reviewing articles

The source is Markdown with MyST directives and LaTeX mathematics.
Use the **Edit on GitHub** link to propose a change to the current page.

## Two mathematical page types

**Regular articles** live in `docs/articles/`.
Each article develops a topic through motivation, definitions, examples, and explanations.
Put definitions directly in the article where they belong.
For example, an article titled *Bornological coarse space* can define coarse structure, bornological space, and bornological coarse space, each with its own label.

**Theorem pages** live in `docs/theorems/`.
Each presents a full formal result with all its hypotheses.
It may include a proof, or explicitly say that the proof is omitted and give a literature reference when available.
Long proofs can be developed using sections, intermediate lemmas, and supporting arguments.
Include links back to the related articles and to prerequisite definitions.

Both types are standalone pages.
An article may explain a result informally and link to the formal statement on its theorem page.
Articles may also contain theorems and short proofs directly: a separate theorem page is useful when a long argument would interrupt the exposition, not mandatory for every result.

The homepage, this guide, and the bibliography are supporting site pages, not additional mathematical page types.

## Definitions belong to articles

Write each definition once, directly in its owning article.
There is no separate definition-reference layer and no collection of definition fragments.
Do not use `{include}` to reproduce definitions or theorem pages in other articles.

Italicize each term where it is defined, using Markdown emphasis such as `A *coarse structure* on a set ...`.
Do this in both definition blocks and definitions given in running prose.

The following is a syntax illustration for a future article, not drafted mathematical content:

````markdown
(article-bornological-coarse-space)=
# Bornological coarse space

Motivation and overview.

```{prf:definition} Coarse structure
:nonumber:
:label: def-coarse-structure

Write the complete definition here.
```

```{prf:definition} Bornological space
:nonumber:
:label: def-bornological-space

Write the complete definition here.
```

```{prf:definition} Bornological coarse space
:nonumber:
:label: def-bornological-coarse-space

Write the complete definition here.
```

Examples and further discussion.
````

## References open the owning page

From another article, use a reference to the relevant label:

```markdown
See {prf:ref}`coarse structure <def-coarse-structure>`.
See {ref}`article-bornological-coarse-space` for the broader discussion.
```

The first link opens the whole article and scrolls to the definition.
The second opens the article at its labelled heading.
These are normal page links, not embedded excerpts or popup definitions.

Use `{eq}` for numbered equations, `{ref}` with descriptive text for ordinary labels, and ordinary Markdown links for page paths.
All labels must be unique across the project.
Preserve labels and URLs as reviewed content evolves.
Statements have no visible numbers: add `:nonumber:` to each statement directive and use descriptive text for its links.

## Standalone results

Use descriptive filenames such as `theorems/descriptive-result.md`.
A theorem page can be structured as follows:

````markdown
(theorem-descriptive-result)=
# Descriptive result

Context and links to the relevant articles and definitions.

```{prf:theorem} Descriptive result
:nonumber:
:label: thm-descriptive-result

Full hypotheses and formal statement.
```

## Supporting lemmas

Supporting results, when needed, with their own labels and proofs.

## Proof

The full argument, or an explicit note that no proof is supplied here.

## Related articles

Links to the motivating articles.
````

An article can give an informal description and then link to the result:

```markdown
Informally, the result says ... .
See {prf:ref}`the full statement <thm-descriptive-result>` and its proof.
```

Adjust the wording if the target page does not supply a proof.
Avoid duplicating the full formal statement in both places.
Do not confuse an omitted proof with an unknown proof or a conjecture; state the status accurately.

## Literature citations

Write definitions and explanations so that they can be read on their own.
Do not add literature citations for definitions, self-contained arguments, or well-known textbook material.
Keep ordinary internal links to prerequisite articles and named statements.

When using a nontrivial result without giving its proof, cite a publicly available paper and link directly to it beside the claim.
An arXiv preprint is sufficient.
Do not cite private notes or inaccessible manuscripts.
List only the papers actually cited in the bibliography; a routine Sources section is unnecessary.

## Mathematical formatting and proofs

Write prose with one sentence per source line.
Do not wrap a sentence across multiple lines, even when it is long.
Apply this to all wiki pages, including prose inside definitions, proofs, other directives, and list items.
Keep blank lines between paragraphs, and preserve the syntax of code blocks, tables, and mathematics.

Use `$x\in X$` for inline mathematics and `$$...$$` for a display.
Use the shared macros below, such as `\cA` for $\cA$.
Keep braces around letters in macro definitions, as in `\mathcal{A}`.
Write bornological coarse spaces as $(X, \cB, \cC)$, with the bornology before the coarse structure.
Use a `{math}` directive with `:label:` for a numbered equation.
For an unnumbered equation with a text link, put an ordinary MyST target before the block and omit both `:label:` and `:name:` inside it; either option creates numbering.
Put the `$$` delimiters on their own lines, with no blank line between the display and the surrounding prose:

```markdown
For every real number $x$, we have
$$
x^2\geq 0,
$$
with equality exactly when $x=0$.
The next sentence starts on its own line.
```

A display may interrupt a sentence; keep each prose portion before or after it on one line.
The same spacing rule applies inside definitions, proofs, and list items; indent displays to match the containing list item.
The wiki configuration enables MyST's `myst_dmath_double_inline` option so these displays are recognized within prose.
Preserve structural spacing required by MyST targets and directives.

Write the $E$-fattening of a subset $Y$ as $Y_E$.
Its {ref}`defining equation <def-fattening>` on the Coarse space page is unnumbered and labelled as follows:

````markdown
(def-fattening)=

```{math}
Y_E:=\{x\in X:\exists y\in Y,\ (x,y)\in E\}.
```
````

Refer to it using a word or phrase as the link text:

```markdown
The {ref}`thickening <def-fattening>` of $Y$ is denoted by $Y_E$.
```

For a compound set, group it before adding the subscript, as in `$(Y\cup Z)_E$`.
Write `$X_{\langle E\rangle}$` for the space whose coarse structure is generated by $E$, so that this construction has distinct notation.

A short proof can stay with a theorem inside an article.
To make a proof collapsible, use a native dropdown around `prf:proof`:

`````markdown
````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Your proof goes here.
```
````
`````

This starts closed and also works without JavaScript.
On a long theorem page, use ordinary sections for the supporting lemmas and stages of the argument; collapsible proof blocks are optional and should preserve readability.
For a technical remark, an admonition with `:class: dropdown` uses `sphinx-togglebutton`.
Do not attach that class directly to `prf:proof`, whose generated HTML differs from a titled admonition.

## Shared mathematical macros

The definitions in `docs/_ext/wiki_macros.py` are available on every page, including mathematics in headings and navigation, and inside TikZ diagrams.
The configuration loads the same definitions into MathJax and the diagram LaTeX preamble, with `mathrsfs` supplying script letters in diagrams.
Add or update a macro in this central file so the two renderers stay consistent.
Use these macros instead of spelling out their expansions in articles and theorem pages.

| Macros | Meaning | Example |
| --- | --- | --- |
| `\cA` through `\cZ` | Calligraphic capitals, `\mathcal{A}` through `\mathcal{Z}` | $\cA,\cB,\cC$ |
| `\sA` through `\sZ` | Script capitals, `\mathscr{A}` through `\mathscr{Z}` | $\sA,\sB,\sH$ |
| `\N`, `\Z`, `\Q`, `\R`, `\C` | Blackboard-bold number systems | $\N,\Z,\Q,\R,\C$ |
| `\BornCoarse`, `\Set`, `\Cat`, `\Ab`, `\Grp`, `\Vect`, `\Hilb`, `\Top`, `\Sp` | Upright category names | $\BornCoarse,\Hilb,\Sp$ |

The following commands produce upright mathematical operators with operator spacing:

```latex
\Mat \End \Hom \Aut \Inn \id \Der
\ind \tr \str \Tr \Str \supp \ch \ker \coker \spec
\lim \colim \Var \Exp \dom \ran
\Loc \Az \Con \CAR \Cl \Fun \Ad \ad \Tot
```

The standard commands `\ker` and `\lim` already exist and retain their usual definitions.
Write `\mathop{\colim}_{i\in I}` when an index should appear below a colimit in display style, as with `\operatorname*{colim}`.
Command names are case-sensitive: for example, `\tr` and `\Tr` are distinct.
Before an immediately following letter, end the command with braces, as in `\cA{}x`.

For example:

```markdown
A coarse space is written $(X, \cB, \cC)$.
For $V\in\Vect$, consider $\End(V)$ and $\id_V$.
```

## Commutative diagrams and TikZ

Use a standalone `{tikz}` directive for a commutative diagram.
Load the `cd` library and include the complete `tikzcd` environment:

````markdown
```{tikz}
:libs: cd
:alt: A commutative square with maps f from A to B, g from A to C, h from B to D, and k from C to D.

\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, "k"'] & D
\end{tikzcd}
```
````

Do not put the directive or `tikzcd` environment inside `$$...$$` or a `{math}` block.
Those blocks use MathJax; the `{tikz}` directive uses `sphinxcontrib.tikz` to compile the diagram to SVG during the GitHub Actions build.
The downloaded HTML preview includes the resulting image, so authors and readers do not need a local TeX installation.

Diagrams follow the surrounding text size and color and have transparent backgrounds in both light and dark mode.
Use the normal TeX font size; a manual `\Large` adjustment is unnecessary.
Explicit TikZ colors are retained.
Wide diagrams scroll horizontally on small screens so their labels remain readable.

Give each diagram a plain-text `:alt:` description of its objects, arrows, and relevant relationships.
Explain any mathematical conclusion in the surrounding text as well.
Other TikZ diagrams can use a complete `tikzpicture` environment in the same directive.
Add the required TikZ library names to `:libs:`, separated by commas, for example `:libs: arrows.meta,positioning`.

## Conventions, navigation, and review

- In this wiki, *coarse space* abbreviates *bornological coarse space*.
  A coarse map is controlled and proper.
  State other conventions where first needed.
- Distinguish definitions, established results, conjectures, and physical interpretations, and state the hypotheses of each result explicitly.
- Navigation lists all pages in `docs/articles/` under **Articles**, followed by all pages in `docs/theorems/` under **Theorem pages**, in filename order.
  The lists update automatically at each build, including stubs; adding or removing a page requires no menu edit.
- Check citations against original sources.
  Add the sources needed by the actual articles to the bibliography; do not import a speculative reading list.
- For the author's work in this workspace, commit and push completed edits directly to `main`.
  Routine edits do not require a pull request or a separate merge approval.
  GitHub Actions checks the build and reader interactions after each push; repair any failures.
  Refresh the fixed local preview from the successful run with `python3 scripts/update_preview.py --run RUN_ID`.
  Open `.preview/html/index.html` once and refresh the same browser tab after later updates.
  The helper downloads `wiki-html` and overwrites the same folder; no local Sphinx installation is needed.
- The principal author reviews the mathematics before publication.
  Saving a draft on `main` does not mark it as reviewed.
  Passing CI does not verify correctness.

The author chose this direct-push workflow on 10 November 2026 for work carried out in this workspace.
Pull requests remain available when explicitly requested or when collaborators need a separate review process.
Publication remains disabled until the author requests it.

The sample articles were deleted following the editorial decision of 6 November 2026.
The first replacement collection follows the author's requested article list.
Every agent-authored article, stub, and theorem page must retain the warning `Agent-generated, not reviewed yet` until reviewed by the author.
