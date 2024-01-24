@echo off
setlocal enabledelayedexpansion

set "sourceDirectory=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe"
set "destinationDirectory=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe\Archiwum"

for %%i in ("%sourceDirectory%\*.txt") do (
    copy "%%i" "%destinationDirectory%"
)

for %%i in ("%destinationDirectory%\*.txt") do (
    attrib +A "%%i"
)

echo Zmieniono atrybuty plikow na archiwalny.
