const test = require('node:test');
const assert = require('node:assert/strict');
const { normalizePastedText } = require('../src/index.js');

test('normalizes text for the GitLab Package artifact', () => {
  assert.equal(normalizePastedText('Ａ\u00a0B\r\nline  '), 'A B\nline');
});
