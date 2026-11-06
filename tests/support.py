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
FIXTURES = {
    ARTICLE: r"""(article-ci-object)=
# Fixture article

This introduction belongs to the whole article, not just its definition.

```{prf:definition} Fixture object
:label: def-ci-object

A fixture object is an integer $x$.
```

## Further discussion

The full article also contains this discussion after the definition.
Informally, adding zero changes nothing; see
{prf:ref}`the full result <thm-ci-result>` on its standalone page.
There is also {prf:ref}`a statement without a supplied proof <thm-ci-statement>`.

```{prf:theorem} Short inline result
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
:label: thm-ci-result

For every fixture object $x$, one has $x+0=x$.
```

## Supporting lemma

```{prf:lemma} Zero is an additive identity
:label: lem-ci-step

The integer zero is an additive identity.
```

## Argument

````{dropdown} Proof
:class-container: proof-dropdown

```{prf:proof}
Apply {prf:ref}`lem-ci-step` to $x$, giving {eq}`eq-ci-identity`.
```
````
""",
    WITHOUT_PROOF: r"""# Fixture statement without proof

```{prf:theorem} Another identity
:label: thm-ci-statement

For any fixture object $x$, one has $0+x=x$.
```

No proof is supplied on this test-only page.

See the {prf:ref}`definition in its owning article <def-ci-object>`.
""",
}


@contextmanager
def fixture_source():
    with tempfile.TemporaryDirectory(prefix="wiki-fixtures-") as directory:
        source = Path(directory) / "docs"
        shutil.copytree(ROOT / "docs", source, ignore=shutil.ignore_patterns("_build"))
        for name, content in FIXTURES.items():
            path = source / f"{name}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        with (source / "index.md").open("a", encoding="utf-8") as index:
            index.write("\n```{toctree}\n:caption: Test fixtures\n\n")
            index.write("\n".join(FIXTURES) + "\n```\n")
        yield source


def build(source):
    output = source.parent / "html"
    subprocess.run(
        [sys.executable, "-m", "sphinx", "-E", "-b", "html", "-n", "-W",
         "--keep-going", "-q", str(source), str(output)],
        check=True, timeout=120,
    )
    return output
