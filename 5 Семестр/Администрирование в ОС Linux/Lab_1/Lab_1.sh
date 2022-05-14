#!/bin/bash

compare() {
  hlink_content=$(cat ~/test/links/list_hlink)
  slink_content=$(cat ~/test/links/list_slink 2>/dev/null)
  [[ $slink_content == "$hlink_content" ]] && echo YES
}

cd ~ || exit
#1
mkdir test

ls -la /etc > test/list

ls -ld /etc/*/ | wc -l >> test/list
echo $(( $(ls /etc/.* | wc -l) - 2)) >> test/list

cd test || exit
mkdir links
#5
ln -P list links/list_hlink

ln --symbolic --relative list links/list_slink

echo 7
find . -regex '.*\(links/list_hlink\|list\|links/list_slink\)' -printf "%f %n\n"
# links не файл
wc -l list >> links/list_hlink
echo 9
compare
#10
mv list list1

echo 11
compare

cd ~ || exit
#ШТА
echo 12
ln -P list_link list1

find /etc -name "*.conf" 1>list_conf 2>/dev/null

ls -d /etc/*.d > list_d

#15
cat list_conf list_d > list_conf_d

mkdir test/.sub

cp list_conf_d test/.sub

cp -b list_conf_d test/.sub

echo 19
ls -AR test #tree test
#20
man man 1>man.txt 2>/dev/null

split -b 1024 --additional-suffix=_man man.txt

mkdir man.dir

mv x*_man man.dir

cat man.dir/x*_man > man.dir/man.txt
#25
echo 25
diff man.dir/man.txt man.txt && echo YES

echo "123$(cat man.txt)321" > man.txt

diff man.dir/man.txt man.txt > patch_file

cp patch_file man.dir

patch man.dir/man.txt man.dir/patch_file

echo 30
diff man.txt man.dir/man.txt && echo YES
