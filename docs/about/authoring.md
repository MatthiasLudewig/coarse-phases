# Writing and reviewing articles

This guide explains how to contribute to the wiki using Git, a text editor, and a GitHub account.
You do not need to install Python, Sphinx, or LaTeX: GitHub builds the website for you.
The files are plain text with the extension `.md`.
They use Markdown for ordinary text, LaTeX for mathematics, and a few extra commands shown below.

## Technical instructions

### Where files live

All paths below are relative to the [repository](https://github.com/MatthiasLudewig/coarse-phases).

| Path | What belongs here |
| --- | --- |
| `docs/articles/` | Articles containing motivation, definitions, examples, and discussion; short results and proofs may stay in the article. |
| `docs/theorems/` | Standalone theorem pages containing a full statement and a proof, or an explicit notice that the proof is omitted. |
| `docs/index.md` | The homepage introduction and its links under “About this wiki”. |
| `docs/bibliography/index.md` | Publicly accessible papers cited in the wiki. |
| `docs/about/authoring.md` | This guide. |

Put a definition in the article that explains the corresponding concept.
A theorem page is useful when a statement or proof would make an article too long.
Link between the two pages instead of copying the same formal statement into both.

### Start a contribution

Clone the repository once:

```bash
git clone https://github.com/MatthiasLudewig/coarse-phases.git
cd coarse-phases
```

For each contribution, start from an up-to-date `main` branch and create a branch with a descriptive name:

```bash
git switch main
git pull --ff-only
git switch -c add-my-topic
```

Save or commit any work already in progress before switching branches.
If you do not have permission to push to this repository, fork it on GitHub and clone your fork instead.
A *pull request* proposes merging your branch into the wiki's `main` branch, so the maintainer can review the contribution.
The branch workflow here is intended for collaborators; follow the maintainer's instructions if you have been asked to edit `main` directly.

For a small correction, you can also use **Edit on GitHub** on the relevant wiki page, edit the file in your browser, and propose the change on a new branch.

### Add or edit an article or theorem page

To edit a page, open its `.md` file in your text editor.
To add an article, create a new file directly in `docs/articles/`, with a short filename in lowercase and hyphens, such as `my-topic.md`.
Start with this article stub:

```markdown
(article-my-topic)=
# My topic

This article is a stub.
```

Replace `my-topic` and `My topic` with your subject.
The line in parentheses is a stable label for links to this page; the line beginning with `#` is the title readers see.
Replace the stub sentence with your introduction, definitions, examples, and discussion as you develop the article.

For a standalone theorem page, create a file directly in `docs/theorems/`, such as `my-result.md`:

```markdown
(theorem-my-result)=
# My result

This article is a stub.
```

Develop it using the theorem and proof examples in the second section below.
State all hypotheses, link to prerequisite articles, and say whether a proof is supplied or omitted.
Before reusing either template, choose a new filename and a label that is not already used anywhere in `docs/`.
Keep existing filenames and labels when editing a page, since other pages and readers may link to them.

The sidebar automatically lists every article under **Articles** and every theorem page under **Theorem pages**, in filename order.
Stubs are included in the same lists.
Adding or removing a file requires no manual menu edit.

### Submit your work and check the result

Commit the files you changed and push your branch; substitute your own filenames and branch name:

```bash
git add docs/articles/my-topic.md
git commit -m "Add an article on my topic"
git push -u origin add-my-topic
```

On GitHub, open a pull request from your branch to `main` in `MatthiasLudewig/coarse-phases`.
Briefly describe what you changed and identify any mathematical questions that still need review.
Opening the pull request starts **Wiki checks**, which builds the website and checks its links, mathematics rendering, and navigation.
Further commits pushed to the same branch update the pull request and run the checks again.

To inspect the result without installing anything:

1. Open the repository's [Actions tab](https://github.com/MatthiasLudewig/coarse-phases/actions) and select the **Build and deploy wiki** run for your pull request and latest commit.
2. Wait for **Wiki checks** to succeed.
   If it fails, open the failed step and read the error messages; duplicate labels and missing reference targets are common causes.
3. In the run's **Artifacts** section, download **wiki-html** while signed in to GitHub.
4. Extract the entire ZIP, then open `index.html` in the extracted folder with your browser.
   Keep the accompanying files and folders together.
5. Follow the sidebar to your page and check the text, equations, links, and any collapsible proofs.
   The **wiki-screenshots** artifact also contains desktop and mobile views.

The preview needs an internet connection to typeset mathematics, and search may be limited when opening HTML files directly from disk.
GitHub's ordinary Markdown preview does not render all of this wiki's mathematics and statement commands; use the generated HTML to check the final appearance.
The downloadable previews expire after seven days, so use a recent successful run.
Commit source files only, not the downloaded HTML or generated build files.
For help finding the download, see [GitHub's artifact instructions](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts).

Passing the checks does not verify mathematical correctness.
Ask the maintainer to review the mathematics and merge the pull request when it is ready.

### Update the homepage and the public website

You do not need to edit `docs/index.md` when you add, rename, or remove an article or theorem page.
The sidebar is regenerated from the two folders at each build.
Its hidden `toctree` blocks in `docs/index.md` supply the navigation; leave these blocks in place even though they produce no lists in the homepage content.
Edit the introduction or the “About this wiki” links in that file only when you want to change the homepage itself.

Once website hosting is enabled, merging into `main` automatically starts another build and publishes the updated website after the checks pass.
In the Actions run for `main`, wait for both **Wiki checks** and **Publish approved main branch** to succeed, then refresh the website in your browser.
There is no separate HTML upload or homepage-generation command for contributors to run.
If the publishing job is skipped, hosting has not been enabled for that run; the maintainer handles this setup.
Before hosting is enabled, the same workflow still produces the downloadable preview.

## Writing the source

### Text, headings, and spacing

Use one `#` heading for the page title, `##` for sections within an article, and `###` for subsections.
Separate paragraphs with a blank line.
Write one sentence per source line, without breaking a sentence into several lines; the browser will wrap it to fit the page.
This also applies inside lists and mathematical statements.

```markdown
## Examples

This is the first sentence of a paragraph.
This is its second sentence.

Use *italics* for a term being defined and **bold** for occasional emphasis.

- First example.
- Second example.
```

The statement blocks below begin and end with a line of backticks.
Copy those lines too, including the blank line between the options and the statement's text.

### Inline mathematics and display equations

You can generally use ordinary LaTeX mathematics between `$...$`, for example `$x\in X$`, `$\frac{a}{b}$`, or `$\alpha+\beta$`.
You do not need a LaTeX document header or a `\begin{document}` command.

Use `$$...$$` for an ordinary display equation.
Put each `$$` delimiter on its own line, directly beside the surrounding prose without intervening blank lines:

```markdown
For every $x\in\R$, we have
$$
x^2\geq 0,
$$
with equality exactly when $x=0$.
```

A display can interrupt a sentence, as in this example.
For aligned calculations, use `\begin{aligned}...\end{aligned}` inside the dollar delimiters:

```markdown
Expanding the product gives
$$
\begin{aligned}
(a+b)^2 &= (a+b)(a+b) \\
        &= a^2+2ab+b^2.
\end{aligned}
$$
```

### Labels and links between pages

Every target label must be unique across the entire wiki, not just within its file.
A target may be referenced any number of times.
Search the files in `docs/` for your proposed label before introducing it, and change the example labels when copying these snippets.
Use descriptive labels without spaces, such as `article-my-topic`, `def-my-object`, `thm-my-result`, `lem-my-lemma`, and `eq-my-identity`.
Give a page and a statement on that page different labels.

To link to a whole page or a labelled section, put a target immediately before its heading:

```markdown
(article-my-topic-examples)=
## Examples
```

On any other page, write:

```markdown
See the {ref}`examples <article-my-topic-examples>`.
```

For an ordinary link by filename, use a path relative to the file containing the link:

```markdown
See [Coarse space](../articles/coarse-space.md).
```

Prefer stable labels when linking to a particular definition, result, or equation.
Use the reference commands below instead of LaTeX `\ref` or `\eqref`.
Following a reference opens the complete owning page at its target.

### Labelled equations

For a numbered equation that can be referenced, use a `{math}` block with a label instead of `$$...$$`:

````markdown
```{math}
:label: eq-my-square-expansion

(a+b)^2=a^2+2ab+b^2.
```
````

To refer to it from another page, use the same label with `{eq}`:

```markdown
Applying {eq}`eq-my-square-expansion` gives the desired identity.
```

The link displays the equation number automatically.
If you want an unnumbered equation with a descriptive text link, put an ordinary target before the block and omit `:label:` and `:name:`:

````markdown
(eq-my-square-bound)=

```{math}
x^2\geq 0.
```
````

Reference this unnumbered version from another page with `{ref}`:

```markdown
Use the {ref}`nonnegativity of a square <eq-my-square-bound>`.
```

### Definitions

Write definitions directly in their owning articles, with explanations and examples nearby.
Italicize the term being defined.
For example:

````markdown
```{prf:definition} Even integer
:nonumber:
:label: def-example-even-integer

An integer $n\in\Z$ is *even* if $n=2k$ for some $k\in\Z$.
```
````

To refer to this definition from another page:

```markdown
Recall the definition of an {prf:ref}`even integer <def-example-even-integer>`.
```

### Theorems

Use `{prf:theorem}` for a theorem, either inside an article or on a standalone theorem page:

````markdown
```{prf:theorem} Sum of even integers
:nonumber:
:label: thm-example-even-sum

Let $m,n\in\Z$ be even.
Then $m+n$ is even.
```
````

To link to it:

```markdown
Apply the {prf:ref}`sum theorem <thm-example-even-sum>`.
```

Use `{prf:proposition}` or `{prf:corollary}` with the same options when those names fit the result better.
Keep `:nonumber:` on all definitions, theorems, lemmas, and related statements: the wiki uses descriptive names rather than visible statement numbers.
State all hypotheses explicitly.

### Lemmas

A lemma uses the same pattern:

````markdown
```{prf:lemma} Negation preserves evenness
:nonumber:
:label: lem-example-even-negative

If $n\in\Z$ is even, then $-n$ is even.
```
````

Reference it with:

```markdown
By the {prf:ref}`negation lemma <lem-example-even-negative>`, the claim follows.
```

The elementary statements here illustrate the syntax; replace them with the mathematics of your topic.

### Proofs and optional toggles

Put a proof after its statement using `{prf:proof}`:

````markdown
```{prf:proof}
Write $m=2a$ and $n=2b$ with $a,b\in\Z$.
Then $m+n=2(a+b)$, so $m+n$ is even.
```
````

To let readers expand and collapse the proof, wrap it in a `{dropdown}` block:

`````markdown
````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Write $m=2a$ and $n=2b$ with $a,b\in\Z$.
Then $m+n=2(a+b)$, so $m+n$ is even.
```
````
`````

The outer block uses four backticks and the inner proof uses three, so each closing line ends the correct block.
Readers click **Proof** to toggle the argument; it starts closed.
Add `:open:` immediately below `:class-container:` if you want it to start expanded.
The dropdown also works without JavaScript.
Long proofs may instead use ordinary sections and intermediate lemmas.

If a proof is omitted, say so explicitly and cite a publicly available paper for a nontrivial result used without proof.
Do not present an omitted proof as an unknown proof or an established result as a conjecture.

### Shared mathematical commands and conventions

The wiki supplies these LaTeX commands on every page and inside diagrams:

| Commands | Meaning |
| --- | --- |
| `\cA` through `\cZ` | Calligraphic letters, such as $\cA$. |
| `\sA` through `\sZ` | Script letters, such as $\sA$. |
| `\N`, `\Z`, `\Q`, `\R`, `\C` | The standard number systems. |
| `\Hom`, `\End`, `\Aut`, `\id`, `\supp`, `\tr`, `\colim` | Upright mathematical operators with suitable spacing. |
| `\BornCoarse`, `\Set`, `\Cat`, `\Ab`, `\Grp`, `\Vect`, `\Hilb`, `\Top`, `\Sp` | Upright category names. |

Use these shared commands instead of their expanded forms.
Command names are case-sensitive; `\tr` and `\Tr`, for example, are different operators.
Write `\mathop{\colim}_{i\in I}` when an index should appear below a colimit in display style.
The standard `\ker` and `\lim` commands are also available.
The complete list is in the [shared macro definitions](https://github.com/MatthiasLudewig/coarse-phases/blob/main/docs/_ext/wiki_macros.py); ask the maintainer to add a shared command if one is missing.

In this wiki, *coarse space* means *bornological coarse space*.
Write it as `$(X, \cB, \cC)$`, with the bornology first, and distinguish a controlled map from a proper, controlled coarse map.
Write the $E$-fattening of $Y$ as `$Y_E$`, and use `$X_{\langle E\rangle}$` for the coarse structure generated by $E$.

### Diagrams

For a commutative diagram, copy a standalone `{tikz}` block such as this:

````markdown
```{tikz}
:libs: cd
:alt: A commutative square with horizontal maps f and g, and vertical maps u and v.

\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "u"'] & B \arrow[d, "v"] \\
C \arrow[r, "g"'] & D
\end{tikzcd}
```
````

Do not wrap the diagram block in dollar delimiters.
GitHub converts it into an image during the build, so no local LaTeX installation is needed.
Give `:alt:` a short description for readers who cannot see the diagram, and explain its mathematical meaning in the text.

### References and review

Keep explanations self-contained and link to prerequisite definitions in their owning articles.
Do not duplicate definitions across pages or insert other articles as shared fragments.
Definitions, arguments proved on the page, and standard textbook material do not need literature citations.
For a nontrivial result used without proof, link directly to a publicly available paper, such as an arXiv preprint, beside the claim and add it to `docs/bibliography/index.md`.
Check that the cited source supports the exact hypotheses and conclusion.

For an article, stub, or theorem page drafted by an agent, place this warning below the title and retain it until the principal author has reviewed the page:

````markdown
```{warning}
Agent-generated, not reviewed yet
```
````

Before submitting, check the mathematics as well as the rendered page: hypotheses, notation, references, equations, and any proof toggles.
