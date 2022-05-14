#!/bin/bash

yum groupinstall "Development Tools"

tar -xvf bastet.tar.gz
cd bastet-0.43
make
echo -e "\ninstall:\n\tinstall ./bastet /usr/bin" >> Makefile
make install

cd ~
yum info >> task3.log

repoquery --requires gcc >> task4_1.log
rpm -q --whatrequires libgcc >> task4_2.log

cd ~
mkdir localrepo
createrepo localrepo
#/etc/yum.repos.d/local.repo
#
#[local]
#name=CentOS-$releasever - local packages for $basearch
#baseurl=file:///root/localrepo
#enabled=1
#gpgcheck=0
yum install -y checkinstall

yum repolist > task6.log

#/etc/yum.repos.d/CentOS-Base.repo
#
#+enabled=0
yum repolist

cd
alien -r -g -v fortunes-ru_1.52-2_all.deb
cd fortunes-ru-1.52
#fortunes-ru-1.52-2.spec
#
#-%dir "/"
rpmbuild --target=noarch --buildroot /root/fortunes-ru-1.52 -bb fortunes-ru-1.52-2.spec
yum install fortunes-ru-1.52-2.noarch.rpm

cd
rpm -i nano-2.3.1-10.el7.src.rpm
cd rpmbuild/SPECS/
#nano.spec
#
#+ln -s nano %{buildroot}%{_bindir}/newnano
rpmbuild -bb nano.spec
yum install ../RPMS/x86_64/nano-2.3.1-10.el7.x86_64.rpm 

