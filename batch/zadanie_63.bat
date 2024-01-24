@echo off
:menu
cls
echo ========MENU=======
echo === 1. Option 1 ===
echo === 2. Option 2 ===
echo === 3. Option 3 ===
echo === 4. Exit ===
echo ===================
set /p select=”Wybierz 1,2,3,4:”
IF %select%==1 GOTO opt1
IF %select%==2 GOTO opt2
IF %select%==3 goto opt3
IF %select%==4 goto exit
:opt1
echo Wybrales opcje 1
pause
goto menu
:opt2
echo Wybrales opcje 2
pause
goto menu
:opt3
echo Wybrales opcje 3
pause
goto menu
:exit
echo Wybrales wyjscie
pause