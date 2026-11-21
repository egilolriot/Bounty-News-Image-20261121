#!/usr/bin/env python3
"""The World in Brief - 21 November 2026.

Entry for the make.fun bounty news-image-20261121 ($100). The program
copies the front-page image beside it to $MAKEFUN_OUTPUT_DIR/entry.png.

The image sums up Saturday 21 November 2026's world news: Russian missiles
land in Poland during Moscow's biggest strike on Ukraine of the month, the
AI sell-off pushes the S&P 500 into correction, COP31 runs past its deadline
deadlocked over fossil fuels, the FBI crime database is hacked, and the UK
and EU sign their biggest post-Brexit deals.

Python 3, standard library only. Deterministic: the same bytes every run.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(outdir, "entry.png")
    with open(src, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)),
          file=sys.stderr)


if __name__ == "__main__":
    main()
