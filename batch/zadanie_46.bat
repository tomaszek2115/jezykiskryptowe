@echo off

set /p "n=Podaj n: "

if "%1"=="" (
    echo Podaj nazwe pliku do zapisu.
    goto :end
)

set "nazwaPliku=%1"
set "licznik=1"

for /L %%i in (1, 1, %n%) do (
    if !licznik! lss %n% (
        echo !licznik!>>"%nazwaPliku%"
        set /a "licznik+=1"
    )
)

echo Liczby od 1 do %n% zapisano do pliku %nazwaPliku%.

:end
pause