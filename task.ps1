$Action = New-ScheduledTaskAction -Execute "D:\passcripts\shell.bat"
$Trigger = New-ScheduledTaskTrigger -Daily -DaysInterval 1 -At 3am
$Settings = New-ScheduledTaskSettingsSet
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings
Register-ScheduledTask -TaskName 'My PowerShell Scrip434' -InputObject $Task -User 'cnsec' -Password 'Popo2828!']