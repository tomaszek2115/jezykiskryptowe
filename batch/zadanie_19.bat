@echo off
setlocal enabledelayedexpansion

set "sourceDirectory=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe"
set "destinationDirectory=C:\Users\zuzia\Desktop\Batch\III\Języki Skryptowe\Archiwum"

for %%i in ("%destinationDirectory%\*.txt") do (
    del "%%i"
)

echo Usunieto wszystkie skopiowane pliki tekstowe z rozszerzeniem .txt.
