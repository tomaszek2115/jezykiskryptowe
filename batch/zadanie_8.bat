@echo off
setlocal enabledelayedexpansion

set "katalog=C:\Users\zuzia\Desktop\Studia\semestr III"

for %%F in ("%katalog%\*") do (
    echo Zawartosc pliku: %%F
    type "%%F"
    echo. & echo.
)

endlocal
