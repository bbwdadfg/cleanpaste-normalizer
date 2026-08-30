#!/bin/sh
set -eu
python3 -m py_compile app.py
python3 tests/test_app.py
