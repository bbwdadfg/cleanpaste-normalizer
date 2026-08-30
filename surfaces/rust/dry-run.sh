#!/bin/sh
set -eu
CARGO_NET_OFFLINE=true cargo test
