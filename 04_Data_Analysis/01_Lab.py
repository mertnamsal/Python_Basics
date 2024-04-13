
import pandas as pd
import numpy as np

number = [20, 30, 40, 50]
letters = ['a','b','c','d']
scaler = 5
dictionary = {
    'a': 10,
    'b': 20,
    'c': 30
}
ny_array = np.array([20, 30, 40, 40])

# pandas kütüphanesinde 2 ana veri tipi bulunmaktadır. Bunlardan 1. Series bir diğeri ise Dataframe dir.
# pd_series = pd.Series(number)
# print(pd_series)
# print(type(pd_series)) # <class 'pandas.core.series.Series'>

# pandas serisi ML(Machine Learning) algoritmalarında ki matematiksel işlemleri yada istatistiksel methodları kullanırken ihtiyac duyacağız
# pd_series = pd.Series(letters)
# print(pd_series)

# pythondaki sözlük objesinin anahtarlarını index valueları ise series value'su olarak ayarladı.
pd_series = pd.Series(dictionary)
print(pd_series)

# python temellerinde öğrnediğimiz dilimleme işlemini pandas serilerinde de kullanabiliriz.
# print(pd_series[:2])

#pandas serilerinin sahip olduğu bazı built-in fonksiyonlar ve attribute'ler.
# not: aynı fonksiyon ve attribute'lar Dataframe içinde kullanılabilir.
print(pd_series.shape) # verinin kaç satır ve sütundan oluştuğunu döner

print(pd_series.dtype) # serinin veri tipini döner

print(pd_series.ndim) # serinin kaç katmanlı olduğunu döner

print(pd_series.describe()) # serinin

print(pd_series.head(1)) # serinin ilk indexten başlayarak argüman olarak verilen  değere kadar olan indexleri döner. head() default değeri 5 tir.

print(pd_series.tail(1)) #head fonksiyonun tam tersi yani son index ten başlayarak head mantığında çalışır

#şartın tutup tutmamasına göre tru false dönen
print(pd_series >= 20)

print(pd_series % 2 == 0)

# Aggragete function olarak isimlendirilen sum(), min(), max(), count() gibi fonksiyonları kullanabiliriz
print(f'Bütün değerlerin toplamı: {pd_series.sum()}')

opel_2000 = pd.Series([20,30,40],['astra','corsa','vetra'])
opel_2001 = pd.Series([50,60,70],['astra','corsa','vetra'])

total = opel_2000 + opel_2001
print(total)

# DataFrame
# pandas yoğun olarak kullanılan bir başka yapıdır. excel gibi düşüebilirsiniz yani satır ve sütunlardan oluşan bir yapısı söz konusudur.
df = pd.DataFrame(
    data=np.random.rand(3, 5),
    index=['A', 'B', 'C'],
    columns=['Column1','Column2','Column3','Column4','Column5']
)
print(df)

# DataFrame üzerinden veri seçme (select)
print(df['Column2'])
print(type(df['Column2']))

# Tek kareli parantez ile select attığımda tek sütun çağırabilirken double kareli parantez kullandığımda birden fazla sütun çağırabilirim. Bu yüzden kullandığım kareli parantez dönen verinin tipine etki etmektedir. Tek pkareli parantez series dönerken, double kareli parantez dataframe döner.

# loc[] index değelerini vererek istediğimiz index değerinede tutulan kayda erişebiliriz.
print(df.loc['B'])
print(type(df.loc['B']))

print(df.loc['C', 'Column3'])
print(type(df.loc['C', 'Column3']))

print(df.loc[:, ['Column1', 'Column3']])

print(df.loc[['A','C'],['Column2','Column4']])