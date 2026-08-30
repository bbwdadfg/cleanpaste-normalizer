const test = require('node:test');
const assert = require('node:assert/strict');
const { normalizePastedText } = require('../src/index.js');

test('normalizes line endings, compatibility characters, invisible characters, and trailing spaces', () => {
  assert.equal(
    normalizePastedText('Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t '),
    'A B\nsecond line\nfinal',
  );
});

test('rejects non-string input', () => {
  assert.throws(() => normalizePastedText(null), TypeError);
});
