#!/usr/bin/env bash

if [[ $3 -eq 1 ]]; then
 if [[ $# -lt 2 ]]; then exit 3; fi
fi
if ! [[ -d "$1" ]]; then exit 4; fi
if ! [[ -r "$1" ]]; then exit 7; fi

if [[ $3 -eq 1 ]]; then
  grep -r "$2" "$1"
else
  grep -r --color=always "$2" "$1"
fi
