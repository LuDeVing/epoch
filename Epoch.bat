@echo off
rem Epoch as a Windows application: starts the hub when needed and opens the dashboard in its own window.
rem Needs a Python 3.12 or newer; everything else is in the standard library. The lab folder (runs, spaces,
rem accounts) is D:\AGI-lab when it exists, else AGI-lab next to this project folder, made on first start.
setlocal
set "REPO=%~dp0"
set "PYW="
if exist "D:\AGI-lab\.venv\Scripts\pythonw.exe" set "PYW=D:\AGI-lab\.venv\Scripts\pythonw.exe"
if not defined PYW if exist "%REPO%..\AGI-lab\.venv\Scripts\pythonw.exe" set "PYW=%REPO%..\AGI-lab\.venv\Scripts\pythonw.exe"
if not defined PYW for %%p in (pyw.exe) do if not "%%~$PATH:p"=="" set "PYW=%%~$PATH:p"
if not defined PYW for %%p in (pythonw.exe) do if not "%%~$PATH:p"=="" set "PYW=%%~$PATH:p"
if not defined PYW (
  echo Epoch needs Python 3.12 or newer. Install it from python.org with "Add to PATH" ticked, then start Epoch again.
  pause
  exit /b 1
)
start "" "%PYW%" "%REPO%spacepp.py" %*
endlocal
