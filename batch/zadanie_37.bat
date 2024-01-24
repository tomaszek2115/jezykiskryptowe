@echo off

where magick >nul 2>nul
if %errorlevel% neq 0 (
    echo ImageMagick nie jest zainstalowane. 
    echo Zainstaluj a nastepnie dodaj do zmiennej PATH.
    goto :end
)

if not exist "ConvertedImages" mkdir "ConvertedImages"

for %%i in (*.jpg) do (
    magick "%%i" "ConvertedImages\%%~ni.eps"
)

for %%i in (*.png) do (
    magick "%%i" "ConvertedImages\%%~ni.eps"
)

echo Konwersja zakonczona.

:end
pause