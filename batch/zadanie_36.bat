@echo off

if "%1"=="" (
    echo Podaj katalog docelowy.
    goto :end
)

mkdir "%1" 2>nul
copy *.txt "%1"
echo Kopiowanie zakonczone.

:end
pause