Import-Module ServerManager 

[string]$date = get-date -f 'yyyy-MM-dd' 
$path=”\\srvbak1\bak\dc1\”
$TargetUNC=$path+$date
$TestTargetUNC= Test-Path -Path $TargetUNC

if (!($TestTargetUNC)){
New-Item -Path $TargetUNC -ItemType directory 
}

$WBadmin_cmd = "wbadmin.exe START BACKUP -backupTarget:
$TargetUNC -systemState -noverify -vssCopy -quiet"
Invoke-Expression $Wbadmin_cmd
BACKUP -backupTarget: $TargetUNC -systemState -noverify -vssCopy -quiet" Invoke-Expression $Wbadmin_cmd
