#!/usr/bin/env bash

if [[ $# -lt 3 ]]; then
    exit 3
fi
if ! [[ $2 =~ ^-?[0-9]+$ ]]; then
    exit 5
fi
if ! [[ $3 =~ ^-?[0-9]+$ ]]; then
    exit 5
fi

case "$1" in
    sum | +) echo "$(($2 + $3))" ;;
    sub | -) echo "$(($2 - $3))" ;;
    mul | \*) echo "$(($2 * $3))" ;;
    div | /) [[ "$3" -eq 0 ]] && exit 6 || echo "$(($2 / $3))" ;; # | bc -l;;
    *) printf "Неправильная мат. операция\n"; exit 5 #удалить принт или поменять код выхода
esac
