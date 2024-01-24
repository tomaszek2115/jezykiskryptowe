@echo off
setlocal enabledelayedexpansion

set "systemDir=%SystemRoot%\System32"
echo Pliki wykonywalne w katalogu systemowym (%systemDir%):
for %%F in ("%systemDir%\*.exe") do (
    echo - %%~nxF
    echo   Lokalizacja: %%~dpF
    echo.
)

set "userDir=%UserProfile%"
echo Pliki wykonywalne w katalogu uzytkownika (%userDir%):
for %%F in ("%userDir%\*.exe") do (
    echo - %%~nxF
    echo   Lokalizacja: %%~dpF
    echo.
)

set "inneKatalogi=C:\InnyKatalog1 C:\InnyKatalog2"
for %%D in (%inneKatalogi%) do (
    echo Pliki wykonywalne w katalogu %%D:
    for %%F in ("%%D\*.exe") do (
        echo - %%~nxF
        echo   Lokalizacja: %%~dpF
        echo.
    )
)

pause