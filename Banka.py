import datetime

class Hesap:
    def __init__(self, isim, soyisim, hesap_no,  bakiye, borc):
        self.isim     = isim
        self.soyisim  = soyisim
        self.hesap_no = hesap_no
        self.bakiye   = bakiye
        self.borc     = borc
        self.borclu_mu = True
        
    def __str__(self):
        durum = "Borçlu" if self.borclu_mu else "Borçlu değil"
        return f"[{self.isim} {self.soyisim} {self.hesapno} - Borc: {self.borc} TL - Bakiye: {self.bakiye}"
    def BankaHesabı(Hesap):

        def __init__(self, isim, soyisim, hesap_no, bakiye, borc, icra):
            super().__init__(isim, soyisim, hesap_no, bakiye, borc)
            self.icra = icra

           
class Musteri:

    def __init__(self, kredi_notu):
        self.kredi_notu = kredi_notu
        self.segment, self.durum = self.kredi_degerlendir()

    def kredi_degerlendir(self):
        if self.kredi_notu > 1900:
            raise ValueError("Hata: Kredi notu 1900'den büyük olamaz! Program sonlandırılıyor.")

        if 1720 <= self.kredi_notu <= 1900:
            return "Çok İyi", "Alabilir"

        elif 1470 <= self.kredi_notu <= 1719:
            return "İyi", "Alabilir"

        elif 1150 <= self.kredi_notu <= 1469:
            return "Az Riskli", "Değişebilir"

        elif 970 <= self.kredi_notu <= 1149:
            return "Orta Riskli", "Alma İhtimali Düşük"

        else:
            return "En Riskli", "Alamaz"
        

isim = input("isim: ")
soyisim = input("Soyisim: ")
hesap_no = int(input("Hesap no: "))
kredi = int(input("Kredi notunu giriniz: "))

m1 = Musteri(kredi)

i = Hesap(isim, soyisim, hesap_no, 0, 0)

print("\n--- Müşteri Bilgileri ---")
print("İsim:", i.isim)
print("Soyisim:", i.soyisim)
print("Hesap no:", i.hesap_no)

print("\n--- Kredi Değerlendirme Sonucu ---")
print("Kredi Notu:", m1.kredi_notu)
print("Segment:", m1.segment)
print("Durum:", m1.durum)

