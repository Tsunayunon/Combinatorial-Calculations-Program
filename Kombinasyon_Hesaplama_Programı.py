try:

    def faktoriyel(n):
        if n == 0 or n == 1:
            return 1
        else:
           return n * faktoriyel(n - 1)

    def kombinasyon(n, r):
        if n < r:
            return "Hata: n, r'den küçük olamaz!"
        else:
         kombinasyon_sonucu = faktoriyel(n) / (faktoriyel(r) * faktoriyel(n - r))
        return kombinasyon_sonucu

    n = int(input("n değerini girin: "))
    r = int(input("r değerini girin: "))

    print("C(n, r) =", kombinasyon(n, r))
except ValueError:
    print("tam sayı giriniz!")
except ZeroDivisionError:
    print("0'a bölme hatası!")


    if __name__ == "__main__":                  ##kodu baska bır projeye importlamak için kullanılır
        n = int(input("n değerini girin: "))     # import kombinasyon_hesapla 
        r = int(input("r değerini girin: "))
        print("C(n, r) =", kombinasyon(n, r))