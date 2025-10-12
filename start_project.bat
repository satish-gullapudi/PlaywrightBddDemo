@echo off
setlocal

:: --- Configuration ---
set "VENV_DIR_DEFAULT=venv"
set "VENV_DIR_ALT=.venv"
set "REQUIREMENTS_FILE=requirements.txt"
set "MAIN_SCRIPT=main.py"
set "ACTUAL_VENV_DIR="

echo Checking for virtual environment...

:: 1. Check for existing virtual environments (venv OR .venv)
if exist "%VENV_DIR_DEFAULT%" (
    set "ACTUAL_VENV_DIR=%VENV_DIR_DEFAULT%"
    echo Virtual environment "%VENV_DIR_DEFAULT%" found.
) else if exist "%VENV_DIR_ALT%" (
    set "ACTUAL_VENV_DIR=%VENV_DIR_ALT%"
    echo Virtual environment "%VENV_DIR_ALT%" found.
)

:: 1.b. If neither is found, create the default one ('venv')
if not defined ACTUAL_VENV_DIR (
    set "ACTUAL_VENV_DIR=%VENV_DIR_DEFAULT%"
    echo Neither "%VENV_DIR_DEFAULT%" nor "%VENV_DIR_ALT%" found. Creating "%ACTUAL_VENV_DIR%" now...
    python -m venv "%ACTUAL_VENV_DIR%"
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment. Ensure Python is installed and accessible.
        goto :end
    )
    echo Virtual environment created successfully.
)

:: 2. Activate the virtual environment
echo Activating virtual environment in "%ACTUAL_VENV_DIR%"...
call "%ACTUAL_VENV_DIR%\Scripts\activate.bat"

:: The prompt changes to (venv) or (.venv), satisfying requirement #2.

echo.

:: 3. Install dependencies from requirements.txt
if exist "%REQUIREMENTS_FILE%" (
    echo Installing/Updating dependencies from "%REQUIREMENTS_FILE%"...
    "%ACTUAL_VENV_DIR%\Scripts\python.exe" -m pip install -r "%REQUIREMENTS_FILE%"
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies. Check %REQUIREMENTS_FILE%.
        goto :deactivate_and_end
    )
    echo Dependencies installed successfully.
) else (
    echo WARNING: "%REQUIREMENTS_FILE%" not found. Skipping dependency installation.
)

echo.

:: 4. Run the main.py file using streamlit
echo Starting Streamlit application...
:: Using the full path to the executable is the most reliable way in a batch script
"%ACTUAL_VENV_DIR%\Scripts\streamlit.exe" run "%MAIN_SCRIPT%"
echo "%ACTUAL_VENV_DIR%\Scripts\streamlit.exe" run "%MAIN_SCRIPT%"
pause


:: --- Cleanup ---
:deactivate_and_end
echo.
echo Deactivating virtual environment...
call deactivate
:end
echo Script finished.
endlocal
pause