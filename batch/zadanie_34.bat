@echo off

set /p directory=Podaj adres katalogu docelowego: 
title %directory%

set /p output=Podaj nazwe pliku wyjscia danych: 
dir %directory% > %output%
