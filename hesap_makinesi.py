def hesap_makinesi():
    sayi1 = float(input('Birinci sayıyı giriniz:'))
    sayi2 = float(input('İkinci sayıyı giriniz:'))
    operator = input('İşlem operatörünü giriniz(+,-,/,*): ')
    
    if operator == '+':
        sonuc = sayi1 + sayi2
        
    elif operator == '-':
        sonuc = sayi1 - sayi2

    elif operator == '*':
        sonuc = sayi1 * sayi2

    elif operator == '/':
        sonuc = sayi1 / sayi2
    else:
        print('Geçersiz işlem operatörü')
        return
        
    print('Sonuç:', sonuc)

hesap_makinesi()


    

