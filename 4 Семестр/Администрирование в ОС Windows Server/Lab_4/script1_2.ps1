try {
Get-Process -IncludeUserName | Select-Object Id, ProcessName, Path, Username, CPU, WS, @{Name="Date"; Expression={Get-Date}} | Export-Csv "C:\abc.csv"
Write-EventLog -LogName "ProcessMonitoringLog" -Source Test -EventId 1 -EntryType SuccessAudit -Message "Process info file was created successfully"
}
catch {
Write-EventLog -LogName "ProcessMonitoringLog" -Source Test -EventId 2 -EntryType FailureAudit -Message "Process info file was not created"
}
