#define MyAppName "APOD Wallpaper"
#define MyAppVersion "1.0.0"
#define MyAppExeName "APOD_WallPaper.exe"

[Setup]
AppId={{B6B6B7B2-4C7A-4E51-9B2B-APODWALLPAPER}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={localappdata}\Programs\APOD_WallPaper
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=dist_installer
OutputBaseFilename=APOD_WallPaper_Setup
Compression=lzma2
SolidCompression=yes
SetupIconFile=..\frontend\src\public\favicon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
LicenseFile=..\LICENSE

[Files]
Source: "..\backend\dist\APOD_WallPaper.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\backend\dist\daily_wallpaper.exe"; DestDir: "{app}\tools"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
