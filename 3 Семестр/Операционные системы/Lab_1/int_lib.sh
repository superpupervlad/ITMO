#!/usr/bin/env bash

exit_codes=("ЗБС" \
  "Что-то очень плохое" \
  "Что-то башем" \
  "Неправльное количество агрументов" \
  "Нет такого файла или директории" \
  "Неправильный формат аргументов" \
  "Деление на н0ль!")

interactive(){
    while true; do
          exec 3>&1
          selection=$(dialog \
              --backtitle "Interactive mode" \
              --title "Menu" \
              --clear \
              --menu "Choose wisely" 0 0 0 \
              "c" "Calc" \
              "s" "Search" \
              "r" "Reverse" \
              "n" "Strlen" \
              "l" "Log" \
              "e" "Exit" \
              "h" "Help" \
              2>&1 1>&3)
          exec 3>&-
          case $selection in
              c) calc_int ;;
              s) search_int ;;
              r) reverse_int ;;
              n) strlen_int ;;
              l) log_int ;;
              e) exit_int ;;
              h) help_int ;;
              *) clear && exit 0;;
          esac
    done
}

handle_exit_codes(){
    case $1 in
        [1-6] ) show_output "${exit_codes[$1]}" "Interactive mode" "ERROR" && exit 1;;
        0 ) true ;;
    esac
}

calc_int(){
    exec 3>&1
    op=$(dialog \
        --clear \
        --backtitle "Calculator" \
        --title "Operations" \
        --menu "Choose operation" 0 0 0 \
        "+" "Summation" \
        "-" "Substraction" \
        "*" "Multiplication" \
        "/" "Division" \
        2>&1 1>&3)
    response=$(dialog \
      --backtitle "Calculator" \
      --title "$op" \
      --form "Enter 2 numbers" \
      0 0 0 \
      "First number " 1 1 "" 1 15 10 0 \
      "Second number " 2 1 "" 2 15 10 0 \
      2>&1 1>&3)
    # read -r a b <<<$(get_input "Enter 2 numbers" "$op" "Calculator" 2>&1 1>&3)
    exec 3>&-
    arr=($response)
    res="$(./calc.sh "$op" "${arr[0]}" "${arr[1]}")"
    if handle_exit_codes $? ; then
        show_output "$res" "Calculator" "Result"
    fi
}

search_int(){
    exec 3>&1
    dir="$(get_input "Input direcory" "Search" "Input" 2>&1 1>&3)"
    pattern="$(get_input "Input pattern" "Search" "Input" 2>&1 1>&3)"
    res="$(./search "$dir" "$pattern")"
    if handle_exit_codes $? ; then
        show_output "$res" "Search" "Found files"
    fi
    exec 3>&-
}

reverse_int(){
    exec 3>&1
    s="$(get_input "Input source" "Reverse" "Input" 2>&1 1>&3)"
    d="$(get_input "Input destination" "Reverse" "Input" 2>&1 1>&3)"
    # show_output "$(reverse "$s" "$d")" "Reverse" "Success"
    ./reverse.sh "$s" "$d"
    handle_exit_codes $?
    exec 3>&-
}

strlen_int(){
    exec 3>&1
    string="$(get_input "Enter string" "Strlen" "Input" 2>&1 1>&3)"
    show_output "${#string}" "Strlen" "Lenght of this string is"
    exec 3>&-
}

log_int(){
    if ! [[ -f "/var/log/anaconda/X.log" ]]; then
        handle_exit_codes 4; fi
    content=$(cat /var/log/anaconda/X.log)
    IFS=$'\n'
    wt=$(mktemp)
    it=$(mktemp)
    ot=$(mktemp)
    for line in $content; do
        if [[ $line == *"(WW)"* ]]; then
            echo -e "${line/(WW)/\\Z1Warning \\Zn}" >> "$wt"
        elif [[ $line == *"(II)"* ]]; then
            echo -e "${line/(II)/\\Z3 Information \\Zn}" >> "$it"
        else
            echo "$line" >> "$ot"
        fi
    done
    dialog --colors --msgbox "$(cat "$wt" "$it")" 50 50
    for i in $wt $it $ot; do
        cat "$i"
        rm "$i"
    done
}

exit_int(){
    exec 3>&1
    code="$(get_input "Enter exit code" "Exit" "Input" 2>&1 1>&3)"
    exec 3>&-
    clear && exit $code
}

help_int(){
    show_output "$(help "Учи матчасть" "HELP" "***")"
}
