@echo off
echo Sprawdzanie stanu dyskow...
wmic logicaldisk get caption, description, size, freespace
pause