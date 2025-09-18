REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python first: https://www.python.org/downloads/
    pause
    exit /b
)

REM Run the Hangman game
python Hangman.py
pause