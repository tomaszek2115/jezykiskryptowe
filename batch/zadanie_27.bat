@echo off
setlocal enabledelayedexpansion

echo Wybierz opcje sciezki:
echo 1. Lokalna
echo 2. Inna

set /p opcja=Podaj numer opcji: 

if "%opcja%"=="1" (
    set "lokalna_sciezka=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe\Folder"
) else if "%opcja%"=="2" (
    set /p lokalna_sciezka=Podaj innq sciezkę: 
) else (
    echo Niepoprawna opcja. Zakonczono skrypt.
    exit /b 1
)

echo Wybrana sciezka: %lokalna_sciezka%