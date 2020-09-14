#!/usr/bin/env bash

if ! [[ -f "/var/log/anaconda/X.log" ]]; then exit 4; fi

content=$(cat /var/log/anaconda/X.log)
IFS=$'\n'
YELLOW="\e[1;33m"
BLUE="\e[1;34m"
NC="\033[0;39m" # No Color
wt=$(mktemp)
it=$(mktemp)
for line in $content; do
    if [[ $line == *"] (WW)"* ]]; then
        echo -e "${line/(WW)/$YELLOW Warning $NC}" >> "$wt"
    elif [[ $line == *"] (II)"* ]]; then
        echo -e "${line/(II)/$BLUE Information $NC}" >> "$it"
    fi
done
for i in "$wt" "$it"; do
    cat "$i"
    rm "$i"
done
