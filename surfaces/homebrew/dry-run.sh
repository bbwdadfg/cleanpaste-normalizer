#!/bin/sh
set -eu
ruby -c Formula/cleanpaste-normalizer.rb
ruby test_formula.rb
ruby -c bin/cleanpaste-normalizer
