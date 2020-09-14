#!/usr/bin/env bash

if [[ $# -eq 3 ]]; then exit 3; fi

if [[ -f "$1" ]]; then
  true > "$2"
  content=$(cat "$1")
  for (( i=${#content}; i>=0; i-- )); do
      # echo without \n i letter
      echo -n "${content:$i:1}" >> "$2"
  done
  # echo "Done!"
else
    exit 4
fi
