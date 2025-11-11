# YouTube Channel RAG Tool

YouTube kanallarından video transcript'lerini çekip, Google Gemini API ile AI destekli sohbet yapmanızı sağlayan bir RAG (Retrieval Augmented Generation) aracı.

## Özellikler

- YouTube kanalından video listesi çekme (Apify kullanarak)
- Video transcript'lerini otomatik çekme (ücretsiz YouTube Transcript API)
- Transcript'leri Gemini API'ye yükleme ve AI ile arama
- İnteraktif sohbet arayüzü ile video içeriği hakkında soru sorma
- Transcript'leri yerel olarak kaydetme

## Gereksinimler

- Python 3.8 veya üzeri
- Gemini API anahtarı: https://aistudio.google.com/app/apikey
- Apify API token: https://console.apify.com/account/integrations (sadece kanal çekmek için gerekli)

## Kurulum

### 1. Projeyi İndirin

```bash
git clone <repo-url>
cd Youtube-comment-RAG
```

### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

veya virtual environment kullanarak:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. API Anahtarlarını Ayarlayın

`.env` dosyası oluşturun:

```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin ve API anahtarlarınızı ekleyin:

```
GEMINI_API_KEY=your_gemini_api_key_here
APIFY_API_TOKEN=your_apify_api_token_here
```

**Not:** Tek video testi için Apify token'ı gerekli değildir. Sadece kanal çekmek için gereklidir.

## Kullanım

### Tam Akış (Çekme + Sohbet)

Videoları çekip hemen sohbete başlamak için:

```bash
python main.py
```

Program sizden şunları isteyecek:
1. YouTube kanal URL'i
2. Kaç video çekileceği (en yeni videolardan başlayarak)
3. Çekme ve indeksleme tamamlandıktan sonra sohbete başlayabilirsiniz

Örnek:
```
Enter YouTube channel URL: https://www.youtube.com/@channelname
How many videos to scrape: 10
```

### Mevcut Transcript'lerle Sohbet

Daha önce çekilmiş transcript'lerle sohbet etmek için:

```bash
python chat.py
```

Bu komut `transcripts/` klasöründeki mevcut transcript'leri yükleyip sohbet arayüzünü başlatır.

### Tek Video Testi

Tek bir video ile test yapmak için (Apify token gerekmez):

```bash
python -m tests.test_transcript
```

veya

```bash
cd tests && python test_transcript.py && cd ..
```

## Proje Yapısı

```
Youtube-comment-RAG/
├── main.py                 # Ana orkestrasyon scripti
├── chat.py                 # Bağımsız sohbet arayüzü
├── youtube_scraper.py     # YouTube transcript çekme modülü
├── gemini_rag.py          # Gemini API RAG implementasyonu
├── requirements.txt        # Python bağımlılıkları
├── setup.sh               # Otomatik kurulum scripti
├── .env.example           # Ortam değişkenleri şablonu
├── transcripts/           # Kaydedilen transcript'ler (otomatik oluşturulur)
├── tests/                 # Test dosyaları
│   ├── test_transcript.py
│   ├── test_imports.py
│   └── test_apify_config.py
├── utils/                 # Yardımcı scriptler
│   ├── cleanup.py
│   ├── examples.py
│   ├── debug_apify.py
│   └── list_gemini_models.py
└── docs/                  # Dokümantasyon
    ├── KURULUM.md
    ├── QUICKSTART.md
    └── PR_DETAILS.md
```

## Nasıl Çalışır

1. **Video Çekme**: Apify kullanarak YouTube kanalından video listesi çekilir
2. **Transcript Çekme**: Her video için ücretsiz YouTube Transcript API kullanılarak transcript çekilir
3. **Kaydetme**: Transcript'ler metadata ile birlikte `transcripts/` klasörüne kaydedilir
4. **İndeksleme**: Transcript'ler Gemini API'ye yüklenir ve AI destekli arama için hazırlanır
5. **Sohbet**: İnteraktif arayüz ile video içeriği hakkında sorular sorabilirsiniz

## Örnek Sorular

Transcript'ler indekslendikten sonra şu tür sorular sorabilirsiniz:

- "Bu videolarda hangi ana konular işleniyor?"
- "[Belirli bir konu] hakkında ne söylenmiş?"
- "[Anahtar kelime] hangi videolarda geçiyor?"
- "Farklı videolarda bahsedilen yaklaşımları karşılaştır"
- "Son videoda ne anlatılıyor?"

## Sorun Giderme

### "APIFY_API_TOKEN not found" hatası
`.env` dosyasında Apify token'ınızın olduğundan emin olun. Tek video testi için gerekli değildir.

### "No transcript files found" hatası
Önce `main.py` çalıştırarak videoları çekin veya `transcripts/` klasörünün var olduğundan emin olun.

### "Error uploading files" hatası
Gemini API anahtarınızın geçerli olduğunu ve yeterli kotanız olduğunu kontrol edin.

### Rate Limit Hataları
Her iki API'nin de rate limit'i vardır. Hata alırsanız:
- Apify: Plan limitlerinizi kontrol edin
- Gemini: Birkaç dakika bekleyin veya kotanızı kontrol edin

## Maliyet

- **Apify**: Ücretsiz tier sınırlı compute unit içerir. Fiyatlandırma: https://apify.com/pricing
- **Gemini API**: Rate limit'li ücretsiz tier mevcuttur. Fiyatlandırma: https://ai.google.dev/pricing
- **YouTube Transcript API**: Tamamen ücretsiz

## Modüller

### youtube_scraper.py
- `YouTubeScraper`: YouTube kanallarından video çekme sınıfı
- `scrape_channel()`: Kanaldan video çekme
- `save_transcripts()`: Transcript'leri dosyalara kaydetme

### gemini_rag.py
- `GeminiRAG`: Gemini API kullanan RAG implementasyonu
- `upload_files()`: Transcript'leri Gemini'ye yükleme
- `chat()`: RAG sistemini sorgulama
- `delete_all_files()`: Yüklenen dosyaları temizleme

## Lisans

MIT License
