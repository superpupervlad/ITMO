#!/usr/bin/env bash

if [[ $# -lt 1 ]]; then
    exit 3
fi

echo "${#1}"
