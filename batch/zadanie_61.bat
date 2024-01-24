@echo off
setlocal enabledelayedexpansion
set /p loc1=”Podaj lokalizacje 1: ”
set /p loc2=”Podaj lokalizacje 2: ”
set “string=”
for /f “tokens=* delims=” %%i in (%loc1%) do (
set string=!string!%%i
)
set string=!string!
for /f “tokens=* delims=” %%i in (%loc2%) do (
set string=!string!%%i
)
echo %string%
endlocal