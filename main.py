#!/usr/bin/env python3
"""news-image-20261117: write the day's front-page image to the output dir.

The bundled entry.png sums up Tuesday 17 November 2026's world news as a
newspaper front page: the Kerch Bridge collapse, tankers mined near Hormuz,
Trump in Manila ahead of the Xi-Putin trilateral, the Pentagon's ninth
failed audit, the Vulcan rocket failure, and Europe's Rwanda return hub.

The program uses only the standard library, touches no network, and writes
the same bytes on every run.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    # Confirm the copy landed before reporting success.
    if os.path.getsize(dest) == 0:
        print("error: entry.png copied as empty file", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
