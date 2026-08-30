#!/bin/sh
set -eu
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
javac -d "$tmp_dir" src/main/java/cleanpaste/normalizer/CleanPasteNormalizer.java src/test/java/cleanpaste/normalizer/CleanPasteNormalizerSmoke.java
java -cp "$tmp_dir" cleanpaste.normalizer.CleanPasteNormalizerSmoke
