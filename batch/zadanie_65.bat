@echo off
setlocal enabledelayedexpansion
for /f “tokens=* delims=” %%i in (%1) do (
set string=%%i
echo !string:raz=jeden! >> %2
)
endlocal