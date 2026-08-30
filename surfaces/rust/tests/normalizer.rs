use cleanpaste_normalizer::normalize_pasted_text;

#[test]
fn normalizes_pasted_text() {
    assert_eq!(
        normalize_pasted_text("Ａ\u{00a0}B\u{200b}\r\nsecond line  \rfinal\t "),
        "A B\nsecond line\nfinal"
    );
}
