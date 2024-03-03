# in   & not in

# name ="mert"
# print('m' in name)

#range()

# for i in range(10):
#     print(i,end =",")

#range(10 , 101 , 5)  -> 10 dan başlayıp 101 e kadar 5er 5er arrtacak bir tam sayı listesi oluşturur.


# Exp
# 0 - 100 arasında ki çift ve tek sayıların toplamlarını ayrı ayrı ekrana yazdıralım

# cift = 0
# tek = 0
# for i in range(101):
#     if i % 2 == 0:
#         cift += i
#     else:
#         tek += i
# print(f'tekler : {tek}  \n çiftler : {cift}')

#Nested For Loop
# for i in range(10):
#     for j in range(10):
#         pass

for i in range(4,0,-1):
    for j in range (i-1,4):
        print("x", end="")
    print(' ')
