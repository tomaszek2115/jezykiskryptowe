@echo off
setlocal enabledelayedexpansion

set "katalog=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe"

for %%F in ("%katalog%\*") do (
    for %%G in ("%katalog%\*") do (
        if "%%F" neq "%%G" (
            echo Porownywanie plikow: %%F i %%G
            fc "%%F" "%%G"
            echo. & echo.
        )
    )
)

endlocal