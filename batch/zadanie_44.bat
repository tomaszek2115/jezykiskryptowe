@echo off

set /p "fileType=Podaj typ pliku (np. .txt): "

set "filesExist=false"

for %%i in (*%fileType%) do (
    set "filesExist=true"
    goto :invoke_script
)

echo Brak plikow o rozszerzeniu %fileType% w katalogu.
goto :end

:invoke_script

call zadanie_42.bat

:end
pause