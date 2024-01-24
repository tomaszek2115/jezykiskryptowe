@echo off

set /p "fileType=Podaj typ pliku do usuniecia (np. .tmp): "
del *%fileType% /q

pause
