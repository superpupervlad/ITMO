#!/usr/bin/env bash

. dialog.sh
. int_lib.sh

exit_codes=("" \
  "Что-то очень плохое\n" \
  "Что-то c башем\n" \
  "Мало аргуметов\n" \
  "Нет такого файла или директории\n" \
  "Неправильный формат аргументов\n" \
  "Деление на н0ль!\n" \
  "Нет доступа\n") #7

all_commands=("calc" \
  "search" \
  "reverse" \
  "strlen" \
  "log" \
  "exit" \
  "help" \
  "interactive")

available_commands=()
for com in "${all_commands[@]}"; do
  if [[ -f "$com".sh ]]; then
    available_commands+=($com)
  fi
done
diacheck=0; int_ok=1
hash dialog 2>/dev/null || diacheck=1
if [[ diacheck -eq 0 && -f "int_lib.sh" ]]; then
  available_commands+=("interactive")
fi
available_commands+=("exit")

correct_command=0
for com in "${available_commands[@]}"; do
  [[ "$1" = "$com" ]] && correct_command=1
done

if [[ correct_command -eq 1 ]]; then
  if [[ "$1" = "interactive" ]]; then
    if [[ diacheck -eq 1 ]]; then
      echo "Интерактивный режим недоступен, dialog не найден"
    else
      interactive "${available_commands[@]}"
    fi
  elif [[ "$1" = "exit" ]]; then
    if [[ $# -lt 2 ]]; then exit 0
    else
      if ! [[ $2 =~ ^-?[0-9]+$ ]]; then
        echo -en "${exit_codes[5]}"
      else
        exit "$2" || exit 0
      fi
    fi
  else
    ./"$1".sh "${@:2}"
    echo -en "${exit_codes[$?]}"
  fi
else
  printf "Неправильно введена команда \nДоступны следующие комманды:\n" ;
  ( IFS=$'\n'; echo "${available_commands[*]}" )
fi
