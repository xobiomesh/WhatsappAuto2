# My Project

## Setup

### Windows
1. Run `setup\setup_windows.bat` to set up the environment variables.
2. Run the script:
   ```powershell
   python src\script.py
   ```

### Linux
1. Source the setup script to set up the environment variables:
   ```bash
   source setup/setup_linux.sh
   ```
2. Run the script:
   ```bash
   python src/script.py
   ```

## Configuration
- Update the paths in `config/config_windows.env` and `config/config_linux.env` to match your local setup if necessary.

MAKE SURE THE CORRECT PYTHON VERSION IS INSTALLED AND THE PATH IS SET IN THE ENVIRONMENT VARIABLES.
MAKE SURE THE DEPENDENCIES ARE INSTALLED.
Dependencies:
- requests
- python-dotenv
- selenium
- webdriver-manager

```
