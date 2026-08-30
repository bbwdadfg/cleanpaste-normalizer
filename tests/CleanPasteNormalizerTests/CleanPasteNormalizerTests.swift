import XCTest
@testable import CleanPasteNormalizer

final class CleanPasteNormalizerTests: XCTestCase {
    func testNormalizesPastedText() {
        XCTAssertEqual(
            normalizePastedText("Ａ\u{00a0}B\u{200b}\r\nsecond line  \rfinal\t "),
            "A B\nsecond line\nfinal"
        )
    }
}
