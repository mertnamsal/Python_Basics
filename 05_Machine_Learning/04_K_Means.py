import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv('data/Cust_Segmentation.csv')

df.drop('Address', axis=1, inplace=True)

df['Defaulted'].replace(
    np.nan,
    df['Defaulted'].astype(float).mean(),
    inplace=True
)

# print(df.head(50).to_string())

# Normalizasyon
X = df.values[:, 1:]  # diğer örneklere göre features matrix bu yöntemle oluşturdum
# X = np.nan_to_num(X)  # NaN değerler yerine zero bastım
Clus_dataSet = StandardScaler().fit_transform(X)
# print(Clus_dataSet)

# n_clusters => Train sonucunda elde edilecek küme saytısı
# n_init => KMeasns algoritmasında veri seti içerisinde ki en uygun en iyi sonucu vericek olan merkez noktalarını saptamak için kaç deneme yapılmasını istiyorsak onu yazıyoruz.
# init => Ampirik olasılık dağılımına göre örneklemeyi kullanarak başlangıç küme merkezlerini seçmek için kullanılır
# init'in 2 farklı argümanı vardır greedyy ve vanilla her ikiside en iyi ağırlık merkezini seçmek için kullanılır.
# Vanilla k-means++ => merkez belirlemede olasılık yaklaşımını kullanır
# Greedy k-means++ => her biir veri setinde ki features göre tek tek deneyerek merkezi bulur
k_means = KMeans(init='k-means++', n_clusters=3, n_init=12)
k_means.fit(X)
labels = k_means.labels_
print(labels)

df['Clus_km'] = labels
print(df.head(20).to_string())

