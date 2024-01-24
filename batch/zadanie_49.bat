@echo off

set /p "sciezkaKatalogu=Podaj sciezke do katalogu: "

echo Kasowanie plikow tymczasowych...
del /q "%sciezkaKatalogu%\*.tmp"

echo Pliki tymczasowe zostaly usuniete.

:end
pause