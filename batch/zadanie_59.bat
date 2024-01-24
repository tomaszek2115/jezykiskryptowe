@echo off
setlocal enabledelayedexpansion
for /f “tokens=* delims=” %%i in (%1) do (
set string=%%i
echo !string:slowo=!
)
endlocal