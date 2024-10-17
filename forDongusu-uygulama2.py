urunler=[
    {"urunAdi" : "HP Victus" , "fiyat":32999},
    {"urunAdi" : "Lenova thinkPad" , "fiyat":25499},
    {"urunAdi" : "Apple Macbook" , "fiyat":49999},
    {"urunAdi" : "Huawei Matebook" , "fiyat":26999},
    {"urunAdi" : "Casper Nirvana" , "fiyat":20000},
]

#1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#        'Hp Victus marka ürünün fiyatı 32999 Türk Lirası.'
for urun in urunler:
    print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} Türk Lirası.'")

# 2- Ürünlerin fiyatlari toplami nedir ?
toplam = 0
for urun in urunler :
    toplam += urun['fiyat']
print(f"{toplam} urunlerin toplam fiyatıdır")
    
    

# 3- 25000 ile 40000 arasindaki ürünleri listeleyiniz.
for urun in urunler:
    if urun["fiyat"]>=25000 and urun["fiyat"]<=40000:
        print(urun)



# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
anahtarKelime = input('aradiginiz anahtar kelime ')
for urun in urunler:
    if (urun["urunAdi"].lower().find(anahtarKelime.lower())) >-1:
        print(f"{urun} aradiğiniz kelimeye uygun arama bulunmuştur")



