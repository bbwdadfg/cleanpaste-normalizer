from __future__ import annotations

import io
import unittest
from unittest.mock import patch

from cleanpaste_normalizer import normalize_pasted_text
from cleanpaste_normalizer.cli import main


class PastedTextNormalizerTests(unittest.TestCase):
    def test_normalizes_line_endings_unicode_and_trailing_space(self) -> None:
        source = "Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t "

        self.assertEqual(normalize_pasted_text(source), "A B\nsecond line\nfinal")

    def test_removes_directional_and_joiner_characters(self) -> None:
        source = "ab\u200ccd\u202ee\ufefff"

        self.assertEqual(normalize_pasted_text(source), "abcdef")

    def test_uses_nfkc_for_compatibility_characters(self) -> None:
        self.assertEqual(normalize_pasted_text("item ①"), "item 1")

    def test_cli_reads_stdin_without_network(self) -> None:
        with patch("sys.stdin", io.StringIO("one\r\ntwo  ")), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as output:
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "one\ntwo")


if __name__ == "__main__":
    unittest.main()

