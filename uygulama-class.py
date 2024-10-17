"""
**BankaHesabi isminde bir sınıf tanımlayiniz.
**Üretilen her bir nesne 'HesapSahibi' isminde bir özelliğe sahip olup başlanğıçta 0.0 değerinde olmalıdır. 'Bankasahibi:mikailtali
** Üretilen her bir nesne için 'paraYatir ' metodu oluşturun ve dişaridan yatirilacak miktar bilgisini alıp bakiye 
    üzerine ekleyin ve bakiye miktarini geri döndürün.
** Üretilen her bir nesne için 'paraCek'medou oluşturun ve dışarıdan çekilecek miktar bilgisini alip bakiye değerinden çikarip geriye döndürün.


    hesap = BankaHesabi('Mikail Tali')
    hesap.hesapSahibi -> Mikail Tali
    hesap.bakiye -> 0.0
    hesap.parayatir(1000) -> 1000.0
    hesap.paraCek(500) -> 500.0
"""

class BankaHesabi:
    def __init__(self , hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye=0.0
    
    def get_bakiye(self):
        return self.bakiye

    def paraYatir(self,miktar):
        self.bakiye += miktar
        return self.bakiye
    
    def paraCek(self,miktar):
        self.bakiye -= miktar
        return self.bakiye

hesap = BankaHesabi('mikail tali')
print(hesap.paraYatir(1000))
print(hesap.get_bakiye())
hesap.paraCek(500)
print(hesap.get_bakiye)



