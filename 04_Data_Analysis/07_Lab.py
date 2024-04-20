import numpy as np
import pandas as pd

df = pd.read_csv('data/auto.csv')
# print(df.head().to_string())

#Veri setimizde sütun isimleri yok. Veri setimize sütun isimleri basalım

df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
# print(df.head().to_string())

# Hatalı ve Eksik değeleri saptama
# Veri setimizde bazı hücrelerde '?' sembolü bulunmaktadır. Şayet veri setimizde bu tarz anormalliklerin bulunması durumunda veri setimizi her hangi bir Machine Learning algoritmasına
# sokup çalıştırmalıyız. Çünkü ML algoritmaları matematiksel işlemlere dayanmaktadır. Örneğin Regraasyon Entropi vb. Bu sebepten ötürü veri setimizde ki eksik yada hatalı alanları saptayıp onları ele almamız ML algoritması için hazırlamamız gerekmektedir.

# Step 1
# Eksik ve hatalı verileri ML algortimasında kullanamıoruz. Bunun için numpy kütüphanesinde bulunan NaN yani diğer programlama dillerinde Null diye geçen boş anlamına gelen veriyi eksik ve hatalı verilerle değiştireceğiz böylelikle ML algoritmasında bir hata ile karşılaşmayacağız.

df.replace('?',value=np.nan,inplace=True)
# print(df.head().to_string())

# Step 2
# Ne kadar eksik değerim var saptayalım

# aşağıdaki söz diziminde ilgili veri setinde ki başlıkların listesini verir
missing_value_df = df.isnull()
# print(missing_value_df.head().to_string())

# for item in missing_value_df.columns.values.tolist():
#     print(f'Column Name: {item}\n{missing_value_df[item].value_counts()}')

# Step 3
# Yukarıda hangi sütunda ne kadar missing value'muz var detect ettik şimdi onları handle edelim
# Peki neden uğraşıyoruz. Silip kurtulamaz mıyız? ML algoritmalarında ne kadar farklı veri ile algoritmamızı  train edersek o kadar başarılı sonuçlar elde ederiz bu nedenle her bir satır veri bizim için kıymetlidir.

# Eksik verileri ele alırken iki yöntem kullanabiliriz.
# Bunlar:
# 1. İlgili sütunda bulunan değerlerin ortalamasını alarak bu ortalamaya değeri eksik değerlerin bulunduğu hücreye yazabiliriz.
# 2. Yine ilgili sütunda bulunan değerlerin frekans aralığını bulup eksik değerlerin bulunduğu hücrelere yazabiliriz. Burada frekans aralığından kastımız ilgili sütunda bulunan değerlerin ne sıklıkla ilgili süğtunda bulunduğudur.

# Ortalama değeri bularak eksik veriler ile değiştirme
df['normalized-losses'].replace(to_replace=np.nan,
                                value=df['normalized-losses'].astype(float).mean())

# print(df.head().to_string())

# Frekans aralığı ile eksik verileri değiştirme
# value_counts() ==> bir sütunda geçen farklı değerlerin kaç tane olduğunu bize söyler
# idmax() ==> ilgili sütunda en çok geçen değeri bize söyler
df['num-of-doors'] = df['num-of-doors'].replace(to_replace=np.nan,
                                                value=df['num-of-doors'].value_counts().idxmax())
print(df['num-of-doors'].value_counts().idxmax())

#Veri standardizasyonu
# ML algoritmalarında kullanılacak veri setinde ki değerlerin belirli bir standartta olması gerekmektedir.Örneğin 2 veri kaynağımız olsun
# birisi amerikadan diperi avrupadan. Avrupadan gelen verilerde ki yakıt türü kilometre başına litredir lakit amerika da mile per galeon olarak hesaplanmaktadır. Yada
# avrupada kilogram kullanılırken amerikada pound yada libre birimleri kullanılmaktadı. Veri setinde ki bur farklı birimlere sahip değeler ML algoritmalarımızın
# train edilip ürettiği sonuçları olumsuz yönde etkileyecektir. Bu yüzden verimizin bir standartta olması gerekmektedir.
df['city_l/km'] = 235/df['city-mpg']
df['highway_l/km'] = 235/df['highway-mpg']

# veri normalizasyonu
# Belirli bir sütunda ki değerlerin benzer bir aralığa kavuşması işlemine veri normalizasyonu diyoruz. Veri setimizde bulunma length, width gibi değerlerin 0.1 - 1.9 vb bir aralığa yani daha küçük scalar büyüklüklere dönüştürülmesi için yapılan işlemlerdir.
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length','width','height']])

# Dummy Variable
# Veri setimizde sözel yada categorical değerler olabilir. Bu  değerler ML algoritmalarında kullanabilmek için onları scaler büyüklüklere dönüştürmemiz gerekmektedir.
# Veri setimizde 'fuel-type' sütunumuzda categorical değerler diesel, gas vb bulunmaktadır. Bunları scaler büyüklüklere dönüştürelim
dummy_variable_df = pd.get_dummies(df['fuel-type'],dtype='float')
print(dummy_variable_df.head())

# bakımını yaptığımız veri setimizi yeni bir excel yazalım
df.to_csv('clean_auto.csv')