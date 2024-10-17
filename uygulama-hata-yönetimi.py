liste = ['1','2','3','21a','abc','10a','60']

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        sonuc=int(x)
        print(sonuc)
    except ValueError:
        continue

# 2: Kullanıcı 'quit(q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
while True:
    sayi = input('sayi: ')
    if (sayi== 'q'):
        break
    try:
        sonuc = float(sayi)
        print(f"girilen sayı: {sonuc}")
        break
    except ValueError:
        print('geçersiz sayı')
        continue


# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict,key) fonksiyonu hazırlayınız.
urun ={" urunAdi" : "samnsung s10"}

#d['fiyat'] -> KeyError
#get(urun,'fiyat') -> None
# get(urun, 'urunAdi') -> samsung S20

def get(list,key):
    try:
        return list[key]
    except KeyError:
        return None
sonuc = get(urun,'fiyat')

print(sonuc)