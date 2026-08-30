const ZERO_WIDTH = /[\u200b\u200c\u200d\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2060\ufeff]/gu;
const UNICODE_SPACES = /[\u00a0\u1680\u2000-\u200a\u202f\u205f\u3000]/gu;

function normalizePastedText(text) {
  if (typeof text !== 'string') throw new TypeError('text must be a string');
  return text
    .replaceAll('\r\n', '\n')
    .replaceAll('\r', '\n')
    .normalize('NFKC')
    .replace(ZERO_WIDTH, '')
    .replace(UNICODE_SPACES, ' ')
    .replace(/[ \t]+\n/gu, '\n')
    .replace(/[ \t]+$/u, '');
}

module.exports = { normalizePastedText };
