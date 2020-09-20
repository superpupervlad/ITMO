#!/usr/bin/env bash

if [[ $# -lt 2 ]]; then exit 3; fi
if ! [[ -f "$1" ]]; then exit 4; fi
if ! [[ -r "$1" ]]; then exit 7; fi
dir=$(dirname "$2")
if ! [[ -d "$dir" ]]; then exit 4; fi
if ! [[ -w "$dir" ]]; then exit 7; fi

true > "$2"
content=$(cat "$1")
for (( i=${#content}; i>=0; i-- )); do
    echo -n "${content:$i:1}" >> "$2"
done
