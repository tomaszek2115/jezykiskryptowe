@echo off
ren %1\*.txt *.txt2
if “%~2”==”” goto end
if %2==c (goto if) else (goto end)
:if
set /p kat=”podaj katalog: ”
set /p dat=”podaj jak stare: ”
if not exist %1\%kat% mkdir %1\%kat%
forfiles /p %1 /m *.txt2 /c “cmd /c copy @path %kat%\@file” /d -%dat%
:end
echo Zakonczono