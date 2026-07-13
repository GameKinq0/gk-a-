#!/usr/bin/env python3
"""Memory Management Module for GK AI"""

import json
import psutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List

class MemoryManager:
    """Bellek yönetim modülü"""
    
    def __init__(self):
        self.memory_file = Path("ai_memory.json")
        self.load_memory()
    
    def load_memory(self) -> Dict:
        """Kaydedilmiş belleği yükle"""
        try:
            if self.memory_file.exists():
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    self.memory = json.load(f)
            else:
                self.memory = {
                    "created_at": datetime.now().isoformat(),
                    "conversations": [],
                    "learned_facts": []
                }
        except Exception as e:
            self.memory = {"error": str(e)}
    
    def save_memory(self) -> bool:
        """Belleği kaydet"""
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def show_stats(self) -> str:
        """Bellek istatistiklerini göster"""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            memory_percent = process.memory_percent()
            
            stats = f"""
╔════════════════════════════════════════════╗
║           💾 BELLEK DURUMU                 ║
╠════════════════════════════════════════════╣
║  Toplam Bellek: {memory_info.rss / 1024 / 1024:.2f} MB           ║
║  Bellek Kullanım: {memory_percent:.2f}%                  ║
║  Konuşma Sayısı: {len(self.memory.get('conversations', []))}                   ║
║  Öğrenilen Bilgiler: {len(self.memory.get('learned_facts', []))}              ║
╚════════════════════════════════════════════╝
            """
            return stats
        except Exception as e:
            return f"❌ İstatistik alınamadı: {str(e)}"