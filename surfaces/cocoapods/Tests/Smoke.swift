import Foundation

let result = normalizePastedText("Ａ\u{00a0}B\u{200b}\r\nsecond line  \rfinal\t ")
precondition(result == "A B\nsecond line\nfinal")
