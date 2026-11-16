# AI Image Generation with FLUX.1 Schnell

## 📌 Proje Hakkında

Bu proje, Python ve Cloudflare Workers AI kullanılarak geliştirilen yapay zekâ destekli bir görsel üretim çalışmasıdır.

Projede Black Forest Labs tarafından geliştirilen FLUX.1 Schnell modeli kullanılarak metin açıklamalarından görseller oluşturulmaktadır.

Geliştirme sürecinde görsel üretiminin yanı sıra prompt hazırlama, API üzerinden görsel verisi alma ve Python ile temel görsel işleme işlemleri üzerinde çalıştım.

Amacım, metinden görsel üretme sürecini uygulamalı olarak öğrenmek ve yapay zekâ modellerinin görsel üretim yeteneklerini Python ile kullanabilmekti.

## 🚀 Özellikler

### 1. Text-to-Image (Metinden Görsel Üretimi)

- Kullanıcının hazırladığı prompt üzerinden görsel üretimi
- Cloudflare Workers AI API entegrasyonu
- FLUX.1 Schnell modelinin kullanılması
- Görsel üretim adımlarının `steps` parametresiyle ayarlanması

### 2. Prompt Engineering

Görsel üretiminde daha kontrollü sonuçlar elde etmek için prompt hazırlama üzerine çalıştım.

Prompt oluştururken aşağıdaki unsurları kullandım:

- Subject: Ana karakter veya nesne
- Environment: Mekân ve çevre
- Action: Karakterin gerçekleştirdiği eylem
- Style: Görsel tarz
- Lighting: Işıklandırma
- Composition: Görsel kompozisyon ve kamera açısı

### 3. API Yanıtlarının İşlenmesi

Cloudflare API üzerinden gelen görsel verisi Base64 formatında alınmaktadır.

Python'un `base64` modülü kullanılarak bu veri çözülmekte ve PNG dosyası olarak kaydedilmektedir.

### 4. Pillow ile Görsel İşleme

Üretilen görseller üzerinde Pillow kütüphanesi kullanılarak çeşitli işlemler gerçekleştirilmektedir.

- Görseli açma ve görüntüleme
- Görsel boyutunu yeniden ayarlama (Resize)
- Görselin belirli bir alanını kırpma (Crop)
- PNG formatını JPEG formatına dönüştürme
- JPEG kalite ayarını belirleme

### 5. Hata Yönetimi

API istekleri sırasında oluşabilecek bağlantı, zaman aşımı ve yanıt işleme hatalarını kontrol etmek için `try-except` yapısı kullanılmaktadır.

## 🛠️ Kullanılan Teknolojiler

- **Python:** Uygulamanın geliştirilmesi.
- **Cloudflare Workers AI:** Görsel üretim API hizmeti.
- **FLUX.1 Schnell:** Metinden görsel üretim modeli.
- **Requests:** API isteklerinin gönderilmesi.
- **Python-dotenv:** API bilgilerinin ortam değişkenlerinden okunması.
- **Base64:** API'den gelen görsel verisinin çözülmesi.
- **Pillow (PIL):** Görsel işleme ve format dönüştürme.

## 📂 Proje Yapısı

```text
ai-image-generation/
│
├── image_generate.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**Dosyaların görevleri:**

- `image_generate.py`: API bağlantısını, görsel üretim fonksiyonunu ve görsel işleme işlemlerini içerir.
- `requirements.txt`: Projede kullanılan Python bağımlılıklarını listeler.
- `.env`: Cloudflare API Token ve Account ID bilgilerini saklar.
- `.gitignore`: Gizli ve gereksiz dosyaların Git takibine alınmasını engeller.

## ⚙️ Kurulum

### 1. Repository'yi klonlayın

```bash
git clone REPOSITORY_URL
cd ai-image-generation
```

### 2. Sanal ortam oluşturun

```bash
python -m venv venv
```

Sanal ortamı etkinleştirin.

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Gerekli kütüphaneleri yükleyin

```bash
pip install -r requirements.txt
```

### 4. Cloudflare API bilgilerini tanımlayın

Cloudflare hesabınızdan Workers AI API Token ve Account ID bilgilerinizi edinin.

Proje ana dizininde `.env` isimli bir dosya oluşturun:

```env
CLOUDFLARE_API_TOKEN=YOUR_API_TOKEN
CLOUDFLARE_ACCOUNT_ID=YOUR_ACCOUNT_ID
```

Kendi bilgilerinizi ilgili alanlara ekleyin.

**Önemli:** API Token ve Account ID bilgilerinizi herkese açık GitHub repository'lerinde paylaşmayın.

## 💻 Kullanım

`image_generate.py` dosyası çalıştırıldığında tanımlanan prompt Cloudflare Workers AI API'ye gönderilir.

Örnek prompt:

```python
metin = """
A small female calico kitten peacefully sleeping
on a wooden garden table under an apple tree.

The scene takes place in a beautiful garden
on a sunny afternoon.

Warm golden hour sunlight,
soft natural shadows.

Photorealistic photography.
"""
```

Görsel üretim fonksiyonu:

```python
generate_image(metin)
```

API'den başarılı yanıt alındığında görsel Base64 formatından çözülerek PNG dosyasına kaydedilir.

Ardından Pillow ile yeniden boyutlandırma, kırpma ve format dönüştürme işlemleri gerçekleştirilebilir.

## 🧠 Geliştirme Sürecinde Kazandığım Deneyimler

Bu proje üzerinde çalışırken aşağıdaki konularda uygulamalı deneyim kazandım:

- Python ile API entegrasyonu
- Cloudflare Workers AI kullanımı
- FLUX.1 Schnell ile Text-to-Image
- Prompt Engineering
- HTTP POST istekleri ve JSON yanıtlarının işlenmesi
- Base64 ile görsel verisi işleme
- Pillow ile görsel manipülasyonu
- Görsel boyutlandırma ve kırpma
- PNG ve JPEG formatları arasında dönüşüm
- Python fonksiyonları ve hata yönetimi
- Ortam değişkenleri ile API anahtarı yönetimi

## 👩‍💻 Geliştirici

**Meryem Küçük**

[GitHub Profilim](https://github.com/Meryemkerimekucuk)
