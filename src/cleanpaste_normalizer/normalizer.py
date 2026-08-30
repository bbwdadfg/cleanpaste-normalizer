"""Normalize line endings, Unicode, invisible characters, and whitespace."""

from __future__ import annotations

import re
import unicodedata

_ZERO_WIDTH = dict.fromkeys(
    map(
        ord,
        (
            "\u200b",
            "\u200c",
            "\u200d",
            "\u200e",
            "\u200f",
            "\u202a",
            "\u202b",
            "\u202c",
            "\u202d",
            "\u202e",
            "\u2060",
            "\ufeff",
        ),
    ),
    None,
)
_UNICODE_SPACES = str.maketrans(
    {
        "\u00a0": " ",
        "\u1680": " ",
        "\u2000": " ",
        "\u2001": " ",
        "\u2002": " ",
        "\u2003": " ",
        "\u2004": " ",
        "\u2005": " ",
        "\u2006": " ",
        "\u2007": " ",
        "\u2008": " ",
        "\u2009": " ",
        "\u200a": " ",
        "\u202f": " ",
        "\u205f": " ",
        "\u3000": " ",
    }
)


def normalize_pasted_text(text: str) -> str:
    """Return a local-only, deterministic normalization of pasted text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = unicodedata.normalize("NFKC", normalized)
    normalized = normalized.translate(_ZERO_WIDTH).translate(_UNICODE_SPACES)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    return normalized.rstrip(" \t")

