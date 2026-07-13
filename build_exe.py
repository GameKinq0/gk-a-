#!/usr/bin/env python3
"""
GK AI - EXE Builder
Bu script GK AI'yi Windows EXE dosyasına dönüştürür
"""

import os
import sys
import subprocess
from pathlib import Path

def build_exe():
    """EXE dosyasını oluştur"""
    print("\n🔨 GK AI EXE oluşturuluyor...\n")
    
    # PyInstaller komutu
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name=GK_AI",
        "--icon=icon.ico",  # İsteğe bağlı
        "--add-data=modules:modules",
        "--hidden-import=torch",
        "--hidden-import=transformers",
        "--hidden-import=requests",
        "--hidden-import=bs4",
        "--console",
        "main.py"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ EXE başarıyla oluşturuldu!")
            print(f"📁 Konum: ./dist/GK_AI.exe")
            print("\n🚀 Çalıştırmak için: .\\dist\\GK_AI.exe")
        else:
            print(f"❌ Hata: {result.stderr}")
            return False
    
    except FileNotFoundError:
        print("❌ PyInstaller yüklü değil!")
        print("Kurulum: pip install pyinstaller")
        return False
    except Exception as e:
        print(f"❌ Hata: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    # Gerekli paketleri kontrol et
    try:
        import pyinstaller
        print("✅ PyInstaller bulundu")
    except ImportError:
        print("⚠️ PyInstaller yükleniyor...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # EXE oluştur
    success = build_exe()
    
    if success:
        print("\n✨ Tamamlandı! GK AI artık EXE olarak hazır.")
    else:
        print("\n❌ İşlem başarısız oldu.")
        sys.exit(1)