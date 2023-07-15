@echo off
color 3
title skids
mode con: cols=60 lines=10

echo skids by splars#1252
echo.
echo.
echo Loading.
ping 127.0.0.1 -n 3 >nul 2>&1
cls

echo skids by splars#1252
echo.
echo.
echo Loading..
ping 127.0.0.1 -n 2 >nul 2>&1
cls

:skids
ipconfig /flushdns
goto skids