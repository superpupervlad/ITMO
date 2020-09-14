#!/usr/bin/env bash

. dialog.sh
. int_lib.sh

exit_codes=("ЗБС" \
  "Что-то очень плохое" \
  "Что-то башем" \
  "Неправльное количество агрументов" \
  "Нет такого файла или директории" \
  "Неправильный формат аргументов" \
  "Деление на н0ль!")

# run(){
#   res=$(./"$1".sh "$2" "$3" "$4")
#   case $? in
#     [1-7] ) echo "${exit_codes[$?]}" && exit $? ;;
#     0 ) true ;;
#   esac
#   echo "$res"
# }

help(){
    printf "Lab_1
Использование: ./sh_script.sh [параметры] [аргументы]
Параметры:
calc или -c {sum | sub | mul | div}
      sum \$num1 \$num2 - Выводит сумму двух чисел
      sub \$num1 \$num2 - Выводит разность двух чисел
      mul \$num1 \$num2 - Выводит произведение двух чисел
      div \$num1 \$num2 - Выводит частное двух чисел
search или -s ДИРЕКТОРИЯ ПАТТЕРН
      Выводит рекурсивно все файлы удовлетворяющие паттерну в указанной директории
reverse или -r ИСТОЧНИК НАЗНАЧЕНИЕ
      Записывает в обратном порядке данные из ИСТОЧНИКа в НАЗНАЧЕНИЕ
srlen или -n <строка>
      Выводит количество символов в строке
log или -l
      Выводит отредактированное содержимое /var/log/anaconda/X.log
exit или -e [код возврата]
      Завершает работу с заданным кодом возврата или 0
interactive или -i
      Запускает приложение в интерактивном режиме
help или -h
      Выводит это сообщение
"
}

# check_progs(){
# tmp=$(mktemp)
# for i in "grep" "clear"
# do
#   hash $i 2>/dev/null || { echo -n "$i" >> "$tmp"; }
# done
# if [[ -n $(cat "$tmp") ]]; then
#   echo "Не найдены следующие комманды. Программа может работать неправильно."
#   cat "$tmp"
#   pcheck=1
# fi
# }

diacheck=0
hash dialog 2>/dev/null || { diacheck=1; echo "Не установлен dialog, интерактивный режим недоступен."; }
echo "$#"

case "$1" in
    "calc" | -c) res="$(./calc.sh "$2" "$3" "$4")" ;;
    "search" | -s) res="$(./search.sh "$2" "$3")" ;;
    "reverse" | -r) res="$(./reverse.sh "$2" "$3")" ;;
    "strlen" | -n) echo "Number of symbols: ${#2}" ;;
    "log" | -l) ./log.sh ;;
    "exit" | -e) [[ -n $1 ]] && exit "$1" || exit 0 ;;
    "help" | -h) help ;;
    "interactive" | -i) [[ diacheck -ne 1 ]] && interactive && clear ;;
    *) echo "Очень интересно, но ничего не понятно" ; help
esac

# if [[ $? -ge 1 && $? -le 7 ]]; then
#   echo "${exit_codes[$?]}" && exit $?
# fi
case $? in
  [1-6] ) echo "${exit_codes[$?]}" && exit $? ;;
  0 ) true ;;
esac
echo "$res"
