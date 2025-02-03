

# Vücut Yüzey Alanı Hesaplama Programı

Bu Python projesi, kullanıcıdan kilo ve boy verilerini alarak **Vücut Yüzey Alanı** (BSA) hesaplayan basit bir masaüstü uygulamasıdır. Uygulama, kullanıcı dostu bir arayüze sahiptir ve **CustomTkinter** kütüphanesini kullanarak geliştirilmiştir. 

Vücut Yüzey Alanı, özellikle tıbbi hesaplamalar için önemli bir parametredir ve bu programda **Mosteller formülü** kullanılarak hesaplanmaktadır.

---

## Özellikler

- Kullanıcıdan **kilo** ve **boy** verilerini alır.
- **Vücut Yüzey Alanı (BSA)** hesaplamasını yapar.
- Hatalı giriş durumunda kullanıcıyı bilgilendirir.
- Görsel ve kullanıcı dostu bir arayüz sağlar.
- **CustomTkinter** kullanılarak geliştirilmiştir, bu da uygulamanın şık ve modern görünmesini sağlar.

---

## Kullanılan Kütüphaneler

- **CustomTkinter**: Modern ve özelleştirilebilir Tkinter widget'ları sağlar.
- **NumPy**: Hesaplamalar için kullanılan kütüphane.
- **Pillow (PIL)**: Görsel işleme ve arka plan resmi ekleme.
- **Tkinter**: Python için standart GUI kütüphanesi.

---

## Kurulum

Projenin çalışabilmesi için aşağıdaki kütüphanelerin sisteminizde kurulu olması gerekmektedir:

```bash
pip install customtkinter numpy pillow
```

---

## Kullanım

1. Programı çalıştırarak kullanıcı arayüzüne erişebilirsiniz.
2. Kilo ve boy bilgilerinizi sırasıyla girin.
3. "Hesapla" butonuna basarak **Vücut Yüzey Alanı** sonucunu görüntüleyin.
4. Eğer geçerli bir sayı girilmezse, kullanıcıya hata mesajı gösterilecektir.

---

## Hesaplama Formülü

Bu programda **Vücut Yüzey Alanı (BSA)**, aşağıdaki formülle hesaplanır:

\[
img
\]

- **Kilo**: Kullanıcının kilosu (kg).
- **Boy**: Kullanıcının boyu (cm).

---

## Ekran Görüntüsü

![Uygulama Görseli](assets/bsa-application.png)

---

## Lisans

Bu proje, **MIT Lisansı** altında lisanslanmıştır. [Lisansı Görüntüle](LICENSE).

---

## Katkı

Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Yorumlar, öneriler ve hata raporları için [GitHub Issues](https://github.com/kullanici/VSCO1prjct/issues) sayfasını kullanabilirsiniz.

---

## Yazar

**Ali Emir Sertbaş**  
[GitHub Profil](https://github.com/kullanici)

---

**Not:** Projede kullanılan görsel `/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/ımage/BSA.png` yolunda depolanmış olmalıdır. Görsel yolunu gerektiği şekilde güncelleyin.

--- 

Bu şablon, projenizi tanıtan ve kullanıcıları bilgilendiren temel bir README dosyasını kapsamaktadır. Eğer projenize başka özellikler eklerseniz, bunları da README'ye dahil edebilirsiniz.
