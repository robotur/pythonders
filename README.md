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
