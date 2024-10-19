@echo off
POWERSHELL.EXE -Command "Add-Type -AssemblyName System.Windows.Forms; [void] [System.Windows.Forms.Messagebox]::Show( 'Hello!', 'Welcome', 'OK', 'Warning' )"
cls 
MODE 100,15
chcp 65001 >nul
title youtube vid
color D
:youtubevid
echo                [38;2;255;182;193m███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ████████╗ ██████╗  ██████╗ ██╗     
echo                [38;2;255;192;203m████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
echo                [38;2;255;182;193m██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║   ██║   ██║██║   ██║██║     
echo                [38;2;255;174;185m██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║   ██║   ██║██║   ██║██║     
echo                [38;2;255;160;175m██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
echo                [38;2;255;240;245m╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
echo.
echo                                     [97m┌────────────────────────────┐
echo                                     │ 1. [92mgithub                  [97m│
echo                                     │                            │
echo                                     │ 2. credits                 │
echo                                     └────────────────────────────┘

for /f "tokens=2 delims==" %%u in ('echo %USERNAME%') do set "username=%%u"

<nul set /p "=┌─── (@%username%) "
echo.
<nul set /p "=└─# "
set /p choice=


if %choice%==1 goto github
if %choice%==2 goto credits


pause
goto youtubevid

:github
start https://github.com/sxwv
pause
goto youtubevid

:credits
cls
color f
cls 
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
echo [95m┌─────────────────────────────────────┐
echo    [97mMade by [92mSxwv
echo    [97mMade For [92mEducational [97mPurposes Only!
echo [95m└─────────────────────────────────────┘
echo [97m
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls 
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
echo [95m┌─────────────────────────────────────┐
echo    [97mMade by [92mSxwv
echo    [97mMade For [92mEducational [97mPurposes Only!
echo [95m└─────────────────────────────────────┘
echo [97m
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
echo [95m┌─────────────────────────────────────┐
echo    [97mMade by [92mSxwv
echo    [97mMade For [92mEducational [97mPurposes Only!
echo [95m└─────────────────────────────────────┘
echo [97m
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cls 
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls 
timeout 1 /NOBREAK >nul
cls
echo Thank you for using my multitool!
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
timeout 1 /NOBREAK >nul
cls
timeout 1 /NOBREAK >nul
goto youtubevid
                                                    