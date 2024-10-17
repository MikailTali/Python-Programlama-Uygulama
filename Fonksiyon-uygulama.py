# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def yazdir(text,adet):
   return text*adet

print(yazdir('merhaba ' ,10))
   


# 2 - Diktörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
aKenari = int(input('a : '))
bKenari = int(input('b : '))

def alan ():
      return aKenari*bKenari
sonuc = alan()
    
def cevre():
     return (aKenari+bKenari) * 2
sonuc1 = cevre()

print(sonuc,sonuc1)

# 2. çözüm

def hesapla(kisa , uzun):
    alan = kisa*uzun
    cevre = 2*(kisa + uzun)
    return f"alan: {alan} cevre: {cevre}"

sonuc3= hesapla(3,2)
    



# 3-  Yazı tura uygulamasını fonksiyon kullanarak yapınız.(Random modülü)
def yaziTura():
    import random
    sayi =random.random() # 0 ile 1 arasında sayı üretir bize
    if sayi > 0.5:
        return 'tura'
    else:
        return 'yazi'
    
sonuc=yaziTura()
print(sonuc)

# 4-  Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asalSayi(sayi1,sayi2):
    for sayi in range(sayi1 , sayi2+1):
     if (sayi>1) :
         for i in range(2,sayi2):
             if (sayi % i == 0):
                 break
         else:
             print(sayi)    

asalSayi(10,20)
# 5-  Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tamBölenler(sayi3):
    for i in range(1,10):
       if (sayi3%i==0):
           print(i)

tamBölenler(15)
