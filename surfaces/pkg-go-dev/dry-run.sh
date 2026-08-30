#!/bin/sh
set -eu
test -f ../go/cleanpaste.go
grep -q 'module github.com/bbwdadfg/cleanpaste-normalizer' ../go/go.mod
