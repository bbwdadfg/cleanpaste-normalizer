use unicode_normalization::UnicodeNormalization;

const ZERO_WIDTH: [char; 12] = [
    '\u{200b}', '\u{200c}', '\u{200d}', '\u{200e}', '\u{200f}', '\u{202a}',
    '\u{202b}', '\u{202c}', '\u{202d}', '\u{202e}', '\u{2060}', '\u{feff}',
];

const UNICODE_SPACES: [char; 16] = [
    '\u{00a0}', '\u{1680}', '\u{2000}', '\u{2001}', '\u{2002}', '\u{2003}',
    '\u{2004}', '\u{2005}', '\u{2006}', '\u{2007}', '\u{2008}', '\u{2009}',
    '\u{200a}', '\u{202f}', '\u{205f}', '\u{3000}',
];

pub fn normalize_pasted_text(text: &str) -> String {
    let line_endings = text.replace("\r\n", "\n").replace('\r', "\n");
    let compatibility = line_endings.nfkc().collect::<String>();
    let mapped = compatibility
        .chars()
        .filter_map(|character| {
            if ZERO_WIDTH.contains(&character) {
                None
            } else if UNICODE_SPACES.contains(&character) {
                Some(' ')
            } else {
                Some(character)
            }
        })
        .collect::<String>();
    let lines = mapped
        .split('\n')
        .map(|line| line.trim_end_matches([' ', '\t']))
        .collect::<Vec<_>>();
    lines.join("\n").trim_end_matches([' ', '\t']).to_owned()
}
