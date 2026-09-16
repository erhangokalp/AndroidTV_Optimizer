# 📺 Android TV & Google TV Hızlandırıcı & Debloat Aracı

[🇬🇧 **English Documentation**](README.md) | [🇹🇷 **Türkçe Kullanım Kılavuzu**](README_TR.md)

---

![Android TV Optimizer](Screenshot_4.jpg)

> **Tüm Android TV ve Google TV cihazlarını (Philips, TCL, Xiaomi, Sony, Vestel vb.) tek tıkla gereksiz arka plan servislerinden, reklam ve öneri şeritlerinden arındıran; menü geçişlerini hızlandıran güvenli masaüstü aracı.**

---

## 🌟 Neden Bu Aracı Kullanmalısınız?

Televizyon üreticileri ve Google; cihazlara mağaza demoları, kullanılmayan yazıcı/takvim servisleri, kullanım alışkanlıklarınızı toplayan telemetri araçları ve ana ekrana sürekli reklam/öneri şeritleri yükler. 2 GB gibi kısıtlı belleğe (RAM) sahip televizyonlar zamanla şişer, kumanda komutlarına geç yanıt verir ve kasılmaya başlar.

- ✅ **Root veya Bootloader kilidi gerektirmez.**
- ✅ **Widevine L1 sertifikasını bozmaz.** (Netflix, Prime Video gibi platformlar 4K HDR kalitesinde oynamaya devam eder).
- ✅ **Sıfır Veri Kaybı Riski!** Hiçbir dosya veya sistem paketi silinmez (`pm uninstall` yasaktır); yalnızca `pm disable-user --user 0` komutuyla uyutulur.
- ✅ **Tek Tıkla Geri Alınabilir.** İstediğiniz an tek bir butona basarak televizyonu ilk fabrika yazılımı haline döndürebilirsiniz (`pm enable`).
- ✅ **HDMI ve Kumandanızı Korur.** TCL'in meşhur Girişler tuşu (`suspension`), Philips Ambilight, ses ve klavye servisleri kod seviyesinde koruma altındadır.
- ✅ **Çift Dil Desteği.** Sağ üst köşeden anında **Türkçe** ve **English** arasında geçiş yapabilirsiniz.
- ✅ **%100 Taşınabilir (Portable).** Bilgisayarınızda Python veya ADB kurulu olması gerekmez.

---

## 📺 Desteklenen Markalar ve Akıllı Profiller
- **Philips:** Özel Ambilight, HDMI girişleri ve kanal tuner koruması.
- **TCL:** Quick Panel (`suspension`), Kaynak Seçici ve Bluetooth kumanda koruması.
- **Xiaomi & Mi TV / Mi Box / Stick:** Bluetooth kumanda ve TVInput koruması.
- **Sony Bravia:** Görüntü (X-Reality) ve ses motorları koruması.
- **Vestel / Regal / Toshiba / Grundig:** TV Tuner ve giriş koruması.
- **Chromecast with Google TV ve Diğer Android TV Cihazları:** Evrensel güvenli profil.

---

## 🚀 3 Adımda Kullanım Kılavuzu

### 1. Adım: Televizyonu Hazırlama (Sadece 1 Seferlik)
1. TV'nizde **Ayarlar > Cihaz Tercihleri > Hakkında** bölümüne gidin.
2. **"Android TV işletim sistemi derlemesi"** (veya Yapı Numarası) satırının üzerine gelin ve kumandanızın **OK tuşuna arka arkaya 7 kez** basın. *"Artık bir geliştiricisiniz!"* yazısını göreceksiniz.
3. Geri gelip **Geliştirici Seçenekleri** menüsüne girin ve **"USB Hata Ayıklama"** seçeneğini açık konuma getirin.
4. TV'nizin IP adresini öğrenin: **Ayarlar > Ağ ve İnternet > Bağlı olduğunuz ağ durumu** (Örnek: `192.168.1.100`).

> ⚠️ **ÖNEMLİ:** Bilgisayarınız ile televizyonunuz **aynı yerel Wi-Fi veya kablolu ağa** bağlı olmalıdır.

---

### 2. Adım: Programı Çalıştırma & Bağlanma
1. İndirdiğiniz zip arşivini bir klasöre çıkartın.
2. **`AndroidTV_Optimizer.exe`** dosyasına çift tıklayarak çalıştırın.
3. **TV IP Adresi** kutusuna televizyonunuzun IP'sini yazıp **"🔌 TV'ye Bağlan"** butonuna basın.
4. **Televizyon ekranınıza bakın:** Ekranda *"Bu bilgisayara her zaman izin verilsin mi?"* penceresi çıkacaktır. Kumandayla **"İzin Ver / Tamam"** seçeneğini onaylayın.
5. Programda yeşil ışık yanacak, TV'nizin markası ve boş RAM miktarı görüntülenecektir.

---

### 3. Adım: Temizlik ve Hızlandırma
- 🚀 **Akıllı Temizlik:** Butona tıklayın. Program televizyonunuzun markasına uygun olarak yaklaşık 20-30 adet gereksiz arka plan servisini ve reklam motorunu güvenle kapatır.
- ⚡ **Animasyonları 0.5x Yap:** Menü açılış ve geçiş hızlarını iki katına çıkarır.
- 🧹 **RAM & Önbellek Temizle:** Bellekteki gereksiz kalıntıları temizler.

---

## 🏠 (İsteğe Bağlı) Ana Ekrandaki Reklamlardan Tamamen Kurtulma: FLauncher
Google TV'nin kendi ana ekranındaki film ve sponsorlu dizi reklamlarından sıkıldıysanız:
1. TV'deki Google Play Store'dan **FLauncher** uygulamasını yükleyin (ücretsiz ve açık kaynaklıdır).
2. Programdaki **"🎯 FLauncher'ı Aktif Et"** butonuna basın.
3. Program FLauncher'ın kurulu olduğunu doğrulayıp eski reklamlı ana ekranı devre dışı bırakır. Artık kumandadan Home tuşuna bastığınızda sadece tertemiz uygulama listeniz gelir.

---

## ⏪ Her Şeyi İlk Günkü Haline Geri Döndürme (Restore)
İleride televizyonu satmak isterseniz ya da fabrika çıkış haline dönmek isterseniz:
1. Programı açıp TV'ye bağlanın.
2. **"⏪ Tüm Paketleri Geri Aç (Fabrika Haline Dön)"** butonuna tıklayın.
3. Birkaç saniye içinde kapatılan tüm orijinal sistem servisleri yeniden aktif hale gelecektir.

---

## ❓ Sıkça Sorulan Sorular (SSS)

**S: Netflix, YouTube veya PS5/HDMI çalışmayı durdurur mu?**  
**C:** Kesinlikle hayır. Program; HDMI geçiş servislerini, ses sürücülerini, kumanda bluetooth protokollerini ve DRM/Widevine altyapısını asla kapatmaz.

**S: TV güncelleme alırsa ne olur?**  
**C:** Televizyonunuza resmi bir Android güncellemesi geldiğinde sistem bu ayarları otomatik olarak fabrika haline döndürebilir. Böyle bir durumda programı tekrar açıp tek tıkla temizliği tekrarlayabilirsiniz.

**S: Bilgisayarımda Python veya ADB kurulu olması gerekir mi?**  
**C:** Hayır! Bu klasör tamamen taşınabilirdir (portable). Gerekli tüm motorlar gömülü olarak yer almaktadır.
