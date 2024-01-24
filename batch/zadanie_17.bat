@echo off
setlocal enabledelayedexpansion

set "outputFile=combinedFile.txt"

if exist "%outputFile%" del "%outputFile%"

for %%i in (*.txt) do (
    type "%%i" >> "%outputFile%"
    echo. >> "%outputFile%"
)

echo Polaczono wszystkie pliki tekstowe
