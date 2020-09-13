#!/bin/bash

calc(){
    case $2$3 in
        ''|*[!0-9]*) echo "Упс, ты видимо не знаешь, что такое 2 числа"
                     return;; #bad
    esac
    if { [[ $1 = "/" ]] || [[ $1 = "div" ]]; } && [[ $3 -eq 0 ]]; then
        echo "Я тебя сейчас на ноль поделю"
    else
        case "$1" in
        sum | +) echo "$2 + $3 = $(($2 + $3))" ;;
        sub | -) echo "$2 - $3 = $(($2 - $3))" ;;
        mul | \*) echo "$2 * $3 = $(($2 * $3))" ;;
        div | /) echo "$2 / $3 = $(($2 / $3))" ;; # | bc -l;;
        *) echo "Хватит портить прогу, нормально введи математические операции"
        esac
    fi
}

search(){
    # If directory -> recursion
    # If file and regex ok -> echo

    for file in "$1"/*; do
      # echo "f: $file 1: $1 2: $2"
      if [[ -d "$file" ]]; then
        search "$file" "$2"
      elif [[ -f "$file" ]]; then
        g_value=$(grep "$2" "$file")
        if [[ -n $g_value ]]; then
          echo "$file: $g_value"
        fi
      fi
    done
}

reverse(){
    if [[ -f "$1" ]]; then
      true > "$2"
      content=$(cat "$1")
      for (( i=${#content}; i>=0; i-- )); do
          # echo without \n i letter
          echo -n "${content:$i:1}" >> $2
      done
      echo "Done!"
    else
      echo "Нет такого файла :("
    fi
}

log(){
    content=$(cat /var/log/anaconda/X.log)
    IFS=$'\n'
    YELLOW="\e[1;33m"
    BLUE="\e[1;34m"
    NC="\033[0;39m" # No Color
    wt=$(mktemp)
    it=$(mktemp)
    for line in $content; do
        if [[ $line == *"] (WW)"* ]]; then
            echo -e "${line/(WW)/$YELLOW Warning $NC}" >> $wt
        elif [[ $line == *"] (II)"* ]]; then
            echo -e "${line/(II)/$BLUE Information $NC}" >> $it
        fi
    done
    for i in $wt $it; do
        cat $i
        rm $i
    done
}

interactive(){
    if [[ pcheck -eq 1 ]]; then
      show_output "$(cat "$tmp")" "Found errors" "Missing programs"
    fi
    DIALOG_CANCEL=1
    DIALOG_ESC=255
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
          case $? in # exit status of dialog
              $DIALOG_CANCEL)
                  echo "Something went wrong :("
                  exit ;;
              $DIALOG_ESC)
                  echo "Goodbye"
                  exit ;;
          esac
          case $selection in
              c) calc_int ;;
              s) search_int ;;
              r) reverse_int ;;
              n) strlen_int ;;
              l) log_int ;;
              e) exit_int ;;
              h) help_int ;;
              *) clear && exit ;;
          esac
    done
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
    values=$(dialog \
      --backtitle "Calculator" \
      --title "$op" \
      --form "Enter 2 numbers \n(Default is zero)" \
      0 0 0 \
      "First number " 1 1 "" 1 15 10 0 \
      "Second number " 2 1 "" 2 15 10 0 \
      2>&1 1>&3)
    a=$(echo "$values" | head -1)
    b=$(echo "$values" | tail -1)
    a=${a:-0}
    b=${b:-0}
    # read -r a b <<<$(get_input "Enter 2 numbers" "$op" "Calculator" 2>&1 1>&3)
    exec 3>&-
    show_output "$(calc "$op" "$a" "$b")" "Calculator" "Result"
}

search_int(){
    exec 3>&1
    dir="$(get_input "Input direcory" "Search" "Input" 2>&1 1>&3)"
    pattern="$(get_input "Input pattern" "Search" "Input" 2>&1 1>&3)"
    show_output "$(search "$dir" $pattern)" "Search" "Found files"
    exec 3>&-
}

reverse_int(){
    exec 3>&1
    s="$(get_input "Input source" "Reverse" "Input" 2>&1 1>&3)"
    d="$(get_input "Input destination" "Reverse" "Input" 2>&1 1>&3)"
    show_output "$(reverse "$s" "$d")" "Reverse" "Success"
    exec 3>&-
}

strlen_int(){
    exec 3>&1
    string="$(get_input "Enter string" "Strlen" "Input" 2>&1 1>&3)"
    show_output "${#string}" "Strlen" "Lenght of this string is"
    exec 3>&-
}

log_int(){
    content=$(cat /var/log/anaconda/X.log)
    IFS=$'\n'
    wt=$(mktemp)
    it=$(mktemp)
    ot=$(mktemp)
    for line in $content; do
        if [[ $line == *"(WW)"* ]]; then
            echo -e "${line/(WW)/\\Z1Warning \\Zn}" >> $wt
        elif [[ $line == *"(II)"* ]]; then
            echo -e "${line/(II)/\\Z3 Information \\Zn}" >> $it
        else
            echo "$line" >> $ot
        fi
    done
    dialog --colors --msgbox "$(cat $wt $it)" 50 50
    for i in $wt $it $ot; do
        cat $i
        rm $i
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

help(){
    printf "Lab_1
Использование: ./sh_script.sh [параметры] [аргументы]
Параметры:
--calc или -c {sum | sub | mul | div}
        sum \$num1 \$num2 - Выводит сумму двух чисел
        sub \$num1 \$num2 - Выводит разность двух чисел
        mul \$num1 \$num2 - Выводит произведение двух чисел
        div \$num1 \$num2 - Выводит частное двух чисел
--search или -s ДИРЕКТОРИЯ ПАТТЕРН
        Выводит рекурсивно все файлы удовлетворяющие паттерну в указанной директории
--reverse или -r ИСТОЧНИК НАЗНАЧЕНИЕ
        Записывает в обратном порядке данные из ИСТОЧНИКа в НАЗНАЧЕНИЕ
--srlen или -n <строка>
        Выводит количество символов в строке
--log или -l
        Выводит отредактированное содержимое /var/log/anaconda/X.log
--exit или -e [код возврата]
        Завершает работу с заданным кодом возврата или 0
--interactive или -i
        Запускает приложение в интерактивном режиме
--help или -h
        Выводит это сообщение
"
}

check_progs(){
tmp=$(mktemp)
for i in "grep" "clear"
do
  hash $i 2>/dev/null || { echo -n "$i" >> $tmp; }
done
if [[ -n $(cat "$tmp") ]]; then
  echo "Не найдены следующие комманды. Программа может работать неправильно."
  cat "$tmp"
  pcheck=1
fi
}

pcheck=0
diacheck=0
hash dialog 2>/dev/null || { diacheck=1; echo "Не установлен dialog, интерактивный режим недоступен."; }
check_progs

case "$1" in
    --calc | -c) [[ $# -eq 4 ]] && calc $2 $3 $4 || echo "Нужно 4 аргумента";;
    --search | -s) if [[ $# -eq 3 ]]; then search "$2" "$3"  else echo "Нужно 3 аргумента"; fi ;;
    --reverse | -r) [[ $# -eq 3 ]] && reverse "$2" "$3"  || echo "Нужно 3 аргумента" ;;
    --strlen | -n) [[ $# -eq 2 ]] && echo "Number of symbols: ${#2}"  || echo "Нужно 2 аргумента" ;;
    --log | -l) [[ $# -eq 1 ]] &&  log  || echo "Нужен 1 аргумент1" ;;
    --exit | -e) [[ -n $1 ]] && exit "$1" || exit 0 ;;
    --help | -h) [[ $# -eq 1 ]] && help ;;
    --interactive | -i) [[ $# -eq 1 ]] && [[ diacheck -eq 0 ]] && interactive && clear ;;
    *) echo "Очень интересно, но ничего не понятно" ; help
esac
