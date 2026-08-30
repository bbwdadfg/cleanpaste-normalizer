#!/bin/sh
set -eu
ruby -Ilib test/test_normalizer.rb
ruby -c cleanpaste-normalizer.gemspec
