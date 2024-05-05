

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing, metrics, tree
from sklearn.model_selection import train_test_split
from six import StringIO
import pydotplus
import matplotlib.image as mpimg


df = pd.read_csv('data/drug200.csv')
print(df.head(20).to_string())

X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values

# Yukarıda oluşturduğumuz X features matrix'sinde Sex, BP, Cholestrol gibi features'ların değerleri categoriecal yani sözel ifadeler olduğunu görebilirsiniz. Biz bu çalışmada karar ağacın algoritmasında entropy hesabı yapacağımız için yani aritmatiksel işlemler yapacağımız için bu categorical değerlerden faydalanamayız. İlgili features'leri scaler büyüklüklere dönüştüreceğiz.
le_sex = preprocessing.LabelEncoder().fit(['F', 'M'])
X[:, 1] = le_sex.transform(X[:, 1])

le_BP = preprocessing.LabelEncoder().fit(['LOW', 'NORMAL', 'HIGH'])
X[:, 2] = le_BP.transform(X[:, 2])

le_Chol = preprocessing.LabelEncoder().fit(['NORMAL', 'HIGH'])
X[:, 3] = le_Chol.transform(X[:, 3])

# Bütün datayı gene normalize ettik
X = preprocessing.StandardScaler().fit_transform(X)

y = df['Drug']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)

drug_tree = DecisionTreeClassifier(criterion='entropy')
# Decisin Tree algoritmasında oluşturulan yapraklarda (node) bilgi kazancına bakılacaksa 'entropy' yada log_loss bir başka değiş ile Shanon information gain yapılırken, yaprakta ki saflığa bakılacaksa 'gini' hesaplaması yapılır.
drug_tree.fit(X_train, y_train)
pred = drug_tree.predict(X_test)

print(f'Decision Tree Accucy Score: {metrics.accuracy_score(y_test, pred)}')


dot_data = StringIO()
filename = 'drugtree.png'
features_names = df.columns[0:5]
target_names = df['Drug'].unique().tolist()
out = tree.export_graphviz(
    drug_tree,
    feature_names=features_names,
    out_file=dot_data,
    class_names=np.unique(y_train),
    filled=True,
    special_characters=True,
    rotate=False
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.show(img, interpolation='nearest')