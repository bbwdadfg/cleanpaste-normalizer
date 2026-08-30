#!/bin/sh
set -eu
test -f ../rust/src/lib.rs
grep -q '^version = "0.2.0"' ../rust/Cargo.toml
