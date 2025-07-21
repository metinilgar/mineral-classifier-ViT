# 🔬 Mineral Sınıflandırıcı - Vision Transformer (ViT)

Bu proje, **Vision Transformer (ViT)** modelini kullanarak mineral görüntülerini otomatik olarak sınıflandıran kapsamlı bir makine öğrenmesi sistemidir. Proje hem araştırma amaçlı Jupyter notebook hem de kullanıcı dostu web arayüzü içermektedir.

## 🎯 Proje Genel Bakış

### Desteklenen Mineral Türleri
- **Biotite** - Koyu renkli mika minerali
- **Bornite** - Bakır sülfür minerali  
- **Chrysocolla** - Bakır silikat minerali
- **Malachite** - Yeşil bakır karbonat minerali
- **Muscovite** - Açık renkli mika minerali
- **Pyrite** - Altın renginde demir sülfür minerali
- **Quartz** - Kristal silisyum oksit minerali

### Temel Özellikler
- 🤖 **Modern AI Teknolojisi:** Vision Transformer (ViT) mimarisi
- 📊 **Yüksek Doğruluk:** Eğitilmiş model ile güvenilir tahminler
- 🖥️ **Web Arayüzü:** Gradio ile kullanıcı dostu interface
- 📝 **Jupyter Notebook:** Detaylı araştırma ve geliştirme ortamı
- 📈 **Görsel Sonuçlar:** Plotly ile interaktif grafikler
- 🔄 **Çoklu Model Versiyonu:** Farklı model iterasyonları

## 📁 Proje Yapısı

```
mineral-classifier-ViT/
├── 📂 app/                          # Web Uygulaması
│   ├── app.py                       # Gradio web arayüzü
│   ├── model_loader.py              # Model yükleme modülü
│   ├── requirements.txt             # Python bağımlılıkları
│   ├── README.md                    # Web app dokümantasyonu
│   └── 📂 model/                    # Aktif model dosyaları
│       ├── config.json              # Model konfigürasyonu
│       ├── model.safetensors        # Eğitilmiş model ağırlıkları
│       └── preprocessor_config.json # Görüntü ön işleme ayarları
├── 📂 models/                       # Model Versiyonları
│   ├── 📂 v1/                      # Model Versiyon 1
│   ├── 📂 v2/                      # Model Versiyon 2
│   └── 📂 v3/                      # Model Versiyon 3
├── 📂 notebooks/                    # Jupyter Notebooks
│   └── Mineral_ViT.ipynb           # Ana geliştirme notebook'u
└── README.md                        # Bu dosya
```

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler
- Python 3.8+
- CUDA desteği (isteğe bağlı, GPU hızlandırması için)
- Minimum 4GB RAM
- 2GB boş disk alanı

### 2. Kurulum

```bash
# Projeyi klonlayın
git clone https://github.com/yourusername/mineral-classifier-ViT.git
cd mineral-classifier-ViT

# Sanal ortam oluşturun (önerilen)
python -m venv mineral_env
source mineral_env/bin/activate  # Linux/Mac
# veya
mineral_env\Scripts\activate     # Windows

# Gerekli paketleri yükleyin
cd app
pip install -r requirements.txt
```

### 3. Web Uygulamasını Çalıştırın

```bash
# App dizinine gidin
cd app

# Web arayüzünü başlatın
python app.py
```

Uygulama otomatik olarak tarayıcınızda açılacak: `http://127.0.0.1:7860`

## 📚 Kullanım Kılavuzu

### 🖥️ Web Arayüzü Kullanımı

1. **Model Yükleme:** Uygulama başladığında model otomatik yüklenir
2. **Görüntü Yükleme:** Sol panelden mineral görüntüsü seçin veya sürükle-bırak yapın
3. **Sınıflandırma:** "🔍 Görüntüyü Sınıflandır" butonuna tıklayın
4. **Sonuçları İnceleyin:** 
   - Ana tahmin ve güven skoru
   - Tüm sınıflar için detaylı skorlar
   - Interaktif grafik görünümü

### 📓 Jupyter Notebook Kullanımı

```bash
# Notebook dizinine gidin
cd notebooks

# Jupyter'ı başlatın
jupyter lab Mineral_ViT.ipynb
```

Notebook'ta bulacaklarınız:
- Veri setini indirme ve hazırlama
- Model eğitimi ve değerlendirme
- Görselleştirme ve analiz
- Model karşılaştırmaları

## 🔧 Teknik Detaylar

### Model Mimarisi
- **Tür:** Vision Transformer (ViT-Base)
- **Giriş Boyutu:** 224x224x3 RGB
- **Çıkış:** 7 sınıf (mineral türü)
- **Framework:** PyTorch + Transformers (Hugging Face)
- **Model Boyutu:** ~300MB

## 📸 Görüntü Gereksinimleri

### Kalite Standartları
- **Resolution:** En az 224x224 piksel
- **Format:** JPEG, PNG
- **Aydınlatma:** İyi ve eşit aydınlatma
- **Netlik:** Bulanık olmayan, keskin görüntü
- **Arka Plan:** Temiz, dikkat dağıtmayan arka plan

### İpuçları
✅ **İyi Örnekler:**
- Mineral tek başına çerçevelenmiş
- Doğal renkler korunmuş
- Yeterli detay görünür

❌ **Kaçınılması Gerekenler:**
- Çoklu mineral karışımı
- Aşırı yakın/uzak çekimler
- Kötü aydınlatma
- Bulanık veya gürültülü görüntüler

## 🔄 Model Versiyonları

### v1 - Temel Eğitim
- İlk eğitim iterasyonu
- Düşük epoch sayısı
- Temel ViT mimarisi

### v2 - Orta Seviye Eğitim
- Artırılmış epoch sayısı
- Daha uzun eğitim süresi
- İyileştirilmiş model performansı

### v3 - Tam Eğitim
- En yüksek epoch sayısı
- Maksimum eğitim iterasyonu
- En iyi model performansı


## 📊 Veri Seti

### Kaynak
- **Veri Seti:** [Minerals Identification Classification](https://www.kaggle.com/datasets/youcefattallah97/minerals-identification-classification)
- **Platform:** Kaggle
- **Boyut:** ~800MB
- **Görüntü Sayısı:** Binlerce mineral fotoğrafı

### Veri Yapısı
```
data/
├── biotite/
├── bornite/
├── chrysocolla/
├── malachite/
├── muscovite/
├── pyrite/
└── quartz/
```

## 📝 Lisans

Bu proje MIT lisansı altında dağıtılmaktadır. Detaylar için `LICENSE` dosyasını inceleyebilirsiniz.

---

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!** 