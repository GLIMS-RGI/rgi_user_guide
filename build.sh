#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

usage() {
	cat <<EOF
Usage: ./build.sh [OPTION]

Options:
	--v7.1   Build only v7.1 (runs v7.1/build.sh)
	--v7.0   Build only v7.0 (runs v7.0/build.sh)
	--merge  Merge already-built outputs into _html
	--all    Build v7.0 and v7.1, then merge (default)
EOF
}

build_v7_0() {
	(cd "$SCRIPT_DIR/v7.0" && ./build.sh)
}

build_v7_1() {
	(cd "$SCRIPT_DIR/v7.1" && ./build.sh)
}

merge_outputs() {
	rm -rf "$SCRIPT_DIR/_html"
	cp -R "$SCRIPT_DIR/v7.1/docs/_build/html" "$SCRIPT_DIR/_html"
	cp -R "$SCRIPT_DIR/v7.0/docs/_build/html" "$SCRIPT_DIR/_html/v7.0"
}

mode="--all"

if [ "$#" -gt 1 ]; then
	usage
	exit 1
fi

if [ "$#" -eq 1 ]; then
	mode="$1"
fi

case "$mode" in
	--v7.0)
		build_v7_0
		;;
	--v7.1)
		build_v7_1
		;;
	--merge)
		merge_outputs
		;;
	--all)
		build_v7_0
		build_v7_1
		merge_outputs
		;;
	-h|--help)
		usage
		;;
	*)
		echo "Unknown option: $mode" >&2
		usage
		exit 1
		;;
esac
