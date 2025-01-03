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

Yüz Algılama Uygulaması

Bu proje, OpenCV kullanarak gerçek zamanlı yüz algılama yapan bir Python uygulamasıdır. Uygulama, web kamerasından alınan görüntüleri analiz eder ve tespit edilen yüzleri dikdörtgenle işaretler.
Özellikler

    Gerçek Zamanlı Yüz Algılama: Uygulama, bağlı web kamerasından gelen görüntüleri işler.
    OpenCV Haar Cascade Modeli: Yüz algılama için OpenCV'nin önceden eğitilmiş Haar Cascade sınıflandırıcısı kullanılır.
    Basit ve Kullanıcı Dostu: Uygulama, sadece bir Python dosyası ile çalıştırılabilir.

Gereksinimler

    Python 3.x
    OpenCV kütüphanesi

Kurulum

    Depoyu Klonlayın:

git clone https://github.com/kullanici/yuz-algilama.git
cd yuz-algilama

Gerekli Kütüphaneyi Kurun:

pip install opencv-python

Programı Çalıştırın:

    python yuz_algilama.py

Kullanım

    Program çalıştırıldığında web kamerası açılır.
    Algılanan yüzler, mavi dikdörtgenlerle işaretlenir.
    Programdan çıkmak için klavyenizde q tuşuna basabilirsiniz.

Kodun Temel Mantığı

    Haar Cascade sınıflandırıcısı yüklenir:

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

Web kamerası başlatılır:

cap = cv2.VideoCapture(0)

Her karede yüz algılanır ve çizim yapılır:

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    q tuşuna basıldığında program sonlandırılır.

Ekran Görüntüsü

(Ekran görüntüsü eklemek için bir kare alabilirsiniz.)
Katkıda Bulunma

    Bu projeyi fork edin.
    Yeni bir dal (branch) oluşturun: git checkout -b yeni-ozellik.
    Değişikliklerinizi commit edin: git commit -m 'Yeni özellik ekle'.
    Dalınızı push edin: git push origin yeni-ozellik.
    Bir Pull Request açın.

Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
