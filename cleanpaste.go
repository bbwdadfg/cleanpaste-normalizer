package cleanpaste

import (
	"regexp"
	"strings"

	"golang.org/x/text/unicode/norm"
)

var zeroWidth = strings.NewReplacer(
	"\u200b", "", "\u200c", "", "\u200d", "", "\u200e", "", "\u200f", "",
	"\u202a", "", "\u202b", "", "\u202c", "", "\u202d", "", "\u202e", "",
	"\u2060", "", "\ufeff", "",
)

var unicodeSpaces = strings.NewReplacer(
	"\u00a0", " ", "\u1680", " ", "\u2000", " ", "\u2001", " ",
	"\u2002", " ", "\u2003", " ", "\u2004", " ", "\u2005", " ",
	"\u2006", " ", "\u2007", " ", "\u2008", " ", "\u2009", " ",
	"\u200a", " ", "\u202f", " ", "\u205f", " ", "\u3000", " ",
)

var spacesBeforeNewline = regexp.MustCompile(`[ \t]+\n`)

// NormalizePastedText returns a local, deterministic normalization.
func NormalizePastedText(text string) string {
	normalized := strings.ReplaceAll(strings.ReplaceAll(text, "\r\n", "\n"), "\r", "\n")
	normalized = norm.NFKC.String(normalized)
	normalized = unicodeSpaces.Replace(zeroWidth.Replace(normalized))
	normalized = spacesBeforeNewline.ReplaceAllString(normalized, "\n")
	return strings.TrimRight(normalized, " \t")
}
