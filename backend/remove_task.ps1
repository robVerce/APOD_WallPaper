$TaskName = "APOD_WallPaper_DailyUpdate"

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
