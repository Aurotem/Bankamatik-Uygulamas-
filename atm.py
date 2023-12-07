
"""! BANKAMATİK UYGULAMASI ÖDEVİ NEOS """
print("Bankamatik'e Hoş geldiniz! Yapılabilecek işlemler:")
print("1. Para Çek")
print("2. Para Yatır")
print("3. Bakiye Sorgula")
print("4. Çıkış Yap")
print("Numara girişi yaparak işlem seçebilirsiniz.")

bakiye = 0
atm_is_on = True

while atm_is_on:
    islem = input('Yapmak istediğiniz işlemi giriniz.')
    
    if islem == '1':
        tutar = int(input('Çekmek istediğiniz tutarı giriniz.'))
        if bakiye > tutar:
            bakiye = bakiye - tutar
            print(f"İşlem Başarılı! {tutar}TL miktarında para çektiniz ve hesabınızdaki toplam bakiye {bakiye}TL olarak güncellendi.")
        else:
            print('İşlem Başarısız! Bakiyeniz yeterli değil.')
    elif islem == '2':
        tutar = int(input('Yatırmak istediğiniz tutarı giriniz.'))
        bakiye = bakiye + tutar
        print(f"İşlem başarılı! Bakiyeniz {bakiye}TL olarak güncellendi.")
    elif islem == '3':
        print(f'Bakiyeniz: {bakiye}TL')
    elif islem == '4':
        print('ATM Kapatılıyor...')
        atm_is_on = False
    else:
        print('Lütfen geçerli bir işlem numarası giriniz!')