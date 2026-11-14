"""Temporary reader fixtures, never included in published docs or artifacts."""

from contextlib import contextmanager
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ARTICLE = "articles/ci-object"
THEOREM = "theorems/ci-result"
WITHOUT_PROOF = "theorems/ci-statement"
DIAGRAMS = "articles/ci-diagrams"
MACROS = "articles/ci-macros"
ARTICLE_STUB = "articles/ci-stub"
THEOREM_STUB = "theorems/ci-a-stub"
DIAGRAM_ALTS = (
    "Commutative square: A to B by f, A to C by g, B to D by h, C equals D.",
    "A red arrow from the real numbers to the complex numbers.",
    "Second occurrence of the same commutative square.",
)
FIXTURES = {
    ARTICLE_STUB: r"""---
stub: true
---

(article-ci-stub)=
# Fixture article stub $\sH$

This fixture is classified by metadata, independently of its prose.
""",
    THEOREM_STUB: """---
stub: true
---

(theorem-ci-stub)=
# Fixture theorem stub

This fixture belongs in the final sidebar section despite its theorem folder.
""",
    ARTICLE: r"""(article-ci-object)=
# Fixture article

This introduction belongs to the whole article, not just its definition.

```{prf:definition} Fixture object
:nonumber:
:label: def-ci-object

A fixture object is an integer $x$.
```

## Further discussion

The full article also contains this discussion after the definition.
Informally, adding zero changes nothing; see
{prf:ref}`the full result <thm-ci-result>` on its standalone page.
There is also {prf:ref}`a statement without a supplied proof <thm-ci-statement>`.
See the {ref}`article stub <article-ci-stub>` and {ref}`theorem stub <theorem-ci-stub>`.

```{prf:theorem} Short inline result
:nonumber:
:label: thm-ci-inline

For every fixture object, $x=x$.
```

```{prf:proof}
This is equality with itself.
```

```{math}
:label: eq-ci-identity

x+0=x.
```

```{admonition} Technical remark
:class: dropdown

This is a test-only technical remark.
```
""",
    THEOREM: r"""(theorem-ci-result)=
# Fixture result

Return to {ref}`article-ci-object` or its
{prf:ref}`definition <def-ci-object>`.

```{prf:theorem} Addition of zero
:nonumber:
:label: thm-ci-result

For every fixture object $x$, one has $x+0=x$.
```

## Supporting lemma

```{prf:lemma} Zero is an additive identity
:nonumber:
:label: lem-ci-step

The integer zero is an additive identity.
```

## Argument

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Apply {prf:ref}`the identity lemma <lem-ci-step>` to $x$, giving {eq}`eq-ci-identity`.
```
````
""",
    WITHOUT_PROOF: r"""---
stub: false
---

# Fixture statement without proof

```{prf:theorem} Another identity
:nonumber:
:label: thm-ci-statement

For any fixture object $x$, one has $0+x=x$.
```

No proof is supplied on this test-only page.

See the {prf:ref}`definition in its owning article <def-ci-object>`.
""",
    DIAGRAMS: r"""# Fixture diagrams

These diagrams are test fixtures and never enter the published wiki.

```{tikz}
:libs: cd
:alt: Commutative square: A to B by f, A to C by g, B to D by h, C equals D.

\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, equal] & D
\end{tikzcd}
```

```{tikz}
:alt: A red arrow from the real numbers to the complex numbers.

\draw[->,draw=red] (0,0) node[left] {$\mathbb{R}$} -- (10,0) node[right] {$\mathbb{C}$};
```

```{tikz}
:libs: cd
:alt: Second occurrence of the same commutative square.

\begin{tikzcd}
A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, equal] & D
\end{tikzcd}
```
""",
}


# Exercise the requested vocabulary independently of the production definitions.
MACRO_CASES = [
    (prefix + letter, rf"\{font}{{{letter}}}")
    for prefix, font in (("c", "mathcal"), ("s", "mathscr"))
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
] + [(letter, rf"\mathbb{{{letter}}}") for letter in "NZQRC"] + [
    (name, rf"\operatorname{{{name}}}")
    for name in (
        "Mat End Hom Aut Inn id Der ind tr str Tr Str supp ch ker coker spec "
        "colim Var Exp dom ran Loc Az Con CAR Cl Fun Ad ad Tot"
    ).split()
] + [("lim", r"\operatorname*{lim}")] + [
    (name, rf"\mathrm{{{name}}}")
    for name in "BornCoarse Set Cat Ab Grp Vect Hilb Top Sp".split()
]
FIXTURES[MACROS] = (
    "# Fixture macros $\\sH$\n\n"
    "| Command | Macro | Expansion |\n| --- | --- | --- |\n"
    + "\n".join(rf"| `\{name}` | $x\{name} y$ | $x{expansion} y$ |"
                for name, expansion in MACRO_CASES)
    + "\n\nDisplay limits:\n$$\n"
    + r"\mathop{\colim}_{i\in I} V_i = \operatorname*{colim}_{i\in I} V_i"
    + "\n$$\n\n```{tikz}\n:alt: All requested macros rendered by LaTeX.\n\n"
    + "\n".join(
        rf"\node[anchor=west] at ({(index % 4) * 3}, {-(index // 4)}) "
        rf"{{$\{name} = {expansion}$}};"
        for index, (name, expansion) in enumerate(MACRO_CASES)
    )
    + "\n```\n"
)


@contextmanager
def fixture_source():
    with tempfile.TemporaryDirectory(prefix="wiki-fixtures-") as directory:
        source = Path(directory) / "docs"
        shutil.copytree(ROOT / "docs", source, ignore=shutil.ignore_patterns("_build"))
        for name, content in FIXTURES.items():
            path = source / f"{name}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        # Folder globs discover the fixtures without any index or menu edits.
        yield source


def build(source):
    output = source.parent / "html"
    subprocess.run(
        [sys.executable, "-m", "sphinx", "-E", "-b", "html", "-n", "-W",
         "--keep-going", "-q", str(source), str(output)],
        check=True, timeout=120,
    )
    return output
