# YouTube Transcript RAG - Kurulum ve Test Rehberi

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git

---

## 🚀 Adım 1: Projeyi İndir

```bash
# Repository'yi clone et
git clone https://github.com/ahmertsengol/Youtube-comment-RAG.git

# Klasöre gir
cd Youtube-comment-RAG

# Yeni branch'e geç (transcript fix'in olduğu branch)
git checkout claude/youtube-rag-tool-011CUxBb2Ps8FtXeY9knorEU
```

---

## 📦 Adım 2: Bağımlılıkları Yükle

```bash
# Virtual environment oluştur (opsiyonel ama önerilen)
python -m venv venv

# Virtual environment'ı aktif et
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Gerekli paketleri yükle
pip install -r requirements.txt
```

**Yüklenecek paketler:**
- `google-generativeai` - Gemini API için
- `apify-client` - Sadece channel video listesi için
- `youtube-transcript-api` - **Video transcript'leri için (ÜCRETSİZ)**
- `python-dotenv` - Environment variables için
- `rich` - Güzel terminal çıktısı için

---

## 🔑 Adım 3: API Anahtarlarını Ayarla

### 3.1. .env Dosyası Oluştur

```bash
# .env.example'dan kopyala
cp .env.example .env
```

### 3.2. API Anahtarlarını Al ve Ekle

#### Gemini API Key (Zorunlu - Sorgu için)
1. https://aistudio.google.com/app/apikey adresine git
2. "Create API Key" butonuna tıkla
3. API key'i kopyala

#### Apify API Token (Opsiyonel - Sadece channel scraping için)
1. https://console.apify.com/account/integrations adresine git
2. "Personal API tokens" bölümünden token'ı kopyala

**NOT:** Tek video test için Apify gerekmez!

### 3.3. .env Dosyasını Düzenle

`.env` dosyasını aç ve şunları ekle:

```env
# Gemini API Key (zorunlu)
GEMINI_API_KEY=your_gemini_api_key_here

# Apify API Token (sadece channel scraping için)
APIFY_API_TOKEN=your_apify_api_token_here
```

---

## 🧪 Adım 4: TEK VİDEO İLE TEST ET (ÖNERİLEN)

Bu test **hiçbir API key gerektirmez**, sadece transcript çekmeyi test eder:

```bash
python test_transcript.py
```

**Beklenen Çıktı:**
```
🧪 Testing YouTube Transcript Scraper
================================================================================
ℹ️  This test uses YouTube's FREE transcript API - no Apify needed!

Testing with video: https://www.youtube.com/watch?v=89CQRxq0YSg

Step 1: Testing single video transcript extraction...
--------------------------------------------------------------------------------

✅ SUCCESS! Transcript fetched:
   - Video ID: 89CQRxq0YSg
   - Title: Unknown Title
   - URL: https://www.youtube.com/watch?v=89CQRxq0YSg
   - Transcript length: 15234 characters

   First 500 characters of transcript:
   ----------------------------------------------------------------------------
   if you're not running AI models locally you're falling behind ...
   ----------------------------------------------------------------------------
```

**Eğer hata alırsan:**
- `pip install youtube-transcript-api` komutunu çalıştır
- Farklı bir video URL'i dene (bazı videolarda subtitle olmayabilir)

---

## 📺 Adım 5: CHANNEL'DAN TOPLU TEST ET

Eğer tek video testi başarılıysa, channel'dan toplu çekmeyi dene:

```bash
python main.py
```

**Örnek Kullanım:**
```
Enter YouTube channel URL: https://www.youtube.com/@DavidOndrej
How many videos to scrape? 3

🔍 Fetching video list from channel: https://www.youtube.com/@DavidOndrej
⏳ Running Apify YouTube scraper...
✅ Found 3 videos

📝 Fetching transcripts for 3 videos...

[1/3] Processing: If you don't run AI locally you're falling behind…
✅ Transcript fetched (15234 chars)

[2/3] Processing: AI Agent that codes for you
✅ Transcript fetched (12456 chars)

[3/3] Processing: Build AI apps with n8n
✅ Transcript fetched (18932 chars)

✅ Successfully scraped 3 videos with transcripts
💾 Saved: transcripts/89CQRxq0YSg.txt
💾 Saved: transcripts/7CYmTLHOUtU.txt
💾 Saved: transcripts/3fK5MvQGHLI.txt

✅ Saved 3 transcripts
```

