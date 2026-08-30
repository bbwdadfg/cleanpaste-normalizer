package cleanpaste.normalizer;

public final class CleanPasteNormalizerSmoke {
    public static void main(String[] args) {
        String result = CleanPasteNormalizer.normalize(
                "Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ");
        if (!"A B\nsecond line\nfinal".equals(result)) {
            throw new AssertionError(result);
        }
    }
}
