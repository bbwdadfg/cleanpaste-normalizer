using CleanPasteNormalizer;

var result = Normalizer.Normalize("Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ");
if (result != "A B\nsecond line\nfinal")
{
    throw new Exception($"Unexpected result: {result}");
}
