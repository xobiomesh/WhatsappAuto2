@echo off
setlocal
set ENV_FILE=config\config_windows.env
for /f "tokens=1,2 delims==" %%A in (%ENV_FILE%) do (
    set %%A=%%B
)
endlocal
