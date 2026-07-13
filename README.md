# 🤖 GK AI - Gelişmiş Yapay Zeka Asistanı

**Sürüm:** 1.0.0
**Geliştirici:** GameKinq0
**Lisans:** MIT

---

## 📋 Özellikler

✨ **GK AI**, aşağıdaki yeteneklere sahip gelişmiş bir yapay zeka asistanıdır:

### 🧠 Temel Yetenekler
- 💬 **Doğal Dil İşleme** - Türkçe/İngilizce sohbet
- 🌐 **Web Arama** - DuckDuckGo ve Wikipedia entegrasyonu
- 💻 **Kod Üretimi** - Çeşitli algoritma ve framework'ler
- 📰 **Haber Takibi** - Son haberler ve trendingler
- 🎮 **Gaming Bilgisi** - Oyun ve e-sports haberleri
- 💾 **Konuşma Belleği** - Geçmiş konuşmaları hatırlama

### 🚀 Teknik Özellikler
- **GPU Desteği** - CUDA ile hızlı işlem
- **Çoklu Model** - DialoGPT, Transformers
- **Async İşlem** - Eşzamanlı sorgu işleme
- **EXE Desteği** - Tek tıkla çalıştırma
- **REST API** - Web entegrasyonu

---

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- pip (Python paket yöneticisi)
- 4GB+ RAM
- İnternet bağlantısı

### Adım 1: Repository'i Clone Et
```bash
git clone https://github.com/GameKinq0/gk-ai.git
cd gk-ai
```

### Adım 2: Sanal Ortam Oluştur
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Adım 3: Paketleri Yükle
```bash
pip install -r requirements.txt
```

### Adım 4: Çalıştır
```bash
python main.py
```

---

## 🎯 Kullanım

### Temel Komutlar

#### 1. **Sohbet**
```
👤 Sen: Selam! Nasılsın?
🤖 GK AI: 👋 Selam! Ben çok iyiyim, sana nasıl yardımcı olabilirim?
```

#### 2. **Web Araması**
```
👤 Sen: ara: Python nasıl öğrenirim
🤖 GK AI: 🔍 Aranıyor...
[Arama sonuçları]
```

#### 3. **Kod Üretimi**
```
👤 Sen: kod: Fibonacci dizisi
🤖 GK AI: 💻 Kod üretiliyor...
[Python kodu]
```

#### 4. **Haber Takibi**
```
👤 Sen: haberler: yapay zeka
🤖 GK AI: 📰 Haberler aranıyor...
[Son haberler]
```

### Özel Komutlar

| Komut | Açıklama |
|-------|----------|
| `/help` veya `/h` | Yardım menüsü |
| `/about` | GK AI Hakkında |
| `/memory` | Bellek istatistikleri |
| `/clear` veya `/c` | Konuşma geçmişini temizle |
| `/exit` veya `/e` | Çıkış |

---

## 🔧 EXE'ye Dönüştürme (Windows)

### Adım 1: PyInstaller Yükle
```bash
pip install pyinstaller
```

### Adım 2: EXE Oluştur
```bash
python build_exe.py
```

### Adım 3: Çalıştır
```bash
.\dist\GK_AI.exe
```

**Sonuç:** Artık GK AI'yi EXE dosyası olarak dağıtabilirsin!

---

## 📚 Modül Yapısı

```
gk-ai/
├── main.py                 # Ana uygulama
├── build_exe.py           # EXE builder
├── requirements.txt       # Paket bağımlılıkları
├── modules/
│   ├── __init__.py
│   ├── utils.py          # Yardımcı fonksiyonlar
│   ├── web_search.py     # Web arama modülü
│   ├── code_generator.py # Kod üretim modülü
│   ├── news_tracker.py   # Haber takibi
│   └── memory.py         # Bellek yönetimi
├── README.md             # Dokümantasyon
└── LICENSE               # MIT Lisansı
```

---

## 🌐 Web API Entegrasyonu

GK AI'yi REST API olarak çalıştırmak için:

```bash
python api_server.py
```

Endpointler:
- `POST /api/chat` - Sohbet
- `GET /api/search?q=query` - Web araması
- `POST /api/code` - Kod üretimi
- `GET /api/news?topic=topic` - Haberler

---

## 🐛 Sorun Giderme

### Model Yükleme Hatası
```
❌ Model yüklenirken hata
```
**Çözüm:** İnternet bağlantısını kontrol et, Hugging Face modellerini indir

### RAM Yetersiz
```
❌ Bellek hatası
```
**Çözüm:** Lighter modeli kullan:
```python
model = pipeline(
    "text-generation",
    model="distilgpt2",  # Hafif model
    device=0
)
```

### Web Araması Çalışmıyor
**Çözüm:** İnternet bağlantısını kontrol et

---

## 🚀 Gelecek Özellikler

- [ ] Ses Tanıma (Speech Recognition)
- [ ] Ses Sentezi (Text-to-Speech)
- [ ] Görüntü Analizi (Image Recognition)
- [ ] Dosya İşleme (File Upload/Download)
- [ ] Veritabanı Entegrasyonu
- [ ] Bulut Senkronizasyonu
- [ ] Mobil Uygulama
- [ ] Discord Bot Entegrasyonu

---

## 📊 Performans

| İşlem | Süre | Bellek |
|-------|------|--------|
| Başlangıç | ~5-10s | 800MB |
| Sohbet | ~1-3s | 900MB |
| Web Araması | ~2-5s | 850MB |
| Kod Üretimi | ~1-2s | 950MB |

---

## 🤝 Katkı

GK AI'ye katkı sağlamak için:

1. Repository'i fork et
2. Feature branch oluştur (`git checkout -b feature/AmazingFeature`)
3. Değişiklikleri commit et (`git commit -m 'Add AmazingFeature'`)
4. Branch'i push et (`git push origin feature/AmazingFeature`)
5. Pull Request aç

---

## 📞 İletişim

- **GitHub:** [@GameKinq0](https://github.com/GameKinq0)
- **Email:** gamekinq0@example.com
- **Discord:** GK AI Community

---

## 📄 Lisans

GK AI, MIT Lisansı altında yayınlanmıştır. Detaylar için `LICENSE` dosyasını gör.

---

## 🙏 Teşekkürler

- Hugging Face Transformers
- OpenAI
- DuckDuckGo
- PyInstaller
- Tüm açık kaynak katkıda bulunanlar

---

**Gelişmiş yapay zeka ile meşgul olmak sizi asla suçlamaz! 🤖✨**

**GK AI v1.0.0 - GameKinq0 tarafından geliştirildi**