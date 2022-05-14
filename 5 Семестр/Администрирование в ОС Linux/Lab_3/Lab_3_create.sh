#!/bin/bash

set -exuo

cd /home
# 1
awk -F: '{print "user " $1 " has id " $3}' /etc/passwd > work3.log

chage -l root | head -1 >> work3.log

awk -F: '{printf $1","}' /etc/group >> work3.log

sed -i 's!# SKEL=/etc/skel!SKEL=/etc/skel!g' /etc/default/useradd
echo "Be careful!" > /etc/skel/readme.txt
# 5
useradd -p $(openssl passwd -crypt 12345678) -m u1

groupadd g1

usermod -aG g1 u1

id u1 >> work3.log

usermod -aG g1 vlad # user
# 10
getent group g1 | awk -F: '{print $4}'

apt-get -y install mc 
usermod -s /usr/bin/mc u1

useradd -p $(openssl passwd -crypt 87654321) -m u2

mkdir test13
cp work3.log test13/work3-1.log
cp work3.log test13/work3-2.log

groupadd test13_group
usermod -aG test13_group u1
usermod -aG test13_group u2
chown -R u1:test13_group test13
chmod 640 -R test13
chmod +110 test13

#15
mkdir test14
chmod +t test14

#16
cp $(which nano) test14
chmod u+s test13/work3-*.log
chown u1 test14/nano

#17
mkdir test15
touch test15/secret_file
chmod -r test15/
