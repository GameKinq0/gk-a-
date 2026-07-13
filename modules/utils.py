#!/usr/bin/env python3
"""Utility functions for GK AI"""

import json
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def colored_print(text: str, color: str = "white") -> None:
    """Renkli yazı yazdır"""
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE,
    }
    print(f"{colors.get(color, Fore.WHITE)}{text}{Style.RESET_ALL}")

def print_banner():
    """GK AI başlık yazdır"""
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║                                                        ║
    ║          🤖  GK AI v1.0.0  🤖                        ║
    ║                                                        ║
    ║        Gelişmiş Yapay Zeka Asistanı                  ║
    ║                                                        ║
    ║  ✨ Web Arama  💻 Kod Üretimi  📰 Haber Takibi      ║
    ║                                                        ║
    ║  Komutlar için: /help veya /h yazın                  ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """
    colored_print(banner, "cyan")

def save_conversation(user_input: str, response: str) -> None:
    """Konuşmayı dosyaya kaydet"""
    history_file = Path("conversation_history.json")
    
    try:
        if history_file.exists():
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        else:
            history = []
        
        history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "ai": response
        })
        
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        colored_print(f"⚠️ Konuşma kaydedilemedi: {e}", "yellow")