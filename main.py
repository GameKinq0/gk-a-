#!/usr/bin/env python3
"""
GK AI - Advanced AI Assistant
Version: 1.0.0
Features: Web Search, Code Generation, News Tracking, Gaming Intelligence
"""

import os
import sys
import json
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional
import warnings

warnings.filterwarnings('ignore')

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
    import torch
    from dotenv import load_dotenv
except ImportError:
    print("\n❌ Gerekli paketler yüklenmedi. Çalıştır: pip install -r requirements.txt")
    sys.exit(1)

from modules.web_search import WebSearch
from modules.code_generator import CodeGenerator
from modules.news_tracker import NewsTracker
from modules.memory import MemoryManager
from modules.utils import print_banner, colored_print, save_conversation

load_dotenv()

class GKAI:
    """GK AI - Gelişmiş Yapay Zeka Asistanı"""
    
    def __init__(self):
        self.name = "GK AI"
        self.version = "1.0.0"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        colored_print(f"🚀 {self.name} başlatılıyor... [{self.device.upper()}]", "cyan")
        
        # Modelleri yükle
        try:
            colored_print("📦 AI modelleri yükleniyor...", "yellow")
            self.chat_model = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-medium",
                device=0 if self.device == "cuda" else -1
            )
            colored_print("✅ Chat modeli yüklendi", "green")
        except Exception as e:
            colored_print(f"⚠️ Model yüklenirken hata: {e}", "red")
            self.chat_model = None
        
        # Modülleri başlat
        self.web_search = WebSearch()
        self.code_gen = CodeGenerator()
        self.news_tracker = NewsTracker()
        self.memory = MemoryManager()
        self.conversation_history = []
        
        colored_print(f"✅ {self.name} hazır! Komutları görmek için 'help' yazın.", "green")
    
    def process_input(self, user_input: str) -> str:
        """Kullanıcı girdisini işle"""
        user_input = user_input.strip()
        
        # Özel komutlar
        if user_input.startswith('/'):
            return self.handle_command(user_input)
        
        # Web araması
        if user_input.startswith('ara:') or user_input.startswith('search:'):
            query = user_input.split(':', 1)[1].strip()
            colored_print(f"🔍 Aranıyor: {query}", "blue")
            results = self.web_search.search(query)
            return self.format_search_results(results)
        
        # Kod yazma
        if user_input.startswith('kod:') or user_input.startswith('code:'):
            prompt = user_input.split(':', 1)[1].strip()
            colored_print(f"💻 Kod üretiliyor: {prompt}", "magenta")
            code = self.code_gen.generate(prompt)
            return code
        
        # Haber takibi
        if user_input.startswith('haberler:') or user_input.startswith('news:'):
            topic = user_input.split(':', 1)[1].strip()
            colored_print(f"📰 Haberler aranıyor: {topic}", "cyan")
            news = self.news_tracker.get_news(topic)
            return self.format_news(news)
        
        # Normal sohbet
        return self.chat(user_input)
    
    def chat(self, user_input: str) -> str:
        """Yapay zeka ile sohbet et"""
        if self.chat_model is None:
            return self.fallback_response(user_input)
        
        try:
            input_ids = self.chat_model.tokenizer.encode(user_input + self.chat_model.tokenizer.eos_token, return_tensors='pt')
            
            bot_input_ids = torch.cat([torch.tensor([[self.chat_model.tokenizer.bos_token_id]]), input_ids], dim=-1) if len(self.conversation_history) == 0 else torch.cat(
                [torch.tensor(self.conversation_history), input_ids], dim=-1)
            
            attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
            
            response = self.chat_model.model.generate(
                bot_input_ids,
                attention_mask=attention_mask,
                max_length=1000,
                pad_token_id=self.chat_model.tokenizer.eos_token_id,
                temperature=0.7,
                top_p=0.9
            )
            
            self.conversation_history = response[0]
            
            chat_history_ids = response[0]
            output = self.chat_model.tokenizer.decode(chat_history_ids, skip_special_tokens=True)
            
            # Son cevabı çıkar
            if "Assistant:" in output:
                output = output.split("Assistant:")[-1].strip()
            
            return output
        except Exception as e:
            return self.fallback_response(user_input)
    
    def fallback_response(self, user_input: str) -> str:
        """Yedek cevap sistemi"""
        responses = {
            "selam": "👋 Selam! Ben GK AI, sana nasıl yardımcı olabilirim?",
            "nasılsın": "🤖 Çok iyiyim! Sana nasıl yardımcı olabilirim?",
            "kim": "👋 Ben GK AI, gelişmiş bir yapay zeka asistanı. Kod yazabilirim, internet araştırması yapabilirim, haberları takip edebilirim!",
            "yardım": self.get_help_text(),
        }
        
        for key, response in responses.items():
            if key.lower() in user_input.lower():
                return response
        
        return f"🤔 İlginç! Bununla ilgili daha fazla detay verebilir misin? (ara: konuşmak için, kod: kod yazmak için)"
    
    def handle_command(self, command: str) -> str:
        """Özel komutları işle"""
        cmd = command[1:].lower()
        
        commands = {
            "help": self.get_help_text,
            "h": self.get_help_text,
            "clear": lambda: (self.conversation_history.clear(), "✨ Konuşma geçmişi temizlendi"),
            "c": lambda: (self.conversation_history.clear(), "✨ Konuşma geçmişi temizlendi"),
            "exit": lambda: sys.exit(0),
            "e": lambda: sys.exit(0),
            "memory": lambda: self.memory.show_stats(),
            "about": self.get_about_text,
        }
        
        if cmd in commands:
            result = commands[cmd]()
            if isinstance(result, tuple):
                return result[1]
            return result
        
        return f"❌ Bilinmeyen komut: {cmd}"
    
    def format_search_results(self, results: list) -> str:
        """Arama sonuçlarını formatla"""
        if not results:
            return "❌ Sonuç bulunamadı"
        
        output = "\n🔍 **ARAMA SONUÇLARI**\n" + "="*50 + "\n"
        for i, result in enumerate(results[:5], 1):
            output += f"\n{i}. {result.get('title', 'Başlık yok')}\n"
            output += f"   📄 {result.get('snippet', 'Açıklama yok')[:200]}...\n"
            output += f"   🔗 {result.get('link', 'Link yok')}\n"
        
        return output
    
    def format_news(self, news: list) -> str:
        """Haberleri formatla"""
        if not news:
            return "❌ Haber bulunamadı"
        
        output = "\n📰 **SON HABERler**\n" + "="*50 + "\n"
        for i, article in enumerate(news[:5], 1):
            output += f"\n{i}. {article.get('title', 'Başlık yok')}\n"
            output += f"   📰 {article.get('description', 'Açıklama yok')[:200]}...\n"
            output += f"   🕐 {article.get('published_at', 'Tarih bilinmiyor')}\n"
        
        return output
    
    def get_help_text(self) -> str:
        """Yardım metni"""
        return """
╔════════════════════════════════════════════════════════════╗
║                   GK AI - KOMUTLAR                         ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🔍 ARA: ara: <sorgu>                                     ║
║     Örnek: ara: Python öğrenme rehberi                   ║
║                                                            ║
║  💻 KOD: kod: <açıklama>                                 ║
║     Örnek: kod: Python'da fibonacci fonksiyonu yaz       ║
║                                                            ║
║  📰 HABERLER: haberler: <konu>                           ║
║     Örnek: haberler: yapay zeka                          ║
║                                                            ║
║  🎮 SOHBET: Normal mesaj yazın                           ║
║     Örnek: Selam! Bugün neler yaptın?                   ║
║                                                            ║
║  ⚙️ KOMUTLAR:                                            ║
║     /help, /h      - Yardım göster                       ║
║     /about         - Hakkında                             ║
║     /memory        - Bellek durumu                        ║
║     /clear, /c     - Geçmişi temizle                     ║
║     /exit, /e      - Çıkış                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
    
    def get_about_text(self) -> str:
        """Hakkında bilgisi"""
        return f"""
