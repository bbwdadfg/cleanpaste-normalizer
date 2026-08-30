import { normalizePastedText } from "../mod.ts";

Deno.test("normalizes pasted text deterministically", () => {
  const actual = normalizePastedText("Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ");
  if (actual !== "A B\nsecond line\nfinal") {
    throw new Error(`unexpected result: ${actual}`);
  }
});

Deno.test("rejects non-string input at runtime", () => {
  let rejected = false;
  try {
    (normalizePastedText as unknown as (value: unknown) => string)(null);
  } catch (error) {
    rejected = error instanceof TypeError;
  }
  if (!rejected) throw new Error("non-string input was accepted");
});
