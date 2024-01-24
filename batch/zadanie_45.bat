@echo off

set /p "n=Podaj n: "

if "%1"=="" (
    echo Podaj nazwe pliku do zapisu.
    goto :end
)

(for /L %%i in (1, 1, %n%) do echo %%i) > "%1"

echo Liczby od 1 do %n% zapisano do pliku %1.

:end
pause