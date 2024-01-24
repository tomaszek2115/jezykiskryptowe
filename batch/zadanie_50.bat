@echo off

if "%1"=="" (
    echo Podaj przelacznik/przelaczniki: "/a" lub "/h".
    goto :end
)

if /i "%1"=="/h" (
    echo Usuniecie wpisow z podmenu Autostart menu Start oraz z rejestru.
    echo.
    echo Uzycie:
    echo   %0 /a   - usun wszystkie wpisy
    echo   %0 /h   - pomoc
    goto :end
)


REM Usuwanie wpisÃ³w
if /i "%1"=="/a" (
    echo Usuwanie wpisow

    for %%F in ("%APPDATA%\Microsoft\Windows\Menu Start\Programs\Autostart\*.*") do (
        if exist "%%F" (
            echo Usuwanie: %%F
            del /q "%%F"
        )
    )

    reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /f
) else (
    echo Nieprawidlowy parametr. Podaj "%0 /h" aby zobaczyc pomoc.
)

:end
pause