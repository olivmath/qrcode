#!/usr/bin/env python3
"""
Script para verificar se todas as dependências estão instaladas corretamente.
"""

import sys

def check_dependencies():
    """Verifica se todas as dependências estão disponíveis."""
    missing_deps = []
    
    # Verificar tkinter
    try:
        import tkinter
        print("✓ tkinter está disponível")
    except ImportError:
        print("✗ tkinter não está disponível")
        missing_deps.append("tkinter")
    
    # Verificar qrcode
    try:
        import qrcode
        print("✓ qrcode está disponível")
    except ImportError:
        print("✗ qrcode não está disponível")
        missing_deps.append("qrcode")
    
    # Verificar pyzbar
    try:
        import pyzbar
        print("✓ pyzbar está disponível")
    except ImportError:
        print("✗ pyzbar não está disponível")
        missing_deps.append("pyzbar")
    
    # Verificar PIL
    try:
        from PIL import Image
        print("✓ PIL (Pillow) está disponível")
    except ImportError:
        print("✗ PIL (Pillow) não está disponível")
        missing_deps.append("pillow")
    
    if missing_deps:
        print("\n❌ Dependências em falta:")
        for dep in missing_deps:
            if dep == "tkinter":
                print(f"  - {dep}: Instale python3-tk (Ubuntu/Debian) ou python-tk (macOS/Homebrew)")
            else:
                print(f"  - {dep}: pip install {dep}")
        return False
    else:
        print("\n✅ Todas as dependências estão disponíveis!")
        return True

if __name__ == "__main__":
    print("Verificando dependências do MyQR GUI...\n")
    print(f"Python {sys.version}\n")
    
    if check_dependencies():
        print("\nVocê pode executar a aplicação com: myqr")
        sys.exit(0)
    else:
        print("\nPor favor, instale as dependências em falta antes de executar a aplicação.")
        sys.exit(1)