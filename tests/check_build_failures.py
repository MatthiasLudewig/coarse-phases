"""Require actionable failures for common mathematical cross-reference mistakes.

Runs on the GitHub runner. All mutations happen in temporary copies of docs/.
"""

import subprocess
import sys

from support import THEOREM, fixture_source


CASES = [
    (
        "duplicate theorem-domain label",
        "\n```{prf:definition} Duplicate\n:label: def-ci-object\n\nDuplicate.\n```\n",
        "duplicate definition label 'def-ci-object'",
    ),
    (
        "missing theorem-domain reference",
        "\nSee {prf:ref}`def-intentionally-missing`.\n",
        "def-intentionally-missing",
    ),
    (
        "missing heading reference",
        "\nSee {ref}`heading-intentionally-missing`.\n",
        "heading-intentionally-missing",
    ),
    (
        "missing equation reference",
        "\nSee {eq}`eq-intentionally-missing`.\n",
        "eq-intentionally-missing",
    ),
    (
        "duplicate heading label",
        "\n(article-ci-object)=\n## Duplicate heading\n",
        "duplicate label article-ci-object",
    ),
]


def main():
    for name, extra, diagnostic in CASES:
        with fixture_source() as source:
            page = source / f"{THEOREM}.md"
            page.write_text(page.read_text(encoding="utf-8") + extra, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "sphinx", "-E", "-b", "html", "-n", "-W",
                 "--keep-going", "-q", str(source), str(source.parent / "html")],
                text=True, capture_output=True, timeout=120,
            )
            output = result.stdout + result.stderr
            if result.returncode == 0 or diagnostic not in output:
                raise AssertionError(f"{name}: expected failed build and {diagnostic!r}\n{output}")
            print(f"PASS: {name} fails with an actionable diagnostic", flush=True)


if __name__ == "__main__":
    main()
