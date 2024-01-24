@echo off
setlocal enabledelayedexpansion

echo === Informacje o maszynie ===

for /f "tokens=2*" %%A in ('hostname') do set "nazwaKomputera=%%B"
echo Nazwa komputera: !nazwaKomputera!

set "liczbaWoluminow=0"
for /f "tokens=*" %%A in ('wmic logicaldisk get caption ^| find ":"') do (
    set /a "liczbaWoluminow+=1"
)
echo Liczba woluminow: !liczbaWoluminow!

set "licznik=0"
for /f "tokens=*" %%A in ('wmic nic get MACAddress ^| find ":"') do (
    if "%%A" neq "" (
        set /a "licznik+=1"
        set "karta[!licznik!]=%%A"
    )
)
echo Ilosc kart sieciowych: !licznik!
for /l %%i in (1, 1, !licznik!) do echo Adres fizyczny karty %%i: !karta[%%i]!

for /f "tokens=2*" %%A in ('systeminfo ^| find "Nazwa domeny"') do set "domena=%%B"
echo Adresacja maszyny w domenie: !domena!

pause