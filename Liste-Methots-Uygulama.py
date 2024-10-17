customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralik siparişi listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append(5000)
print(customers , order_totals)


# 2- Son eklenen siparişi siliniz.
customers.pop(-1)
print(customers)

# 3- Tüm müşteriler için aşağidaki özet cümleyi yazdırınız.
     # '<username>' isimli müşterinin sipariş toplamı <1000> liradir.
sonuc0 = f"{customers[0]} isimli müşterinin sipariş toplamli {order_totals[0]} liradir"
sonuc1 = f"{customers[1]} isimli müşterinin sipariş toplamli {order_totals[1]} liradir"
sonuc2 = f"{customers[2]} isimli müşterinin sipariş toplamli {order_totals[2]} liradir"
sonuc3 = f"{customers[3]} isimli müşterinin sipariş toplamli {order_totals[3]} liradir"
print(sonuc0)
print(sonuc1)
print(sonuc2)
print(sonuc3)

# 4- Müşterileri alfabetik olarak sıralayınız.
customers.sort()
print(customers)

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
print(order_totals)

# 6- En düşük sipariş hangisidir ?
endüşüksipariş = min(order_totals)
print(endüşüksipariş)

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır ?
tekraraAdet= customers.count("sadikturan")
print(tekraraAdet)

# 8- Customers listesinde 'ahmetyilmaz' isimli kullanıcıyı siliniz
customers.remove('ahmetyilmaz')
print(customers)

# 9- Listelerdeki tüm içerikleri siliniz.
customers.clear()
order_totals.clear()


# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
Kullanici1 = input("Kullanici1 :")
Toplam1 = input("Toplam1 : ")

customers.append(Kullanici1)
order_totals.append(Toplam1)

print(customers)
print(order_totals)
