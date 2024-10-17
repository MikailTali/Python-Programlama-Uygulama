# 1- Başlangıç ve bitiş degerlerini kullanicidan aliniz ve bu degerler arasindaki tüm cift sayilari yazdiriniz.
a = int(input('baslangic sayisi : '))
b = int(input('bitis sayisi : '))
c = a
while (c<b):
     if(c % 2 ==0):
          print(c)
          c+=2




# 2 - (1-100) arasındaki sayıları azalan şekilde yazdırınız.

i = 100
while i>= 1:
     print(i)
     i-=1
# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.
i = 0
sayilar = []
while(i<5):
     sayi = int(input('sayi:'))
     sayilar.append(sayi)
     i += 1
sayilar.sort()
print(sayilar)
# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.
username = ""

while not username:
     username = input("kullanıcı adı:")
print("girilen username : " + username )

     
          

