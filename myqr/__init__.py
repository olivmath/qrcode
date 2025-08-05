"""MyQR GUI - A simple GUI application for generating and reading QR codes."""

__version__ = "0.1.0"
__author__ = "Lucas Oliveira"
__email__ = "olivmath@protonmail.com"
__description__ = "A simple GUI application for generating and reading QR codes using Python and Tkinter"

from .main import QRCodeApp, main

__all__ = ["QRCodeApp", "main"]