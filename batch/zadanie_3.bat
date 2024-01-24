@echo off
echo Sprawdzanie zawartosci schowka...

for /f "delims=" %%a in ('powershell -command "Get-Clipboard"') do set "clipboard=%%a"

if "%clipboard%"=="" (
    echo Schowek jest pusty.
) else (
    echo Zawartosc schowka: %clipboard%
)

pause
