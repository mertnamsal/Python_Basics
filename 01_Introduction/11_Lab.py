# Değer döndüren fonksiyonalar (returnable)

# lst = [12, 11, 19, 2, 99]
# lst_1 = []
# lst_2 = []
#
# #lst içerisindeki çift sayıları 2 ile çarparak lst_1 içerisine ekleyelim
# #tek sayıları 3 ile çarparak lst_2 ye ekleyelim
#
# def tek_cift(sayi: int) -> bool:
#     if sayi % 2 == 0:
#         return True
#     else:
#         return False
#
# def append_list(result:bool,counter:int) -> None:
#     if result:
#         lst_1.append(counter * 2)
#     else:
#         lst_2.append(counter * 3)
#
# def main():
#     for i in lst:
#         result = tek_cift(i)
#         append_list(result,i)
#     print(lst_1)
#     print(lst_2)
#
# main()

# Kullanıcıdan alınan 3 adet sayıyı topladıktan sorna karesini alan ve ekrana yazdıralım

# def get_three_number():
#     list = []
#     for i in range(3):
#         list.append(int(input("int : ")))
#     return list
#
#
# def square_of_it(number: int):
#     return number * number
#
#
# def sum(sayi_list : list):
#     sum = 0
#     for number in sayi_list:
#         sum = sum+ number
#     return sum
# def main():
#     number_list = get_three_number()
#     print(square_of_it(sum(number_list)))
#
# main()

# Aşağıdaki listede bulunan rakamların liste içerisinde geçme sıklığını bulun ve sözlük tipinde çıktı verin
# rakamın kendisi key geçme sıklığı value olcak şekilde

#bir söz öbeğinde tekrar eden kelimelerden arındırarak çıktı verelim
#örnek input => merhaba ben burak burak ben burak
#output => merhaba ben burak
# liste = ["elma", "armut", "elma", "portakal", "armut", "üzüm", "çilek", "elma"]
# def tekrar_edeni_cikar(kelimeler : list):
#     yalin_liste = []
#     for kelime in kelimeler:
#         if kelime not in yalin_liste:
#             yalin_liste.append(kelime)
#     return yalin_liste
# print(tekrar_edeni_cikar(liste))

#kullanicidan alinan söz öbeğindeki keliemleri alfabetik olarak sıralayalm
# cumle = "merhaba python nasılsın"
# list = cumle.split(' ')
# list.sort()
# print(list)