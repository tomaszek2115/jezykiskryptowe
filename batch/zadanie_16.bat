REM urządzenie 1:
@echo off
setlocal enabledelayedexpansion

set "nadawca=nadawca.txt"

:input
set /p message="Wpisz wiadomosc (wpisz 'exit' aby zakonczyc): "

if /i "%message%"=="exit" (
    echo Koniec rozmowy.
    goto :eof
)

echo %time% - Nadawca: %message% >> %nadawca%
goto input


REM urządzenie 2:
@echo off
setlocal enabledelayedexpansion

set "odbiorca=odbiorca.txt"

:check
timeout /nobreak /t 1 >nul

set "newMessage="
for /f "tokens=*" %%a in ('more +%line% %odbiorca%') do (
    set "newMessage=%%a"
    set /a "line+=1"
)

if defined newMessage (
    echo %newMessage%
)

goto check
