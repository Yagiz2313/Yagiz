import tkinter as tk
import random

class TiklamaOyunu:
    def __init__(self, master):
        self.master = master
        master.title("Hızlı Tıklama Oyunu!")
        master.geometry("600x400")
        master.resizable(False, False)

        self.skor = 0
        self.oyun_basladi = False
        self.oyun_suresi = 10 

        # Arayüz Bileşenleri
        self.skor_etiketi = tk.Label(master, text=f"Skor: {self.skor}", font=("Helvetica", 16))
        self.skor_etiketi.pack(pady=10)

        self.baslat_butonu = tk.Button(master, text="Oyunu Başlat", command=self.oyunu_baslat, font=("Helvetica", 14), bg="green", fg="white")
        self.baslat_butonu.pack(pady=5)

        self.saniye_etiketi = tk.Label(master, text=f"Süre: {self.oyun_suresi}s", font=("Helvetica", 16))
        self.saniye_etiketi.pack(pady=5)
        
        # Oyun alanı
        self.canvas = tk.Canvas(master, width=580, height=250, bg="lightblue", bd=2, relief="groove")
        self.canvas.pack(pady=10)
        
        self.top = None
        self.zamanlayici_id = None

    def oyunu_baslat(self):
        if not self.oyun_basladi:
            self.oyun_basladi = True
            self.skor = 0
            self.oyun_suresi = 10
            self.skor_etiketi.config(text=f"Skor: {self.skor}")
            self.baslat_butonu.config(state=tk.DISABLED, text="Oyun Başladı!")
            self.canvas.bind("<Button-1>", self.topa_tiklandi)
            
            self.yeni_top_olustur()
            self.geri_sayim_baslat()

    def geri_sayim_baslat(self):
        if self.oyun_suresi > 0:
            self.oyun_suresi -= 1
            self.saniye_etiketi.config(text=f"Süre: {self.oyun_suresi}s")
            self.zamanlayici_id = self.master.after(1000, self.geri_sayim_baslat)
        else:
            self.oyunu_bitti() # Hata buradaydı, 'oyunu_bitti' olarak düzeltildi.

    def yeni_top_olustur(self):
        if self.top:
            self.canvas.delete(self.top)
            
        top_boyut = 30
        x = random.randint(0, 550)
        y = random.randint(0, 220)

        renkler = ["red", "blue", "green", "purple", "orange", "deeppink"]
        self.top = self.canvas.create_oval(x, y, x + top_boyut, y + top_boyut, fill=random.choice(renkler), outline="black")

    def topa_tiklandi(self, event):
        x, y = event.x, event.y
        items = self.canvas.find_overlapping(x-1, y-1, x+1, y+1) 
        
        if self.top in items:
            self.skor += 1
            self.skor_etiketi.config(text=f"Skor: {self.skor}")
            self.yeni_top_olustur()

    def oyunu_bitti(self):
        self.oyun_basladi = False
        self.canvas.unbind("<Button-1>")
        self.baslat_butonu.config(state=tk.NORMAL, text="Tekrar Oyna")
        
        if self.zamanlayici_id:
            self.master.after_cancel(self.zamanlayici_id)
        
        self.canvas.delete("all")
        self.canvas.create_text(290, 125, text=f"OYUN BİTTİ!\nSkorun: {self.skor}", 
                                 font=("Helvetica", 24, "bold"), justify="center", fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    oyun = TiklamaOyunu(root)
    root.mainloop()
