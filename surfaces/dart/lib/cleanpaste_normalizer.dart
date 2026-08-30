final RegExp _zeroWidth = RegExp(
  r'[\u200b\u200c\u200d\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2060\ufeff]',
);
final RegExp _unicodeSpaces = RegExp(
  r'[\u00a0\u1680\u2000-\u200a\u202f\u205f\u3000]',
);

String normalizePastedText(String text) {
  var normalized = text.replaceAll('\r\n', '\n').replaceAll('\r', '\n');
  normalized = _nfkcCompatibility(normalized)
      .replaceAll(_zeroWidth, '')
      .replaceAllMapped(_unicodeSpaces, (_) => ' ')
      .replaceAll(RegExp(r'[ \t]+\n'), '\n')
      .replaceFirst(RegExp(r'[ \t]+$'), '');
  return normalized;
}

String _nfkcCompatibility(String text) => String.fromCharCodes(
      text.runes.map((rune) {
        if (rune >= 0xFF01 && rune <= 0xFF5E) return rune - 0xFEE0;
        if (rune == 0x3000) return 0x20;
        return rune;
      }),
    );
