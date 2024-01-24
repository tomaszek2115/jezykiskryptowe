@echo off

if "%1"=="" (
    echo Podaj nazwe pliku wyjsciowego.
    goto :end
)

for /d %%i in (*) do (
    echo %%i>>"%1"
)

echo Wyniki zapisano w pliku: %1.

:end
pause