# cleanpaste-normalizer

`cleanpaste-normalizer` is a deterministic, local Python utility for standardizing clipboard and pasted text. It handles common encoding and spacing inconsistencies across operating systems and rich-text editors without altering actual wording.

## What It Does

- Normalizes line endings to standard Unix newlines (`\n`).
- Applies Unicode NFKC normalization.
- Replaces non-breaking spaces (NBSP), zero-width characters, and irregular whitespace.
- Expands or normalizes tabs and strips trailing whitespace.

## Data Privacy and Processing Scope

- Operates purely in-memory with standard library routines.
- Preserves ordinary text, casing, and semantic structure without automated rewriting.
- Does not upload content, contact external endpoints, or log inputs.

## Python API Usage

The public interface consists of a single function: `normalize_pasted_text(text: str)`.

```python
from cleanpaste_normalizer import normalize_pasted_text

raw_text = "First line\r\nSecond line with non-breaking\u00a0space and zero-width\u200bchar.  "
normalized = normalize_pasted_text(raw_text)
print(normalized)
```

## Command-Line Interface

The CLI accepts an optional positional UTF-8 filename or reads directly from standard input:

```bash
# Process a local file directly
cleanpaste-normalizer raw_input.txt

# Process input from stdin
cat raw_input.txt | cleanpaste-normalizer
```

All execution is local and synchronous with zero network traffic.

## Testing

To verify behavior across Unicode test fixtures, run:

```bash
pytest
```

## Related Resources & Metadata

To explore browser-based normalization tools and background guidelines, visit the [CleanPaste text tools page](https://cleanpasteai.com/). Package distribution metadata may link to this project homepage.

## License

Distributed under the MIT License.
