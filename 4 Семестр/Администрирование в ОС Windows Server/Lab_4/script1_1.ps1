try {
	New-EventLog -LogName ProcessMonitoringLog -Source Test
}
catch {
	Write-Host "Event log with this name already exists"
}