╔════════════════════════════════════════════════════════════╗
║              {self.name} v{self.version}                       ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🤖 Gelişmiş Yapay Zeka Asistanı                         ║
║  🌐 Web Arama ve İnternet Entegrasyonu                   ║
║  💻 Kod Üretim Yeteneği                                 ║
║  📰 Haberleri Takip Etme                                ║
║  🎮 Gaming Bilgisi                                       ║
║  💾 Konuşma Belleği                                      ║
║                                                            ║
║  Geliştirici: GameKinq0                                 ║
║  Tarih: {datetime.now().strftime('%Y-%m-%d')}                      ║
║  Cihaz: {self.device.upper()}                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
    
    def run(self):
        """Ana döngüyü çalıştır"""
        print_banner()
        
        try:
            while True:
                try:
                    user_input = input("\n👤 Sen: ").strip()
                    
                    if not user_input:
                        continue
                    
                    response = self.process_input(user_input)
                    colored_print(f"🤖 GK AI: {response}", "cyan")
                    
                    # Konuşmayı kaydet
                    save_conversation(user_input, response)
                    
                except KeyboardInterrupt:
                    colored_print("\n👋 Görüşmek üzere!", "yellow")
                    break
                except Exception as e:
                    colored_print(f"❌ Hata: {str(e)}", "red")
        
        except Exception as e:
            colored_print(f"❌ Kritik hata: {str(e)}", "red")
            sys.exit(1)


if __name__ == "__main__":
    try:
        ai = GKAI()
        ai.run()
    except KeyboardInterrupt:
        colored_print("\n👋 Çıkış yapılıyor...", "yellow")
        sys.exit(0)
    except Exception as e:
        colored_print(f"❌ Hata: {str(e)}", "red")
        sys.exit(1)