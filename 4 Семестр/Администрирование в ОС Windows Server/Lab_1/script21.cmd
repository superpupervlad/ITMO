set /p str=Print 4 letters: 
set "username=UPart2%str%"
set "groupname=GPart2%str%"
net user %username% 123 /add
net localgroup %groupname% /add
net localgroup %groupname% %username% /add
net user %username% /active:yes
