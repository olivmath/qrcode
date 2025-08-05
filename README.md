# MyQR GUI

A simple and intuitive GUI application for generating and reading QR codes using Python and Tkinter.

[![PyPI version](https://badge.fury.io/py/myqr-gui.svg)](https://badge.fury.io/py/myqr-gui)
[![Python versions](https://img.shields.io/pypi/pyversions/myqr-gui.svg)](https://pypi.org/project/myqr-gui/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Home

![](./assets/home.png)

## Generate

![](./assets/generate.png)
![](./assets/saved.png)

## Read

![](./assets/readded.png)

## Features

- Generate QR codes from user input text
- Read QR codes from PNG, JPG, and JPEG images

## Requirements

- Python 3.9+
- Tkinter (usually built-in with Python, but may need separate installation on some systems)
- qrcode library (for generating QR codes)
- pyzbar library (for reading QR codes)
- PIL library (for image processing)

### Tkinter Installation

Tkinter is usually included with Python, but if you encounter import errors:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**macOS (with Homebrew):**
```bash
brew install python-tk
```

**Windows:**
Tkinter should be included with the standard Python installation from python.org

## Installation

### From PyPI (Recommended)

```bash
pip install myqr-gui
```

After installation, you can run the application from anywhere:

```bash
myqr
```

### From Source

1. Clone the repository:
```bash
git clone https://github.com/olivmath/myqr-gui.git
cd myqr-gui
```

2. Install dependencies:
```bash
pip install -e .
```

3. Run the application:
```bash
python -m myqr.main
```

## Usage

1. Launch the application.
2. Click "Gerar QR Code" to generate a QR code from user input text.
3. Enter the text for the QR code and a filename (without extension).
4. Click "Gerar e Salvar" to save the QR code as a PNG image.
5. Click "Ler QR Code" to read a QR code from an image file.
6. Select the image file containing the QR code.
7. The decoded text will be displayed in a message box. Click "OK" to copy the text to the clipboard.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
