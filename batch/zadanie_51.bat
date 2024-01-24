@echo off
set /p number=Podaj liczbe: 
set /p operator=Podaj operator (+,-,*,/): 
set /p secondNumber=Podaj druga liczbe: 

if "%operator%"=="+" (
    set /a result=%number%+%secondNumber%
) else if "%operator%"=="-" (
    set /a result=%number%-%secondNumber%
) else if "%operator%"=="*" (
    set /a result=%number%*%secondNumber%
) else if "%operator%"=="/" (
    set /a result=%number%/%secondNumber%
)

echo Wynik: %result%
