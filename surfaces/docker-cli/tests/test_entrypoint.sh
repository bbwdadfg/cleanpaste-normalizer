#!/bin/sh
set -eu

sh -n entrypoint.sh
actual="$(printf 'Ａ\302\240B\r\nline  ' | python3 app.py)"
test "$actual" = "A B\nline"
