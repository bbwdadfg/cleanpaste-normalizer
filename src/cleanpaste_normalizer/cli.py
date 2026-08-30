"""Command-line interface for pasted-text normalization."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from .normalizer import normalize_pasted_text


def main(argv: Sequence[str] | None = None) -> int:
    """Read pasted text from stdin or one UTF-8 file and print normalized text."""
    parser = argparse.ArgumentParser(
        description="Normalize pasted text without network access."
    )
    parser.add_argument("input_file", nargs="?", help="Optional UTF-8 text file.")
    args = parser.parse_args(argv)

    text = Path(args.input_file).read_text(encoding="utf-8") if args.input_file else sys.stdin.read()
    sys.stdout.write(normalize_pasted_text(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

