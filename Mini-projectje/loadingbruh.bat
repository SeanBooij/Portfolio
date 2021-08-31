@echo off
color 2
title Geluid
:: Laad scherm
echo Loading
ping localhost -n 2 >nul
cls
echo Loading.
ping localhost -n 2 >nul
cls
echo Loading..
ping localhost -n 2 >nul
cls
echo Loading...
ping localhost -n 2 >nul
cls
echo Loading
ping localhost -n 2 >nul
cls
echo Loading.
ping localhost -n 2 >nul
cls
echo Complete!
ping localhost -n 2 >nul
cls
:: Pratende batch file
echo set speech = Wscript.CreateObject("SAPI.spVoice") >> "temp.vbs"
set text=Choose your option.
echo speech.speak "%text%" >> "temp.vbs"
start temp.vbs
pause
del temp.vbs
:: Keuze scherm
color 4
echo Press 1 for bruh
echo Press 2 for bababoey
type bruh.txt
echo.
echo.
echo.
set /p keuze=
if %keuze% == 1 goto :bruh
if %keuze% == 2 goto :bababoey
:bruh
start https://www.youtube.com/watch?v=2ZIpFytCSVc
pause
exit
:bababoey
start https://youtu.be/8Scm09bwT_s?t=46
pause
exit