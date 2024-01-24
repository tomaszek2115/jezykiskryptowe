@echo off

if "%1"=="" (
    echo Podaj sciezke do pliku.
    goto :end
)

set "sciezkaPliku=%1"

for /f "usebackq tokens=2 delims=:" %%d in (`wmic logicaldisk get deviceid^,volumename ^| find ":"`) do (
    echo Sprawdzanie dysku %%d...
    if exist "%%d\%sciezkaPliku%" (
        echo Plik znaleziony na dysku %%d w lokalizacji: "%%d\%sciezkaPliku%"
        goto :end
    )
)

echo Plik nie zostal znaleziony na zadnym z dostepnych dyskow.

:end
pause