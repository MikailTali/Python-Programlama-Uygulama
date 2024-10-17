# BANKAMATİK UYGULAMASI

# Hesap bilgileri tutulacak.(dict)
# menu , paraCekme , bakiyeSorgula , paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    {
        'ad':'mikail tali',
        'hesapNo' : '12324',
        'bakiye' : 20000,
        'ekHesap': 5000,
        'username' : 'mikailtali',
        'password': '3401'
    },
    {   'ad':'berivan tali',
        'hesapNo' : '12324',
        'bakiye' : 10000,
        'ekHesap': 2000,
        'username' : 'berivantali',
        'password': '3401' 
    }
]
def menu(hesap):
    
    print(f"merhaba, {hesap['ad']}")

    print('1- bakiye sorgulama')
    print('2- para çekme')
    print('3- para yatirma')

    islem = input("yapmak istediğiniz işlem :") 

    if islem =='1':
        bakiyeSorgula(hesap)
    elif islem =='2':
        paracekme(hesap)
    elif islem == '3':
        paraYatirma(hesap)
    else:
        print('yanlis seçim')
    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap['bakiye']}")
    print(f"ek bakiye: {hesap['ekHesap']}")

def paracekme(hesap):
    miktar = float(input('çekmek istediğiniz miktar:'))
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranizi alabilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimİzni = input('ek hesap kullanilsin mi ? (e/h): ' )

            if ekHesapKullanimİzni == 'e':
                kullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= kullanilacakMiktar
                print('paranizi alabilirsiniz')

            else:
                print('üzgünüz bakiyeniz yetersiz')

        else:
            print('üzgünüz bakiyeniz yetersiz')
def paraYatirma(hesap):
    yatirilanMiktar = int(input('yatirilmak istenen tutar:'))
    ekhesapborçDurumu = (input('ek hesap borcunuz var mi : evet / hayir '))
    if yatirilanMiktar >= hesap['ekHesap']:
        if ekhesapborçDurumu == 'hayir' :
            print(f"ek hesap borcunuz bulunmamakta güncel bakiyeniz ({hesap['bakiye']} + {yatirilanMiktar})")
            
        else:
            print(f"ek hesap borcunuz bulunmaktadir yatirilan tutardan ek hesap borcunuz düşmüştür.")
            print(f"güncel bakiyeniz {yatirilanMiktar} - {hesap['ekHesap']}) + {hesap['bakiye']}")
            
        

    elif yatirilanMiktar <= hesap['ekHesap']:
        print(f"yatirilan miktardan ek hesap borcunuz düşmüştür kalan borcunuz ({hesap['ekHesap']} - {yatirilanMiktar})")




       



def login():
    username = input('username: ')
    password = input('parola:')
    isLoggedIn = False

    for hesap in hesaplar:
        if hesap['username'] == username and hesap['password'] == password:
            isLoggedIn = True
            menu(hesap)
            break
        
        if not (isLoggedIn):
            print('username ya da parola yanliş')

login()