---

## 💬 Adım 6: CHATBOT İLE KONUŞ

Transcript'ler indirildikten sonra, onlar üzerinden soru sor:

```bash
python chat.py
```

**Örnek Sorular:**
```
You: Bu videolarda hangi AI araçlarından bahsediyor?
Assistant: Videolarda Ollama, LM Studio, n8n gibi araçlardan bahsediyor...

You: Ollama nasıl kurulur?
Assistant: Ollama kurulumu için...

You: En çok hangi konular işlenmiş?
Assistant: Local AI model'leri çalıştırma, quantization, model selection...
```

**Çıkmak için:** `exit`, `quit` veya `Ctrl+C`

---

## 📁 Transcript Dosyaları

Transcript'ler `transcripts/` klasörüne kaydedilir:

```
transcripts/
├── 89CQRxq0YSg.txt
├── 7CYmTLHOUtU.txt
└── 3fK5MvQGHLI.txt
```

**Dosya İçeriği:**
```
Title: If you don't run AI locally you're falling behind…
URL: https://www.youtube.com/watch?v=89CQRxq0YSg

================================================================================

Transcript:
if you're not running AI models locally you're falling behind ...
```

---

## 🐛 Sık Karşılaşılan Hatalar

### 1. "APIFY_API_TOKEN not found"
**Çözüm:** Tek video testi için gerekli değil. Channel scraping yapmıyorsan görmezden gel.

### 2. "GEMINI_API_KEY not found"
**Çözüm:** `.env` dosyasını oluştur ve Gemini API key ekle.

### 3. "No transcript found"
**Çözüm:**
- Bazı videolarda subtitle olmayabilir
- Farklı bir video URL'i dene
- İngilizce içerikli videolar daha çok subtitle'a sahip

### 4. "Module not found"
**Çözüm:**
```bash
pip install -r requirements.txt
```

### 5. "AttributeError: 'YouTubeTranscriptApi' has no attribute"
**Çözüm:** Kütüphaneyi güncelle:
```bash
pip install --upgrade youtube-transcript-api
```

---

## 🎯 Hızlı Test Senaryosu

Tüm sistemi test etmek için:

```bash
# 1. Tek video testi (API key gerekmez)
python test_transcript.py

# 2. Eğer başarılıysa, requirements'ı kontrol et
pip list | grep -E "(youtube-transcript|gemini|apify)"

# 3. .env dosyasını kontrol et
cat .env

# 4. Gemini API key varsa, chat'i test et (mevcut transcript'lerle)
python chat.py
```

---

## 📊 Sistem Gereksinimleri

### Minimum:
- Python 3.8+
- 100 MB boş disk alanı
- İnternet bağlantısı

### Önerilen:
- Python 3.10+
- 500 MB boş disk alanı (çok transcript için)
- Kararlı internet bağlantısı

---

## 🆘 Yardım

Sorun yaşıyorsan:

1. **Hata mesajını oku** - genellikle ne yapman gerektiğini söyler
2. **Python versiyonunu kontrol et:** `python --version` (3.8+ olmalı)
3. **Dependencies'i yeniden yükle:** `pip install -r requirements.txt --force-reinstall`
4. **Virtual environment kullan** - paket çakışmalarını önler

---

## ✅ Test Başarılıysa

Artık YouTube videolarından transcript çekip, Gemini ile RAG sistemi üzerinden soru sorabilirsin!

**Kullanım senaryoları:**
- Uzun videoların içeriğini analiz et
- Belirli konuları ara ("Python", "Docker", etc.)
- Video serilerindeki bilgileri karşılaştır
- Öğrendiklerini özetle

---

## 🔄 Güncellemeler

Bu branch (`claude/youtube-rag-tool-011CUxBb2Ps8FtXeY9knorEU`) main'e merge edildikten sonra:

```bash
# main branch'e geç
git checkout main

# Güncellemeleri çek
git pull origin main

# Dependencies'i güncelle
pip install -r requirements.txt --upgrade
```

---

**İyi Kullanımlar!** 🚀