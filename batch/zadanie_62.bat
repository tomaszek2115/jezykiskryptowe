@echo off
setlocal ENABLEDELAYEDEXPANSION
set s=%1
set p=0
:next
set char=!s:~%p%,1!
set /a p=”%p%+1"
if !char!==^” GOTO next
set test=%st%
set “st=%st%%char%”
if !test!==!st! goto eof
goto next
:eof
echo %st%