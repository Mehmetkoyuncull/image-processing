# Image Processing Algorithms (Python & NumPy)

Bu depo, görüntü işleme alanında temel ve ileri düzey algoritmaların Python ve NumPy kullanılarak uygulandığı kapsamlı bir çalışma koleksiyonudur. Her klasör, görüntü işleme literatüründe önemli bir kavrama veya metoda karşılık gelir ve tüm kodlar eğitim, akademik araştırma ve uygulama geliştirme süreçlerine uygun olacak şekilde düzenlenmiştir.

Depodaki amaç; görüntü işleme konularını hem teorik hem pratik olarak anlamak, her bir algoritmanın çalışma mantığını adım adım görmek, görüntü manipülasyonunun temel yapı taşlarını öğrenmek ve gelecekteki üst seviye projeler için güçlü bir temel oluşturmaktır.

---

## 1. Projenin Amacı

Bu çalışmanın genel hedefleri şunlardır:

- **Görüntü işleme prensiplerini uygulamalı şekilde öğrenmek**
- **Python ve NumPy ile düşük seviyeli görüntü manipülasyonlarını gerçekleştirmek**
- Filtreleme, dönüşüm, histogram işlemleri, kenar tespiti, segmentasyon ve morfolojik işlemler gibi konuların algoritmik mantığını kavramak
- Her klasörün kendi içerisinde bağımsız bir örnek sunması sayesinde modüler bir öğrenme ve geliştirme ortamı oluşturmak
- Ders, laboratuvar, proje veya araştırma çalışmaları için doğrudan kullanılabilir kaynak hazırlamak

Bu depo; bilgisayar mühendisliği öğrencileri, görüntü işleme ile ilgilenen araştırmacılar ve temel algoritmaların nasıl işlediğini görmek isteyen herkes için referans niteliğindedir.

---

## 2. Kullanılan Teknolojiler

Projede sadece çekirdek kütüphaneler kullanılmıştır:

- **Python 3.x**
- **NumPy**
- (Bazı klasörlerde) Matplotlib – yalnızca görselleştirme amaçlı
- Standart Python dosya okuma/yazma işlemleri

OpenCV gibi gelişmiş kütüphaneler kasıtlı olarak kullanılmamıştır.  
Bu sayede algoritmalar tamamen **sıfırdan** uygulanmış, böylece öğrenme odaklı bir yapı sağlanmıştır.

---

## 3. Depodaki Konular

Depo, görüntü işleme alanının temel yapı taşlarını kapsayan geniş bir konu yelpazesi içerir. Bunlar arasında:

### **Dönüşümler ve Temel İşlemler**
- Bit plane slicing
- Grey level transformations
- Logarithmic transformations
- Power law (Gamma) transformations
- Contrast stretching
- Negative images
- Intensity level slicing

### **Histogram Tabanlı İşlemler**
- Histogram equalization
- Histogram matching

### **Uzaysal Filtreler**
- Linear spatial filters
- Nonlinear (order-statistic) filters
- Low-pass smoothing filters
- Weighted smoothing filters
- Gaussian filters
- Median filter
- Spatial filtering temelleri

### **Kenar Tespiti ve Türevsel İşlemler**
- Sobel, Prewitt, Roberts
- Laplacian
- Second Order Derivative
- The Marr–Hildreth Edge Detector
- Canny edge detection
- Thresholding yöntemleri

### **Morfolojik İşlemler ve Segmentasyon**
- Morphological filtering
- Image segmentation
- Connected components analysis
- Component labeling

### **Dönüşümsel Yaklaşımlar**
- Hough Transform
- Image sampling and quantization
- Spatial resolution

### **Diğer Temel Konular**
- Image acquisition and representation
- Interpolation
- Nonlinear spatial filter yapıları
- Edge linking ve global işlem teknikleri

Depodaki klasörlerin her biri, o konuya ait Python dosyaları ve gerekli açıklamaları içeren küçük bir çalışma alanı şeklindedir.

---

## 4. Dosya Yapısı

Proje yapısı modüler olacak şekilde tasarlanmıştır. Her klasör bir algoritmaya veya konuya karşılık gelir. Her klasörde:

- İlgili algoritmanın Python kodu
- Açıklayıcı notlar veya açıklamalar
- Gerekliyse yardımcı fonksiyonlar

bulunur.

Bu sayede kullanıcı, herhangi bir konuya doğrudan gidip uygulamayı çalıştırabilir.

---

## 5. Kodların Çalıştırılması

Projeyi kendi bilgisayarında çalıştırmak için:

### Depoyu klonla:
```bash
git clone https://github.com/Mehmetkoyuncull/image-processing.git
