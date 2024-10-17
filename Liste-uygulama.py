# 1- "toyota , bmw, renualt , mercedes " elemanlarına sahip markalar isimli bir liste oluşturunuz.
arabalar=["toyota","renualt","mercedes"]
print(arabalar)
print(type(arabalar))
# 2 - Liste kaç elemanlıdır ?
print(len(arabalar))
# 3- Listenin ilk ve son elemanı nedir ? 
print(arabalar[0] + arabalar[-1])
# 4 - "renualt" markasını " togg" ile güncelleyiniz.
arabalar[1] = "togg"
print(arabalar)
# 5- "tog" listenin bir elemanı mıdır ?
sonuc = "togg" in arabalar
print(sonuc)
# 6- listenin ilk 2 elemanını alınız.
print(arabalar[:2])
# 7- listenin sonuna "ford" ve "citroen" markalarını ekleyiniz.
print(arabalar + ["ford" , "citroen"] )
# 8- listenin son elemanını siliniz.
#del arabalar[4]
#print(arabalar)

# 9- Aşağıdaki verileri liste içerisinde saklayınız.
   # ögrenci1: Yigit Bilgi 2010 [70,80,90]
   # ögrenci2: Ada Bilgi 2011 [70,70,80]
   # ögrenci3: Çınar Turan 2017[60,60,90]
ögrenci1 = ["Yigit" , "Bilgi" , 2010, [70,80,90]]
ögrenci2 = ["Ada" , "Bilgi" , 2011 , [70,70,80]]
ögrenci3 = ["Çinar" , "Turan" , 2017 ,[60,60,90]]

ögrenciler = [ögrenci1 , ögrenci2 , ögrenci3]
# 10- ögrencilerin yaşlarını hesaplayınız.
yasYiğit = 2024 - ögrenci1[2]
yasAda = 2024 - ögrenci2[2]
yasÇinar = 2024 - ögrenci3[2]

print(yasYiğit,yasAda,yasÇinar)
# 11- Ögrencilerin not ortalamarını hesaplayınız.
ortalamaYiğit = (ögrenciler[0][3][0] + ögrenciler[0][3][1] + ögrenciler[0][3][2]) / 3
ortalamaAda = (ögrenciler[1][3][0] + ögrenciler[1][3][1] + ögrenciler[1][3][2]) / 3
ortalamaÇinar = (ögrenciler[2][3][0] + ögrenciler[2][3][1] + ögrenciler[2][3][2]) / 3
print(ortalamaYiğit , ortalamaAda , ortalamaÇinar)
