#Tuple (Demetler)
#List ler gibi benzer mantığa sahiptirler. Lakin listelere uyguladığımız built in fonksiyonlara sahip değildir. Lakin indexleme mantığı Tuple'da mevcuttur.
#Hem Listelerde hemde demetlerde ki ortak noktalardan bir diğeride slicing (dilimleme)
#Tuple sabitlerimi tutacağım bir yapı gibi düşünebilirsiniz. Yani değiştirilemezler. 2 tuple birleştirme gibi opsiyonlar vardır.
#Listeler gibi farklı tiplerde değerler tutabiliriz.

# tuple_1 = ('Galatasaray', 'Fenerbahçe', 'Beşiktaş', 'Tranbzonspor')
# tuple_2 = ('12','35.5','b','Eagles','Patrios','Red Skins')
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3) # ('Galatasaray', 'Fenerbahçe', 'Beşiktaş', 'Tranbzonspor', '12', '35.5', 'b', 'Eagles', 'Patrios', 'Red Skins')
#
# #Slicing
#
# print(tuple_3[0:3]) #  -> 0,1 ,2 indexleri
# print(tuple_3[::2]) # 0,2,4 diye gider
# print(tuple_3[-1]) # Red Skins son index
# print(tuple_3[::-1]) # terse çevirir
# print(tuple_3[3::-2]) # Trabzon ,fener

tuple_4 = ('Sarıyer',('Suadiye','Erenköy'),('Yeniköy','Bebek',('Etiler','Ulus')))
print(tuple_4[2]) # ('Yeniköy', 'Bebek', ('Etiler', 'Ulus'))
print(tuple_4[1][1]) #Erenköy
print(tuple_4[2][2][0]) # Etiler