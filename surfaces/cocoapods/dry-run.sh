#!/bin/sh
set -eu
ruby -c CleanPasteNormalizer.podspec
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
swiftc Sources/CleanPasteNormalizer.swift Tests/Smoke.swift -o "$tmp_dir/smoke"
"$tmp_dir/smoke"
