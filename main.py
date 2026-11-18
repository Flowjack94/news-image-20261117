"""Entry point for the news-image-20261117 submission.

The front page itself is the file entry.png next to this script; this
program only places a copy of it where the grader expects it. It uses
only the Python standard library, touches no network, and writes the
exact same bytes on every run, so the two grading runs agree.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target_dir / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
