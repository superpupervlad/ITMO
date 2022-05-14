Write-Host "1. Auto"
Write-Host "2. Manual"
$ans = Read-Host "Enter answer"
if ($ans -eq 1){
    Set-NetIPInterface -InterfaceAlias "Ethernet" -Dhcp Enabled
    Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ResetServerAddresses
}
if ($ans -eq 2){
    New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.10 -DefaultGateway 192.168.1.1 -PrefixLength 24 -AddressFamily IPv4
    Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 8.8.8.8
}
