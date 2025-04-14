# Google Dorks Toolkit

A cross-platform tool for performing Google dork searches from the command line. Works on Kali Linux, Termux, and Windows Terminal.

## Features

- Pre-loaded with common Google dorks
- Add your own custom dorks
- Cross-platform compatibility
- Simple command line interface
- Direct browser integration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/google-dorks-toolkit.git
cd google-dorks-toolkit
```

2. Install requirements (Python 3.6+ required):
```bash
pip install -r requirements.txt
```

## Usage

Basic commands:
```bash
# List all available dorks
python dorker.py -l

# Search using dork number
python dorker.py -s 3

# Search using custom dork
python dorker.py -c "inurl:admin/login.php"

# Interactive mode (default)
python dorker.py
```

## Adding Custom Dorks

Edit `dorks.txt` and add your dorks (one per line):
```
intitle:"index of" password
filetype:sql "INSERT INTO users"
```

## Platforms Supported

- Kali Linux
- Termux (Android)
- Windows Terminal
- Any system with Python 3.6+

## License

MIT License
