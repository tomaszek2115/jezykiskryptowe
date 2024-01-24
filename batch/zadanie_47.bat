@echo off

set /p "parametr=Co chcesz zrobic? [utworz/kasuj]: "

if /i "%parametr%"=="utworz" (
    echo Tworzenie pliku test.txt...
    echo Zawartosc pliku a b c d e f hej>"test.txt"
    echo Plik utworzony.
) else if /i "%parametr%"=="kasuj" (
    echo Kasowanie pliku test.txt...
    if exist "test.txt" del "test.txt"
    echo Plik skasowany.
) else (
    echo Nieprawidlowy parametr. Wpisz ponownie polecenie utworz lub kasuj.
)

pause