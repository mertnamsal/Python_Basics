
# KNN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing, metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/teleCust1000t.csv')
# print(df.head(20).to_string())

# hangi pakketti kullanan kaç kullanıcı var
# print(df['custcat'].value_counts())

# K-Nearst Neighborhood algoritması veri setimizde ki her bir satır yada noktanın bir diğerine olan mesafesini hesaplamak için geometrik hesaplamalar kullanır. Bunun için veri setinde ki her bir value alacağız. Esasen bir features matrix oluşturuyoruz.
X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed', 'employ', 'retire', 'gender', 'reside']].values
# print(X)

# custcat için de bir matrix yapalım
y = df['custcat'].values
# print(y)

# X matrix'inde ki değerleri incelediğimizde income verisinde 944, age verisinde 34 gender verisinde 0 yada 1 verileri bulunmaktadır. Bu tüm değerler scaler olarak farklı büyüklüklere sahip. Bu yüzden veri setimizde ki value'ları normalize edelim.
X = preprocessing.StandardScaler().fit_transform(X)
# print(X.tolist())

# Veri setini train & test olarak split edelim
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)
# print(f'Train Sets: {X_train.shape}, {y_train.shape}')
# print(f'test Sets: {X_test.shape}, {y_test.shape}')

# train ver setimizde ki her bir nokta için yani features için en yakın 4 komşusuna bakacaş şekilde KNN algoritmamızı train edelim. Burada 4 komşuya bakmasının her hangi bir mantığı yok kafamıza ögre verdik.
neighbor = KNeighborsClassifier(n_neighbors=4).fit(X_train, y_train)
y_result = neighbor.predict(X_test)
# print(y_result)

# Doğruluk değerlendirmesi
# Birden fazla sınıf oluşurulacak yada etiket oluşturulacak modellerde her bir sub class yada label için doğrulama yapmak gerekmektedir.
# print(f'Train Set Accuracy: {metrics.accuracy_score(y_train, neighbor.predict(X_train))}')
# print(f'Train Set Accuracy: {metrics.accuracy_score(y_test, neighbor.predict(X_test))}')
# Outputs:
# Train Set Accuracy: 0.575
# Train Set Accuracy: 0.2925
# Yukarıda ki çıktı incelendiğinde 4 komşu için algoritmanın başarısız olduğunu görebilirsiniz. Accuracy score 1're yaklaştıkça başarılıdır.

# Not: accuracy_score() fonksiyonu arkasında çalışan matematikte Jaccard Similarty Index kullanılmaktadır. Yani 'y_train' ile 'neighbor.predict(X_train)' arasındaki benzerliği ve çeşitliliği bulmak için kullanılmaktadır.

# Veri setimizde 4 tip telekominicasyon paketi var. Bu yüzden bizden 4 tane sınıf oluşturmamız ve kullanıcıların hangi sınıflara ait olduğunu saptamamız gerekmektedir. Bu bağlamda yeni gelen bir müşterinin features'larına göre ona en uygun paketi önerebilerim
# Yukarıda 4 komşu için başarısız olduk. Peki kaç komşuya bakarsak en iyi sonucu elde edeceğiz.
k_neigh = int(input('Please type K number: '))
array_lenght = k_neigh - 1
jsi_acc = np.zeros(array_lenght)
std_acc = np.zeros(array_lenght)

for k in range(1, k_neigh):
    neigh = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    y_pred = neigh.predict(X_test)

    jsi_acc[k - 1] = metrics.accuracy_score(y_test, y_pred)
    std_acc[k - 1] = np.std(y_pred == y_test) / np.sqrt(y_pred.shape[0])

print(f'JSI Score: {jsi_acc}')
print(f'SRD Score: {std_acc}')

plt.plot(range(1, k_neigh), jsi_acc, c='g')
plt.fill_between(
    range(1, k_neigh),
    jsi_acc - 1 * std_acc + 1 * std_acc,
    alpha=0.1
)
plt.legend(
    ('accuracy', 'std')
)
plt.xlabel('Number of Neighbor')
plt.ylabel('Accuracy')
plt.grid()
plt.tight_layout()
plt.show()

print(f'The best accuracy was with {jsi_acc.max()}, with k={jsi_acc.argmax()+1}')


