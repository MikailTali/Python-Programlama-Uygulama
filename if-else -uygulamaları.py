# Bir aracın yakıt tipine göre (benzin , dizel , lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulama yapınız.
benzin : 39.35
dizel : 41.71
lpg : 20.28

benzin = 39.35
dizel = 41.71
lpg : 20.28
toplamYakitÜcreti = 0
ortalamYakitTüketimi = float(input('100 km deki ortalama yakit tüketim: '))
BelirtilenMesafe = int(input ('BelirtilenMesafe :'))
yakitTürü = str(input('yakitTürü: '))
ortalamaFiyat= (int(BelirtilenMesafe) * str('yakitTürü'))
toplamYakitTüketimi = BelirtilenMesafe * (ortalamYakitTüketimi/100)


if (yakitTürü==('benzin')):
      toplamYakitÜcreti = benzin * toplamYakitTüketimi
elif(yakitTürü==('dizel')):
      toplamYakitÜcreti = dizel * toplamYakitTüketimi
else : (yakitTürü==('lpg'))
toplamYakitÜcreti = benzin * toplamYakitTüketimi

print(toplamYakitÜcreti)


# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#  0-24 => 0 
#  25-44 => 1
#  45-54 => 2
#  55-69 => 3
#  69-84 => 4
#  85-100 => 5

yazyili1= int(input("yazili1 :"))
yazyili2= int(input("yazili2 :"))
sözlü1 = int(input("sözlü1 :"))
notOrtalama= int(yazyili1 + yazyili2 + sözlü1) / 3 

if(notOrtalama >= 0) and (notOrtalama <25):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 0")
elif (notOrtalama >= 25) and (notOrtalama <45):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 1")
elif (notOrtalama >= 45) and (notOrtalama <55):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 2")
elif (notOrtalama >= 55 ) and (notOrtalama <70):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 3")
elif (notOrtalama >= 70 ) and (notOrtalama <85):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 4")
elif (notOrtalama >= 85) and (notOrtalama <100):
     print(f"ortalamanız : {notOrtalama} ve başari durumu : 5")
else: print('başari durumu hatali')
