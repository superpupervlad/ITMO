#!/usr/bin/env bash

# If directory -> recursion
# If file and regex ok -> echo
if ! [[ -d "$1" ]]; then exit 6; fi
if [[ $# -eq 3 ]]; then exit 3; fi

for file in "$1"/*; do
  # echo "f: $file 1: $1 2: $2"
  if [[ -d "$file" ]]; then
    search "$file" "$2"
  elif [[ -f "$file" ]]; then
    g_value=$(grep "$2" "$file")
    if [[ -n $g_value ]]; then
      echo "$file: $g_value"
    fi
  fi
done
