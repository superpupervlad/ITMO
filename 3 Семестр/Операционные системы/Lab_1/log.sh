#!/usr/bin/env bash

if ! [[ -f "/var/log/anaconda/X.log" ]]; then exit 4; fi
if ! [[ -r "/var/log/anaconda/X.log" ]]; then exit 7; fi

content=$(cat /var/log/anaconda/X.log)
IFS=$'\n'
YELLOW_NORMAL="\e[1;33m"
BLUE_NORMAL="\e[1;34m"
NC="\033[0;39m" # No Color
wt=$(mktemp)
it=$(mktemp)
if [[ $1 -eq 1 ]]; then
    for line in $content; do
        if [[ $line == *"] (WW)"* ]]; then
            echo -e "${line/(WW)/\\Z3Warning \\Zn}" >> "$wt"
        elif [[ $line == *"] (II)"* ]]; then
            echo -e "${line/(II)/\\Z4Information \\Zn}" >> "$it"
        fi
    done
else
    for line in $content; do
        if [[ $line == *"] (WW)"* ]]; then
            echo -e "${line/(WW)/$YELLOW_NORMAL Warning $NC}" >> "$wt"
        elif [[ $line == *"] (II)"* ]]; then
            echo -e "${line/(II)/$BLUE_NORMAL Information $NC}" >> "$it"
        fi
    done
fi
cat "$wt"; rm "$wt"
cat "$it"; rm "$it"
