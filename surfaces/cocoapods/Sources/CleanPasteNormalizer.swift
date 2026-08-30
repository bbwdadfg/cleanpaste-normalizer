import Foundation

private let zeroWidth = ["\u{200B}", "\u{200C}", "\u{200D}", "\u{200E}", "\u{200F}", "\u{202A}", "\u{202B}", "\u{202C}", "\u{202D}", "\u{202E}", "\u{2060}", "\u{FEFF}"]
private let unicodeSpaces = ["\u{00A0}", "\u{1680}", "\u{2000}", "\u{2001}", "\u{2002}", "\u{2003}", "\u{2004}", "\u{2005}", "\u{2006}", "\u{2007}", "\u{2008}", "\u{2009}", "\u{200A}", "\u{202F}", "\u{205F}", "\u{3000}"]

public func normalizePastedText(_ text: String) -> String {
    var normalized = text.replacingOccurrences(of: "\r\n", with: "\n")
        .replacingOccurrences(of: "\r", with: "\n")
        .precomposedStringWithCompatibilityMapping
    for character in zeroWidth { normalized = normalized.replacingOccurrences(of: character, with: "") }
    for character in unicodeSpaces { normalized = normalized.replacingOccurrences(of: character, with: " ") }
    return normalized.split(separator: "\n", omittingEmptySubsequences: false)
        .map { $0.trimmingCharacters(in: CharacterSet(charactersIn: " \t")) }
        .joined(separator: "\n")
}
