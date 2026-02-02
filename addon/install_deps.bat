@echo off
REM Gemini NVDA Add-on - Dependency Installer (Windows Batch)
REM Double-click this file to install dependencies

echo ============================================================
echo Gemini NVDA Add-on - Dependency Installer
echo ============================================================
echo.

REM Check for uv first
where uv >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Found uv, using it for installation...
    uv pip install -r "%~dp0requirements.txt" --target "%~dp0lib"
) else (
    echo uv not found, using pip...
    python -m pip install -r "%~dp0requirements.txt" --target "%~dp0lib"
)

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo Installation complete! Restart NVDA to use the add-on.
    echo ============================================================
) else (
    echo.
    echo ============================================================
    echo Installation failed! Check errors above.
    echo ============================================================
)

echo.
pause
