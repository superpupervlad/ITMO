$act = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "C:\processes.ps1"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 3) -RepetitionDuration ([System.TimeSpan]::MaxValue)
$settings = New-ScheduledTaskSettingsSet -DontStopIfGoingOnBatteries -AllowStartIfOnBatteries

Register-ScheduledTask -TaskName "Process monitoring" -Action $act -Trigger $trigger -Settings $settings
