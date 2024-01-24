@echo off
setlocal enabledelayedexpansion

if "%1"=="" (
    echo Podaj liczbe jako argument.
    goto :end
)

set "limit=%1"

set "outputFile=output38.txt"
del "!outputFile!" 2>nul
for /L %%i in (0, 1, %limit%) do (
    echo %%i>>"!outputFile!"
)

echo Wyniki zapisano w pliku: %outputFile%.

:end
pause