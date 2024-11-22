# Köşe Algılama Uygulaması - README

## Proje Hakkında

Bu proje, OpenCV ve Tkinter kullanarak bir kamera görüntüsü üzerinde köşe algılama işlemini gerçekleştiren bir Python uygulamasıdır. Uygulama, kamerayı başlatıp durdurabilme ve köşe algılama özelliğini açıp kapatma gibi temel işlevlere sahiptir.

---

## Gerekli Kütüphaneler

Uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

1. **OpenCV**: Görüntü işleme ve kamera kontrolü için.
   - Kurulum: `pip install opencv-python`
2. **NumPy**: Matematiksel işlemler ve veri manipülasyonu için.
   - Kurulum: `pip install numpy`
3. **Tkinter**: GUI (Grafiksel Kullanıcı Arayüzü) oluşturmak için (Python'da vars

---

# Yüz Takip Uygulaması - README

## Proje Hakkında

Bu proje, OpenCV kullanılarak gerçek zamanlı yüz algılama ve yüz takip işlemlerini gerçekleştiren bir Python uygulamasıdır. Haar cascades algoritması ile yüz algılanır ve MeanShift yöntemi ile takip edilir.

---

## Gerekli Kütüphaneler

Uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

1. **OpenCV**: Görüntü işleme ve yüz algılama/takibi için.
   - Kurulum: `pip install opencv-python`
2. **NumPy**: Matematiksel işlemler ve veri manipülasyonu için.
   - Kurulum: `pip install numpy`

---

## Projenin Özellikleri

1. **Yüz Algılama:**
   - OpenCV'nin `haarcascade_frontalface_default.xml` dosyası kullanılarak yüz algılanır.
   - İlk algılanan yüz, takip edilecek hedef olarak seçilir.

2. **Yüz Takibi:**
   - MeanShift algoritması, takip edilen yüzün yerini gerçek zamanlı olarak günceller.
   - Hedef bölge, bir dikdörtgen ile işaretlenir.

3. **Dinamik Görüntü İşleme:**
   - HSV renk uzayında geri projeksiyon tekniği kullanılarak hedef bölge belirlenir ve takip işlemi daha kararlı hale getirilir.

---

## Kullanım

### 1. Gerekli Kütüphaneleri Yükleme:
Projenin çalışması için aşağıdaki komutlarla kütüphaneleri yükleyin:
```bash
pip install opencv-python numpy

