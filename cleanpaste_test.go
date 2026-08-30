package cleanpaste

import "testing"

func TestNormalizePastedText(t *testing.T) {
	got := NormalizePastedText("Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ")
	want := "A B\nsecond line\nfinal"
	if got != want {
		t.Fatalf("NormalizePastedText() = %q, want %q", got, want)
	}
}
