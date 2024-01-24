@echo off
setlocal enabledelayedexpansion

set "katalog1=C:\Users\zuzia"
set "katalog2=C:\Users\zuzia"

for %%F in ("%katalog1%\*") do (
    set "plik1=%%~nxF"
    set "plik2=!katalog2!\!plik1!"

    if exist "!plik2!" (
        fc "%%F" "!plik2!" > nul
        if errorlevel 1 (
            echo Różnice w pliku: !plik1!
        )
    ) else (
        echo Brak pliku w drugim katalogu: !plik1!
    )
)

endlocal