@echo off

if "%~5"=="" (
    echo Uzycie: %~nx0 parametr1 parametr2 parametr3 parametr4 parametr5
    exit /b
)

echo Parametry wejsciowe z przesunieciem o 2:

echo %~3
echo %~4
echo %~5

exit /b
