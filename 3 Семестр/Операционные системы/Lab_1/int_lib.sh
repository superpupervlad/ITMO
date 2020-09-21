#!/usr/bin/env bash

cmd=(dialog \
--backtitle "Interactive mode" \
--title "Menu" \
--clear \
--nocancel \
--menu "Добро пожаловать. Снова." 0 0 0)



interactive(){
    int_commands=()
    input=("$@")
    for ((i=1 ; i < $#+1 ; i++)); do
      int_commands+=($i)
      int_commands+=("${input[$i-1]}")
    done
    while true; do
          exec 3>&1
          selection=$("${cmd[@]}" "${int_commands[@]}" 2>&1 1>&3)
          exec 3>&-
          eval ${int_commands[(($selection*2))-1]}_int
    done
}

handle_exit_codes(){
  show_output "${exit_codes[$1]}" "Interactive mode" "ERROR"
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
    exit_code=$?
    if [[ exit_code -eq 0 ]]; then
        show_output "$res" "Calculator" "Result"
    else
      handle_exit_codes $exit_code
    fi
}

interactive_int(){
  show_output "Любители рекурсии идут на ЙУХ" "***" "~~~"
}

search_int(){
    exec 3>&1
    dir="$(get_input "Input direcory" "Search" "Input" 2>&1 1>&3)"
    pattern="$(get_input "Input pattern" "Search" "Input" 2>&1 1>&3)"
    if [[ -z $dir ]] || [[ -z $pattern ]]; then
      handle_exit_codes 3
    else
      res="$(./search.sh "$dir" "$pattern" 1)"
      exit_code=$?
      exec 3>&-
      if [[ exit_code -eq 0 ]]; then
        show_output "$res" "Calculator" "Result"
      else
        handle_exit_codes $exit_code
      fi
    fi
}

reverse_int(){
    exec 3>&1
    s="$(get_input "Input source" "Reverse" "Input" 2>&1 1>&3)"
    d="$(get_input "Input destination" "Reverse" "Input" 2>&1 1>&3)"
    ./reverse.sh "$s" "$d"
    exit_code=$?
    exec 3>&-
    if [[ exit_code -ne 0 ]]; then
      handle_exit_codes $exit_code
    fi

}

strlen_int(){
    exec 3>&1
    string="$(get_input "Enter string" "Strlen" "Input" 2>&1 1>&3)"
    res="$(./strlen.sh "$string")"
    exit_code=$?
    exec 3>&-
    if [[ exit_code -eq 0 ]]; then
      show_output "$res" "Calculator" "Result"
    else
      handle_exit_codes $exit_code
    fi
}

log_int(){
    res=$(./log.sh 1)
    show_output "$res" "Log" "asd"
}

exit_int(){
    exec 3>&1
    code="$(get_input "Enter exit code" "Exit" "Input" 2>&1 1>&3)"
    exec 3>&-
    if [[ -z $code ]]; then clear; exit 0;
    elif ! [[ $code =~ ^-?[0-9]+$ ]]; then
        handle_exit_codes 5
    else
      clear; exit $code
    fi
}

help_int(){
    show_output "$(./help.sh "Учи матчасть" "HELP" "***")"
}
