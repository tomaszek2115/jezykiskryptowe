@echo off
setlocal enabledelayedexpansion

set "count=0"

for /f %%a in ('tasklist /NH /FO CSV ^| find /c /v ""') do (
    set "count=%%a"
)

echo Liczba procesow w biezacej sesji systemu: %count%