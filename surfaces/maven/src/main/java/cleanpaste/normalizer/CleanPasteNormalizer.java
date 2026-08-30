package cleanpaste.normalizer;

import java.text.Normalizer;

public final class CleanPasteNormalizer {
    private static final String ZERO_WIDTH = "\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2060\uFEFF";
    private static final String UNICODE_SPACES = "\u00A0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000";

    private CleanPasteNormalizer() {}

    public static String normalize(String text) {
        if (text == null) throw new IllegalArgumentException("text must not be null");
        String normalized = text.replace("\r\n", "\n").replace('\r', '\n');
        normalized = Normalizer.normalize(normalized, Normalizer.Form.NFKC);
        for (int i = 0; i < ZERO_WIDTH.length(); i++) {
            normalized = normalized.replace(String.valueOf(ZERO_WIDTH.charAt(i)), "");
        }
        for (int i = 0; i < UNICODE_SPACES.length(); i++) {
            normalized = normalized.replace(String.valueOf(UNICODE_SPACES.charAt(i)), " ");
        }
        normalized = normalized.replaceAll("[ \\t]+\\n", "\\n");
        return normalized.replaceFirst("[ \\t]+$", "");
    }
}
