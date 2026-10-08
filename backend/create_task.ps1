param(
    [string]$ExePath = (Join-Path $PSScriptRoot "daily_wallpaper.exe")
)

$TaskName = "APOD_WallPaper_DailyUpdate"

$action = New-ScheduledTaskAction -Execute $ExePath
$trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Automatically updates the desktop wallpaper with today's NASA Astronomy Picture of the Day." -Force
