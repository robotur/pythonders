Köşe Algılama Uygulaması - README
Proje Hakkında

Bu proje, OpenCV ve Tkinter kullanarak bir kamera görüntüsü üzerinde köşe algılama işlemini gerçekleştiren bir Python uygulamasıdır. Uygulama, kamerayı başlatıp durdurabilme ve köşe algılama özelliğini açıp kapatma gibi temel işlevlere sahiptir.
Gerekli Kütüphaneler

Uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

    OpenCV: Görüntü işleme ve kamera kontrolü için.
        Kurulum: pip install opencv-python
    NumPy: Matematiksel işlemler ve veri manipülasyonu için.
        Kurulum: pip install numpy
    Tkinter: GUI (Grafiksel Kullanıcı Arayüzü) oluşturmak için (Python'da varsayılan olarak gelir).
    Pillow: Tkinter ile uyumlu görüntü işleme için.
        Kurulum: pip install pillow

Projenin Özellikleri

    Kamerayı Başlatma ve Durdurma:
        Kamera görüntüsü, pencere üzerine gerçek zamanlı olarak yansıtılır.
        Kamera durdurulduğunda görüntü sonlandırılır.

    Köşe Algılama:
        Köşe algılama özelliği açıldığında, görüntü üzerindeki köşe noktaları yeşil dairelerle işaretlenir.
        OpenCV'nin cv2.goodFeaturesToTrack fonksiyonu kullanılarak uygulanır.

    Dinamik Kontrol:
        Uygulama içerisindeki butonlar aracılığıyla kamera kontrolü ve köşe algılama özelliği kolayca yönetilebilir.

# Yüz Algılama Uygulaması

Bu proje, OpenCV kullanarak gerçek zamanlı yüz algılama yapan bir Python uygulamasıdır. Web kamerasından alınan görüntülerde yüz algılar ve bunları dikdörtgenlerle işaretler.

## Özellikler

- **Gerçek Zamanlı Yüz Algılama**: Web kamerası üzerinden çalışır.
- **OpenCV Haar Cascade**: Önceden eğitilmiş modelle yüksek doğruluk.
- **Kullanıcı Dostu**: Sadece birkaç adımda çalıştırabilirsiniz.

## Gereksinimler

- **Python 3.x**  
- **OpenCV** kütüphanesi (opencv-python)

## Kurulum

1. **Depoyu Klonlayın**:
    ```bash
    git clone https://github.com/kullanici/yuz-algilama.git
    cd yuz-algilama
    ```

2. **Gerekli Paketleri Yükleyin**:
    ```bash
    pip install opencv-python
    ```

3. **Uygulamayı Çalıştırın**:
    ```bash
    python yuz_algilama.py
    ```

## Kullanım

- Program çalıştırıldığında web kamerası açılır.
- Algılanan yüzler, mavi dikdörtgenlerle işaretlenir.
- Programı kapatmak için **q** tuşuna basın.

## Kod Mantığı

1. **Haar Cascade Sınıflandırıcısı**:
    ```python
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    ```

2. **Web Kamerasının Açılması**:
    ```python
    cap = cv2.VideoCapture(0)
    ```

3. **Yüz Algılama ve İşaretleme**:
    ```python
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    ```

4. **Programın Sonlandırılması**:
    ```python
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ```

## Örnek Görüntü

_(Ekran görüntüsü eklemek için bir kare alabilirsiniz.)_

## Katkıda Bulunma

1. Bu projeyi fork edin.
2. Yeni bir dal (branch) oluşturun:
    ```bash
    git checkout -b yeni-ozellik
    ```
3. Değişikliklerinizi commit edin:
    ```bash
    git commit -m 'Yeni özellik eklendi'
    ```
4. Dalınızı push edin:
    ```bash
    git push origin yeni-ozellik
    ```
5. Bir **Pull Request** açın.

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
