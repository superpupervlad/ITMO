Get-EventLog -LogName "System" -Newest 10 -InstanceId 12

Get-SilWindowsUpdate | Sort-Object -Property InstallDate | Select -First 5

@(Get-EventLog -list | %{Get-EventLog -LogName $_.Log -EntryType @("Error", "Warning") -After (Get-Date).AddDays(-1) -ErrorAction Ignore}).Count
