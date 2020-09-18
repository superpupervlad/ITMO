#!/usr/bin/env bash

case $2$3 in
    ''|*[!0-9]*) exit 5;;
esac
if { [[ $1 = "/" ]] || [[ $1 = "div" ]]; } && [[ $3 -eq 0 ]]; then
    exit 6
fi
case "$1" in
    sum | +) echo "$(($2 + $3))" ;;
    sub | -)
        echo "$(($2 - $3))" ;;
    mul | \*) echo "$(($2 * $3))" ;;
    div | /) echo "$(($2 / $3))" ;; # | bc -l;;
    *) exit 5
esac
