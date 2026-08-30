#!/bin/sh
set -eu
sh tests/test_entrypoint.sh
python3 -m py_compile app.py
