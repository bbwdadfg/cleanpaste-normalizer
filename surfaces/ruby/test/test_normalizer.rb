require "minitest/autorun"
require "cleanpaste_normalizer"

class CleanPasteNormalizerTest < Minitest::Test
  def test_normalizes_pasted_text
    assert_equal(
      "A B\nsecond line\nfinal",
      CleanPasteNormalizer.normalize_pasted_text("Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ")
    )
  end
end
