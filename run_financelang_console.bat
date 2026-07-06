@"
@echo off
title FinanceLang - Frontend de Consola
cd /d "%~dp0"
echo Iniciando FinanceLang...
python src\menu.py
echo.
echo Programa finalizado.
pause
"@ | Set-Content run_financelang_console.bat -Encoding ASCII