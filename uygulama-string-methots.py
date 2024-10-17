kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- "Btk Akademi " karekter dizisinin baş ve sondaki boşluk karekterlerini siliniz
sonuc0='Btk Akademi'.split()
print(sonuc0)

# 2- kursAdi değişkenindeki tüm karekterleri küçük harfe çeviriniz.
sonuc = kursAdi.lower()
print(sonuc)

# 3- website değişkeninde kaç tane '.' karekteri vardır ? 
sonuc2= website.count('.')
print(sonuc2)

# 4- website değişkeni 'https' ile mi başlıyor ? 
sonuc1 = website.startswith('https')
print(sonuc1)

# 5- website 'tr' ile mi bitiyor ? 
sonuc2= website.endswith('tr')
print(sonuc2)

# 6- kursAdi içerisindeki tüm karekterler harflerden mi oluşuyor?
sonuc3= website.isalpha()
print(sonuc3)

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz.
sonuc4= kursAdi.replace(' ' , '-')
print(sonuc4)

# 8- kursAdi değişkenindeki python kelimesini mikail ile değiştiriniz.
sonuc5= kursAdi.replace('Python' , 'mikail')
print(sonuc5)

# 9- website değişkeni 'ww' içeriyor mu ?
sonuc6 = website.index('ww')
print(sonuc6)

# 10- kursAdi değişkeninini listeye çeviriniz.
sonuc7= kursAdi.split()
print(sonuc7)