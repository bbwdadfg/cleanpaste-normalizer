local normalizer = dofile("src/cleanpaste_normalizer.lua")

assert(normalizer.normalize_pasted_text("Ａ\194\160B\226\128\139\r\nsecond line  \rfinal\t ") == "A B\nsecond line\nfinal")
