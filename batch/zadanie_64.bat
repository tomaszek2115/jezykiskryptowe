@echo off
setlocal enabledelayedexpansion
set “string=”
echo =============
echo Przed zmiana
echo =============
for /f “tokens=* delims=” %%i in (%1) do (
set string=%%i
echo !string!
)
echo =============
set “string=”
echo Po zmianie:
echo =============
for /f “tokens=* delims=” %%i in (%1) do (
set string=%%i
echo !string:raz=jeden!
)
echo =============
endlocal