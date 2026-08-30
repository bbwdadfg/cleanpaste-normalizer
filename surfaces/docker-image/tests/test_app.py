from app import normalize_pasted_text


assert normalize_pasted_text("Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ") == (
    "A B\nsecond line\nfinal"
)
