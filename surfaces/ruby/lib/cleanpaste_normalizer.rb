module CleanPasteNormalizer
  ZERO_WIDTH = "\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2060\uFEFF"
  UNICODE_SPACES = "\u00A0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000"

  def self.normalize_pasted_text(text)
    raise TypeError, "text must be a string" unless text.is_a?(String)

    normalized = text.gsub("\r\n", "\n").gsub("\r", "\n")
    normalized = normalized.unicode_normalize(:nfkc)
    normalized = normalized.delete(ZERO_WIDTH).tr(UNICODE_SPACES, " " * UNICODE_SPACES.length)
    normalized = normalized.gsub(/[ \t]+\n/, "\n")
    normalized.sub(/[ \t]+\z/, "")
  end
end
