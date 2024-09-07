@echo off

REM Activate the virtual environment (if you're using one)
REM Uncomment the following line and adjust the path if needed
.venv\Scripts\activate

REM Clean up previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.egg-info" rmdir /s /q "*.egg-info"

REM Install or upgrade build tools
python -m pip install --upgrade pip setuptools wheel build pytest

REM Run tests
python -m pytest

if %errorlevel% neq 0 (
    echo Tests failed. Build process aborted.
    exit /b %errorlevel%
)

echo Build completed successfully!

REM Deactivate the virtual environment (if you activated it)
REM Uncomment the following line if you uncommented the activation
REM deactivate
