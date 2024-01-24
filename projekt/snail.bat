@echo off
:menu
cls
echo ########################
echo           MENU
echo ########################
echo 1. Wygeneruj rysunek
echo 2. Generuj raport
echo 3. Zamknij program
echo ########################

set /p choice="wybierz: "

if "%choice%"=="1" goto startup
if "%choice%"=="2" goto generateReport
if "%choice%"=="3" goto close

echo error
timeout /nobreak /t 1 >nul
goto menu

:startup
echo Generuje rysunek
py ".\snail.py"
pause
goto menu

:generateReport


:close
timeout /nobreak /t 1 >nul
exit /b