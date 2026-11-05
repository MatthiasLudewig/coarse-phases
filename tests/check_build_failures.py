"""Require actionable failures for common mathematical cross-reference mistakes.

Runs on the GitHub runner. All mutations happen in temporary copies of docs/.
"""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CASES = [
    (
        "duplicate theorem-domain label",
        "\n```{prf:definition} Duplicate\n:label: def-coarse-space\n\nDuplicate.\n```\n",
        "duplicate definition label 'def-coarse-space'",
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
        "\n(ref-coarse-space)=\n## Duplicate heading\n",
        "duplicate label ref-coarse-space",
    ),
]


def main():
    for name, extra, diagnostic in CASES:
        with tempfile.TemporaryDirectory(prefix="wiki-invalid-") as directory:
            root = Path(directory)
            source = root / "docs"
            shutil.copytree(ROOT / "docs", source, ignore=shutil.ignore_patterns("_build"))
            page = source / "geometry" / "coarse-spaces.md"
            page.write_text(page.read_text(encoding="utf-8") + extra, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "sphinx", "-E", "-b", "html", "-n", "-W",
                 "--keep-going", "-q", str(source), str(root / "html")],
                text=True, capture_output=True, timeout=120,
            )
            output = result.stdout + result.stderr
            if result.returncode == 0 or diagnostic not in output:
                raise AssertionError(f"{name}: expected failed build and {diagnostic!r}\n{output}")
            print(f"PASS: {name} fails with an actionable diagnostic", flush=True)


if __name__ == "__main__":
    main()
