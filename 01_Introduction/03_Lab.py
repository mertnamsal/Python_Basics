try:
    x = int(input('Tam sayı giriniz'))
    sonuc = x/0
    print(sonuc)
except ZeroDivisionError as err:
    print(f'Hata var {err}')
else:
    print('Exception çalışmazsa çalışır')
finally:
    print('Çalıştı hertürlü')