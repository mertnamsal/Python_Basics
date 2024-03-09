# List
#index mantığıyla çalışır
#Uygulama içerisinde anlık bizim bir yada birden fazla değer tutan yapılardır.Farklı tiplerde değerler tutabilirler.Listelerde Ram üzerinde ..... alanında tutulduğu için değişkenler gibi uygulama sonlandığında RAM'den uçurulurlar yani Run Time içerisinde eklenilen değerleri Hard Disk gibi saklayamazlar.
from random import randint

#Listeler index mantığı ile çalışırlar.Liste içerisinde saklanılan değerler sıfırıncı



# word = input("PLease type").lower()
# for c in word:
#     print(c)
#
# liste = ['a', 'e', 'i', 'ı', 'o', 'ö', 'u', 'ü']
# sesli_harfler = []
# sessiz_harfler = []
#
# for c in word:
#     if c.isalpha():
#         if c not in sesli_harfler and c not in sessiz_harfler:
#             if c in liste:
#                 sesli_harfler.append(c)
#             else:
#                 sessiz_harfler.append(c)
# print(sessiz_harfler)
# print(sesli_harfler)

#Exp  iki listeyi random sayılar ile dolduralalım
#akabinde benzer index lerde tutulan değeleri toplayarak 3. listede gene aynı index'se yazalm
# random_list1 = []
# random_list2 = []
# random_list3 = []
# for i in range(10):
#     random_list1.insert(i,randint(0,100))
#     random_list2.insert(i,randint(0,100))
#     random_list3.insert(i,(random_list1[i]+random_list2[i]))
#
# print(random_list1)
# print(random_list2)
# print(random_list3)
#users listesi içerisinde bulunan kullanıcılara kurumsal mail adresi oluşturalım
# users  = ['burak yilmaz', 'mert namsal','kerim abdul cabbar okkes',' ']
# mail_adress = []
#
# for user in users:
#     if len(user) > 3:
#         name_surname = user.replace(" ", "_")
#         mail_adress.append(name_surname+"@gmail.com")
#
# print(mail_adress)

#kullanıcının girdiği password is valid mi ?
#1. girilen şifre en az 16 karakter uzunlugunda olmalı
# en az bir büyük bir kücük
# en az bir rakam
# en az bir noktalama işareti
# herhangi bir ifade tekrar etmemeli

#List Comprehansion
# [expresion for item in liste if  condition]

print([item for item in range(10)])

power = [item * item for item in range(10)]
print(power)

print([i * i for i in range(100) if i % 3 ==0])