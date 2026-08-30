from __future__ import annotations

import re
import sys
import unicodedata

ZERO_WIDTH = "\u200b\u200c\u200d\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2060\ufeff"
UNICODE_SPACES = "\u00a0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000"


def normalize_pasted_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = unicodedata.normalize("NFKC", normalized)
    normalized = normalized.translate(str.maketrans("", "", ZERO_WIDTH))
    normalized = normalized.translate(str.maketrans(UNICODE_SPACES, " " * len(UNICODE_SPACES)))
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    return normalized.rstrip(" \t")


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: app.py [optional UTF-8 filename]")
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) == 2 else sys.stdin.read()
    sys.stdout.write(normalize_pasted_text(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
