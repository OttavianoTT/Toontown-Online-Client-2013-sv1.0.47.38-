@echo off
title Toontown Online - Game Client
cd ..

set /P PPYTHON_PATH=<PPYTHON_PATH

%PPYTHON_PATH% -m main
pause
goto :main