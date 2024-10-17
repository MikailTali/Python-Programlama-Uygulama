# NOT UYGULAMASI 
#1- Menu
    # 1- Not Gir
    # 2- Ortalamaları Göster (90-100 -> AA , 85-89 -> BA)
    # 3- Notları Kayıt Et
    # 4- Çıkış
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ögrenciAdi = liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+not2+not3)/3
    if ortalama>= 90 and ortalama <=100:
        harf='AA'
    elif ortalama>=80 and ortalama<= 89:
        harf='BA'
    elif ortalama>=75 and ortalama<= 79:
        harf='BB'

    elif ortalama>=70 and ortalama<= 74:
        harf='CB'

    elif ortalama>=65 and ortalama<= 69:
        harf='CC'
    elif ortalama>=60 and ortalama<= 64:
        harf='DC'
    
    return f"{ögrenciAdi}  :  {harf} - ( {ortalama} )"


    


def not_gir():
    ad = input('ögrenci adı :')
    soyad = input('ögrenci soyad:')
    not1 = input('not1')
    not2 = input('not2')
    not3 = input('not3')
    with open('sinav_notlari.txt' , 'a' , encoding='utf-8')as file:
        file.write(ad+ ' ' +soyad + ':' +not1 + ',' + not2 + ',' +not3+'\n')
def notlari_oku():
    with open('sinav_notlari.txt' , 'r',encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))
def notlarikayitEt():
    with open('sinav_notlari.txt' , 'r' , encoding='utf-8') as file:
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir))
    with open('sinav_notlari.txt' , 'w' , encoding='utf-8') as file2:
        file2.writelines(liste)
    
        
def Cikis():
    pass 
while True:
    islem = input('1- Not gir\n2-Notlari Oku\n3-Notlari Kayit et\nÇikiş\nseçim:')
    
    if islem =='1':
        not_gir()
    elif islem=='2':
        notlari_oku()
    elif islem=='3':
        notlarikayitEt()
    else:
        break
    