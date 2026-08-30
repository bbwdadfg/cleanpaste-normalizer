#!/bin/sh
set -eu
dart pub get --offline
dart run test/cleanpaste_normalizer_test.dart
