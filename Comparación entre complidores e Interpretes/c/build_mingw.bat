@echo off
setlocal
if not exist "%~dp0bin" mkdir "%~dp0bin"
gcc -O2 -Wall -o %~dp0bin\fib_rec.exe %~dp0\fib_rec.c
if errorlevel 1 exit /b 1
gcc -O2 -Wall -o %~dp0bin\fib_iter.exe %~dp0\fib_iter.c
if errorlevel 1 exit /b 1
echo Build MinGW OK
