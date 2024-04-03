
---

# Kombinasyon Hesaplama Programı

Bu Python programı, kullanıcının girdiği n ve r değerleri için kombinasyon hesaplar.

## Nasıl Kullanılır

1. `kombinasyon_hesaplama.py` dosyasını çalıştırın.
2. Program başlatıldığında, n ve r değerlerini girin.
3. Program, verilen n ve r değerleri için kombinasyon hesaplayacak ve sonucu ekrana yazdıracaktır.

## Örnek Kullanım

```
$ python kombinasyon_hesaplama.py
n değerini girin: 5
r değerini girin: 2
C(n, r) = 10.0
```

## Desteklenen Hatalar

- ValueError: Girilen değerlerin tam sayı olması gerekmektedir.
- ZeroDivisionError: 0'a bölme hatası oluştuğunda.

## Kullanım Notları

- `faktoriyel()` ve `kombinasyon()` fonksiyonlarına ilişkin detaylar program içerisinde belirtilmiştir.
- Bu program, n değerinin r'den küçük olamayacağını varsayar.

## Geliştirme

Bu program, basit bir kombinasyon hesaplama aracıdır. Geliştirmek için şunları düşünebilirsiniz:

- Kullanıcıya daha fazla geri bildirim sağlamak için hata mesajlarını iyileştirin.
- Farklı kombinasyon hesaplama algoritmalarını uygulayarak performansı optimize edin.
- Programın esnekliğini artırmak için kullanıcıya farklı giriş seçenekleri sunun.

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---
