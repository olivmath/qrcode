# QR Code Generator and Reader

> [!TIP]
> NOW WRITE IN RUST 🦀

A simple GUI application for generating and reading QR codes using Python and Tkinter.

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

- Python 3.x
- Tkinter (built-in with Python)
- qrcode library (for generating QR codes)
- pyzbar library (for reading QR codes)
- PIL library (for image processing)

## Installation

1. Install Python 3.x if not already installed.
2. Install the required libraries using pip:

```
poetry add "qrcode[pil]" pyzbar Pillow
```

3. Run the application using Python:

```
python myqr/main.py
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
