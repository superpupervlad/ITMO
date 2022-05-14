#!/bin/bash

set -exuo

cd /home
rm -rf work3.log u1 u2 test1{3,4,5}
userdel u1
userdel u2
groupdel g1
groupdel test13_group
rm -f /etc/skel/readme.txt
sed -i 's!SKEL=/etc/skel!# SKEL=/etc/skel!g' /etc/default/useradd
