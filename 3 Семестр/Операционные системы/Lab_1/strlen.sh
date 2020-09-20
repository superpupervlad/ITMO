#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    exit 3
fi

echo "${#1}"
