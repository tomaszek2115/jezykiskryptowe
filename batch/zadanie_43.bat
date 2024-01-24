@echo off

if "%1"=="" (
    echo Podaj katalog.
    goto :end
)

del "%1\*.tmp" /q

echo Usunieto pliki o rozszerzeniu tmp.

:end
pause