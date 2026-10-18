@echo off
rem HTSA as a Windows application: starts the hub when needed and opens the dashboard in its own window.
rem No console stays open: the windowless Python runs space/app.py.
setlocal
set "REPO=%~dp0"
set "PYW=D:\AGI-lab\.venv\Scripts\pythonw.exe"
if not exist "%PYW%" set "PYW=pythonw"
start "" "%PYW%" "%REPO%space\app.py" %*
endlocal
