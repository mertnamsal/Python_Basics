

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
from math import floor


df = pd.read_csv('data/FuelConsumption.csv')


# Simple Linear Regression yapacağımız için sadece bir independent variable kullanacağız bu bağlamda tahmin edeceğimiz attribute ile independent variable içeren bir data frame hazırlayalım. Simple regrasyonda diğer alanlara ihtiyacımız yok.
# Independent Variable is ENGINESIZE
# Dependent Variable is CO2EMISSIONS
cdf = df[['ENGINESIZE', 'CO2EMISSIONS']]

# Split Main Data to Train & Test Sets
# Ana veri setimizi train ve test olmak üzere 2 ayrı veri setine bölüyoruz.
# Ana veri setimizin yüzde 80'lik kısmını train set için yüzde 20'lik kısmınıda test seti için kullanacağız. Burada ki değerler best practice'dir. Bu yüzdelerin arkasında ki mantık şudur, makine öğrenimi algoritmamızı ne kadar farklı ve çok data ile train edersek o kadar başarılı sonuç alırız. Bu yüzden veri setimizin %80'lik kısmını train için ayırıyoruz.
# Veri setimizi bölerken hem train hemde test setinin homojen olmasına özen göstermeliyiz. Örneğin veri setimizde a, b, c ve d tipi veriler olsun. Split işlemi sonucunda sadece a tipi verilerden oluşan bir train seti oluştursak ML algoritmanız b, c ve d veri tipleri için doğu sonuç vermez. Bu yüzden hem train hemde test seti heterojen değil homojen olmalıdır.
# Bu split işlemi tüm makine öğrenimi algoritmalarında kullanılır.
msk = np.random.rand(len(df)) <= 0.8
train_df = cdf[msk]
test_df = cdf[~msk]

# print(f'Train Set Shape: {train_df.shape}')
# print(type(train_df))
# print(f'Test Set Shape: {test_df.shape}')
# print(type(test_df))


regression = linear_model.LinearRegression()
train_x = np.asarray(train_df[['ENGINESIZE']])
train_y = np.asarray(train_df[['CO2EMISSIONS']])
regression.fit(train_x, train_y)
print('Coefficient: %.2f' % regression.coef_[0][0])
print('Intercept: %.2f' % regression.intercept_[0])

engine_size = float(input('Please type into engine size: '))
y = regression.intercept_[0] + regression.coef_[0][0] * engine_size
print(f'Carbon Emission Value: {floor(y)}')

plt.scatter(train_df['ENGINESIZE'],  train_df['CO2EMISSIONS'], color='r')
plt.plot(train_x, regression.coef_[0][0] * train_x + regression.intercept_[0], color='b')
plt.title('Relation About Between The Engine Size and Co2', c='r')
plt.xlabel('Engine Size', c='r')
plt.ylabel('Emission', c='r')
plt.show()

# regrasyon işlemi sonucunda elde ettiğimiz kat sayılar ne kadar doğru bunu test edelim. sklearn'ün çok güçlü metric kütüphanesi bulunmaktadır. biz burada r2 score gibi çok populer bir metrik algoritmasını kullanacağız. r2 sonucu 1're yakınsadıkça başarılı 0'ra yakınsadıkça test soncumuzun başarısız olduğunu söylemektedir. Bunun haricinde regrasyon ile Mean Square Error'de tercih edilmektedir
test_x = np.asarray(test_df[['ENGINESIZE']])
test_y = np.asarray(test_df[['CO2EMISSIONS']])
test_prediction = regression.predict(test_x)
print(test_prediction)
print('r2 score: %.2f' % r2_score(test_prediction, test_y))



