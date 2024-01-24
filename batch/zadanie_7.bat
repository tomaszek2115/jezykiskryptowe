@echo off
setlocal enabledelayedexpansion

set "katalogZrodlowy=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe"
set "katalogDocelowy=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe\folder"

if not exist "!katalogDocelowy!" mkdir "!katalogDocelowy!"

for %%F in ("%katalogZrodlowy%\*") do (
    set "plik=%%~F"
    set "dataModyfikacji=%%~tF"
    
    if not exist "!plik!\nul" (
        set "rok="
        set "miesiac="
        set "dzien="
        for /f "tokens=1-3 delims=/: " %%A in ("!dataModyfikacji!") do (
            set "rok=%%C"
            set "miesiac=%%B"
            set "dzien=%%A"
        )

        for /f "tokens=1-3 delims=/ " %%A in ('echo %date%') do (
            set "aktualnyRok=%%C"
            set "aktualnyMiesiac=%%B"
            set "aktualnyDzien=%%A"
        )

        if defined rok if defined miesiac if defined dzien if defined aktualnyRok if defined aktualnyMiesiac if defined aktualnyDzien (
            set /a "roznica=!aktualnyRok!*365+!aktualnyMiesiac!*30+!aktualnyDzien!-!rok!*365+!miesiac!*30+!dzien!"

            if !roznica! gtr 120 (
                echo Kopiowanie pliku: !plik!
                copy "!plik!" "!katalogDocelowy!"
            )
        )
    )
)

endlocal