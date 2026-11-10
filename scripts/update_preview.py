#!/usr/bin/env python3
"""Refresh the fixed local HTML preview from a successful GitHub Actions run."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "MatthiasLudewig/coarse-phases"
DESTINATION = ROOT / ".preview" / "html"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, type=int, help="GitHub Actions run ID")
    args = parser.parse_args()
    if args.run <= 0:
        parser.error("--run must be a positive run ID")
    gh = shutil.which("gh")
    if gh is None:
        parser.error("GitHub CLI (gh) must be installed and authenticated")

    result = subprocess.run(
        [gh, "run", "view", str(args.run), "--repo", REPOSITORY,
         "--json", "status,conclusion,headSha,headBranch,url"],
        check=True, capture_output=True, text=True,
    )
    info = json.loads(result.stdout)
    if info["status"] != "completed" or info["conclusion"] != "success":
        parser.error("the selected run has not completed successfully; preview unchanged")

    # Download and validate first, so network failures leave the old preview usable.
    preview_root = DESTINATION.parent
    preview_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="download-", dir=preview_root) as temporary:
        source = Path(temporary)
        subprocess.run(
            [gh, "run", "download", str(args.run), "--repo", REPOSITORY,
             "--name", "wiki-html", "--dir", str(source)],
            check=True,
        )
        if not (source / "index.html").is_file():
            parser.error("wiki-html has no index.html; preview unchanged")
        (source / ".build-info.json").write_text(
            json.dumps({"run_id": args.run, **info}, indent=2) + "\n"
        )

        # Keep the same directory and filenames: existing browser tabs can refresh.
        shutil.copytree(source, DESTINATION, dirs_exist_ok=True)
        expected = {path.relative_to(source) for path in source.rglob("*")}
        old_paths = sorted(
            DESTINATION.rglob("*"), key=lambda path: len(path.parts), reverse=True
        )
        for path in old_paths:
            if path.relative_to(DESTINATION) not in expected:
                if path.is_dir() and not path.is_symlink():
                    path.rmdir()
                else:
                    path.unlink()

    print(f"Updated {DESTINATION}")
    print(f"Source: {info['headBranch']} at {info['headSha']}")
    print(f"Run: {info['url']}")
    print(f"Open {DESTINATION / 'index.html'} once, then refresh after later updates.")


if __name__ == "__main__":
    main()
