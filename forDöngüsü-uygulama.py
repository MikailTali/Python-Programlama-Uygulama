sayilar = [3,5,7,2,12,32,45]

# 1 - 'sayilar'listesindeki her bir elemanı yazdırınız
for cevap1 in sayilar:
    print(cevap1)
# 2 - 'sayilar'listesindeki hangi sayılar 3'ün katıdır ? 
for cevap1 in sayilar:
    if cevap1 % 3 ==0:
        print(cevap1)
# 3 - 'sayilar'listesindeki tüm sayıların toplamı nediir ?
toplam = 0 
for cevap1 in sayilar:
    toplam += cevap1
    print(toplam) # for döngüsü 7 kez dönerek(tek seferdede yapılabilir.) ekranna yazdırır .


urunler = ['samsung s24' , 'samsung s22' , 'iphone 15' , 'iphone14']

# 4- 'urunler'listesindeki tüm iphone marka ürünlerini listeleyiniz. (find , index)
for urun in urunler:
    index =(urun.find('iphone')) # urun find ile -1 de yok 0 da var . koşul oluşturup önümüze çıkardık.
    if index > -1:
        print(urun)
    
# 5- 'urunler' listesinde kaç adet samsung ürünü vardır.
adet=0
for urun in urunler:
    index = (urun.find('samsung'))
    if index > -1 :
        adet += 1
print(adet) # tekrar et