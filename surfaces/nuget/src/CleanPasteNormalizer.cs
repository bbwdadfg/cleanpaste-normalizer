using System;
using System.Text;
using System.Text.RegularExpressions;

namespace CleanPasteNormalizer;

public static partial class Normalizer
{
    private static readonly char[] ZeroWidth = "\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2060\uFEFF".ToCharArray();
    private static readonly char[] UnicodeSpaces = "\u00A0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000".ToCharArray();

    public static string Normalize(string text)
    {
        ArgumentNullException.ThrowIfNull(text);
        var normalized = text.Replace("\r\n", "\n").Replace('\r', '\n');
        normalized = normalized.Normalize(NormalizationForm.FormKC);
        normalized = normalized.Replace("\u00A0", " ");
        foreach (var character in UnicodeSpaces) normalized = normalized.Replace(character, ' ');
        foreach (var character in ZeroWidth) normalized = normalized.Replace(character.ToString(), "");
        normalized = TrailingBeforeNewline().Replace(normalized, "\n");
        return TrailingAtEnd().Replace(normalized, "");
    }

    [GeneratedRegex("[ \\t]+\\n")]
    private static partial Regex TrailingBeforeNewline();

    [GeneratedRegex("[ \\t]+$")]
    private static partial Regex TrailingAtEnd();
}
