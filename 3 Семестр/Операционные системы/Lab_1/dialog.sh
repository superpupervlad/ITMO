#!/usr/bin/env bash

show_output(){
    dialog \
    --clear \
    --backtitle "$2" \
    --title "$3" \
    --msgbox "$1" 0 0
}

get_input(){
    exec 4>&1
    input=$(dialog \
        --backtitle "$2" \
        --title "$3" \
        --inputbox "$1" 0 0 \
        1>&4)
    exec 4>&-
    echo "$input"
}
