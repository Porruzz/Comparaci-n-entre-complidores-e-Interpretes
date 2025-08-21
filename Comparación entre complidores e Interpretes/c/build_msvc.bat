@echo off
setlocal
if not exist "%~dp0bin" mkdir "%~dp0bin"
cl /O2 /W3 /nologo /Fe:%~dp0bin\fib_rec.exe %~dp0\fib_rec.c
if errorlevel 1 exit /b 1
cl /O2 /W3 /nologo /Fe:%~dp0bin\fib_iter.exe %~dp0\fib_iter.c
if errorlevel 1 exit /b 1
echo Build MSVC OK
