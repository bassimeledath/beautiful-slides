#!/usr/bin/env python3
"""Render a .pptx to per-slide PNGs using headless LibreOffice + pdftoppm.

Usage:
    python scripts/render_preview.py path/to/deck.pptx [--out DIR] [--dpi 100]

Writes ``DIR/slide-01.png``, ``DIR/slide-02.png``, ... next to an intermediate
PDF.  Default output dir is ``<pptx-basename>-preview/`` next to the pptx.
Exits 0 on success, 1 if ``soffice`` or ``pdftoppm`` are missing or convert.
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def require(binary: str) -> str:
    path = shutil.which(binary)
    if not path:
        print(
            f"error: {binary!r} not found on PATH. "
            f"Install LibreOffice (soffice) and poppler (pdftoppm).",
            file=sys.stderr,
        )
        sys.exit(1)
    return path


def render(pptx: Path, out_dir: Path, dpi: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    soffice = require("soffice")
    pdftoppm = require("pdftoppm")

    # 1. pptx -> pdf via LibreOffice headless.
    subprocess.run(
        [
            soffice,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(out_dir),
            str(pptx),
        ],
        check=True,
    )
    pdf = out_dir / (pptx.stem + ".pdf")
    if not pdf.exists():
        print(f"error: expected {pdf} after soffice conversion", file=sys.stderr)
        sys.exit(1)

    # 2. pdf -> per-slide PNGs.
    subprocess.run(
        [
            pdftoppm,
            "-r", str(dpi),
            "-png",
            str(pdf),
            str(out_dir / "slide"),
        ],
        check=True,
    )

    pngs = sorted(out_dir.glob("slide-*.png"))
    print(f"rendered {len(pngs)} slides to {out_dir}")
    for p in pngs:
        print(f"  {p}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--out", default=None, help="output directory (default: <pptx>-preview)")
    ap.add_argument("--dpi", type=int, default=100)
    args = ap.parse_args()

    pptx = Path(args.pptx).resolve()
    if not pptx.exists():
        print(f"error: {pptx} does not exist", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out).resolve() if args.out else pptx.with_name(pptx.stem + "-preview")
    render(pptx, out_dir, args.dpi)


if __name__ == "__main__":
    main()
