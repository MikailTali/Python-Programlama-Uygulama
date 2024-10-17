# Klavyeden girilen n sayıdaki ögrenci bilgisini liste içerisinde saklayınız.
#          ** Dictionary listesi yapısı( ogrenciNo , ogrenciAdi , ogrenciSoyad) şeklinde olsun
#          **ürün ekleme işlemi bittiğinde ögrencileri listeleyiniz.

# ögrenci= {'ogrenciNo : ' : input('ogrenciNo') , 'ogrenciAd : ' : input('ogrenciAd') , 'ogrenciSoyad : ' : input('ogrenciSoyad')}
# n = int(ögrenci['ogrenciNo : '])
# # while n>0:
# #     print(ögrenci) 

# # print(ögrenci.items())
# devammi = 'evet'

# while (devammi !='hayir'):
#     ögrenci.append(
#         ögrenci.keys['ogrenciNo : '],
#         ögrenci.keys['ogrenciAd : '],
#         ögrenci.keys['ogrenciSoyad : ']
#     )
#     print(f"ögrenci no {ögrenci['ogrenciNo : ']} ögrenci adi {ögrenci['ogrenciAd : ']} ögrenci soyadı {ögrenci['ogrenciSoyad : ']}")
#     devammi = input('devam mi ? (evet/hayir)')
# print(ögrenci.values())
devammi = 'evet'
ogrenciler = []
while (devammi != 'hayir'):
    ögrenciNo = input('no:')
    ögrenciSoyad=input('soyad:')
    ögrenciAd = input('ad :')

    ogrenciler.append({        
        "ögrenciNo" : ögrenciNo,
        "ögrenciAd" : ögrenciAd ,
        "ögrenciSoyad" : ögrenciSoyad})

    devammi = input('devam mı (evet/hayır):')
for ogrenci in ogrenciler:
    print(f"{ogrenci['ögrenciNo']} numaralı ögrencinin adı {ogrenci['ögrenciAd']} {ogrenci['ögrenciSoyad']}")
