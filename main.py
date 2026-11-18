#!/usr/bin/env python3
"""news-image-20261117 entry point.

The front page itself is baked into this repository as entry.png; this
program only copies that file to the output directory the harness asks
for. It touches no network, and its output is byte-identical on every
run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # The harness sets MAKEFUN_OUTPUT_DIR; without it we fall back to the
    # conventional /output directory. The copy is a plain file copy, so the
    # bytes in the destination match entry.png exactly.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
