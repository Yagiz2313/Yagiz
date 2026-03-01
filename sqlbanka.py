import mysql.connector
from mysql.connector import Error

 
def veritabanina_kaydet(hesap_obj, musteri_obj):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='banka_iki_db',  
            user='root',         
            password='Yagiz2022!'   
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
             
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS banka_kayitlari (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    isim VARCHAR(100),
                    soyisim VARCHAR(100),
                    hesap_no INT,
                    kredi_notu INT,
                    segment VARCHAR(50),
                    durum VARCHAR(50),
                    tarih DATETIME
                )
            """)

            
            query = """INSERT INTO banka_kayitlari 
                       (isim, soyisim, hesap_no, kredi_notu, segment, durum, tarih) 
                       VALUES (%s, %s, %s, %s, %s, %s, NOW())"""
            
            values = (
                hesap_obj.isim, 
                hesap_obj.soyisim, 
                hesap_obj.hesap_no, 
                musteri_obj.kredi_notu, 
                musteri_obj.segment, 
                musteri_obj.durum
            )

            cursor.execute(query, values)
            connection.commit()
            print("\n[!] Veriler başarıyla MySQL Workbench'e aktarıldı.")

    except Error as e:
        print(f"Hata oluştu: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

 
class Hesap:
    def __init__(self, isim, soyisim, hesap_no, bakiye, borc):
        self.isim = isim
        self.soyisim = soyisim
        self.hesap_no = hesap_no
        self.bakiye = bakiye
        self.borc = borc

class Musteri:
    def __init__(self, kredi_notu):
        if kredi_notu > 1900:
             raise ValueError("Hata: Kredi notu 1900'den büyük olamaz!")
        self.kredi_notu = kredi_notu
        self.segment, self.durum = self.kredi_degerlendir()

    def kredi_degerlendir(self):
        if 1720 <= self.kredi_notu <= 1900: return "Çok İyi", "Alabilir"
        elif 1470 <= self.kredi_notu <= 1719: return "İyi", "Alabilir"
        elif 1150 <= self.kredi_notu <= 1469: return "Az Riskli", "Değişebilir"
        elif 970 <= self.kredi_notu <= 1149: return "Orta Riskli", "Alma İhtimali Düşük"
        else: return "En Riskli", "Alamaz"

 
try:
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    hesap_no = int(input("Hesap no: "))
    kredi = int(input("Kredi notunu giriniz: "))

    m1 = Musteri(kredi)
    i1 = Hesap(isim, soyisim, hesap_no, 0, 0)

     
    veritabanina_kaydet(i1, m1)

except ValueError as e:
    print(e)
