# BulkRedactAttachments

This Python script is designed to bulk redact attachments in Kustomer. Before using the script, replace `orgnamehere` with your Kustomer organization's name and `apitoken` with your Kustomer organization's API token.

## Requirements
- Python 3.x
- Homebrew (for macOS users)
- Visual Studio Code (recommended but optional)
- `virtualenv` and `requests` Python packages

## Installation

### 1. Install Python
**MacOS:** MacOS comes with Python 2.7 pre-installed, which is outdated. It's recommended to install Python 3 using Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

### 2. Install a Code Editor
Visual Studio Code is a recommended editor for coding. Download and install it from:
[Visual Studio Code Official Website](https://code.visualstudio.com/)

### 3. Set Up a Virtual Environment
```bash
pip3 install virtualenv
mkdir path/to/your/project
cd path/to/your/project
python3 -m venv myenv
source myenv/bin/activate
```

### 4. Install Required Packages
With your environment activated, install the necessary Python packages:
```bash
pip install requests
```

## Usage

### Running the Script
Place the script (`bulkredact.py`) in your project directory. Run it using:
```bash
python3 bulkredact.py
```
The script will generate an output log for any failed updates or errors encountered. If successful, it prints "All attachments updated successfully."

### Deactivating the Virtual Environment
To deactivate the virtual environment and return to your system's default Python interpreter:
```bash
deactivate
```

## Note
Follow the steps carefully to ensure the script runs correctly on your system. Adjust the paths as needed depending on your setup.
