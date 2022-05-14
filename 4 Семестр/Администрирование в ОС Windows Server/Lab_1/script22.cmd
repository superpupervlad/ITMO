echo 1. Auto
echo 2. Manual
echo 3. True manual
set /p answer=Enter answer: 
if %answer%==1 (netsh interface ipv4 set address name="Ethernet" dhcp
		netsh interface ipv4 set dnsserver name="Ethernet" source=dhcp)
if %answer%==2 (netsh interface ipv4 set address name="Ethernet" static 192.168.1.10 255.255.255.0 192.168.1.1
		netsh interface ipv4 set dnsserver name="Ethernet" static 8.8.8.8)
if %answer%==3 (set /p ip=Enter IP: 
		set /p mask=Enter subnet mask: 
		set /p gw=Enter gateway: 
		netsh interface ipv4 set address name="Ethernet" static %ip% %mask% %gw%
		set /p dns=Enter DNS: 
		netsh interface ipv4 set dnsserver name="Ethernet" static %dns%)
if %answer% NEQ 3 (if %answer% NEQ 2 (if %answer% NEQ 1 (echo Enter normal answer!)))
