
import pandas as pd

users = {
    'employee': ['Mert','Ali','Ahmet','Can'],
    'occupation': ['Kumarbaz','Kaçakcı','Dolandırıcı','Kumarbaz'],
    'neighbor': ['Sarıyer','Suadiye','Nişantaşı','Nişantaşı'],
    'income': [5000,4000,5000,5000],
    'age': [35,28,35,28]
}

# Group By
# Veri setimizde ki bazı değelere göre verilerimizi gruplamaya yarar. SQL temelleri veri tabanlarında da aynı mantık birebir aynı şekilde bulunmaktadır.

df = pd.DataFrame(users)
print(df.to_string())

# veri serimizi mesleklerine göre gruplayalım
# print(df.groupby('occupation').groups)

# hangi semtte kimler oturuyor
# for name, group in df.groupby('neighbor'):
#     print(name)
#     print(group)

# hangi semtte kaç çalışanım var

result = df.groupby('neighbor')['employee'].count()
df_groupby_result = pd.DataFrame(result)
print(df_groupby_result)


# mesleklere göre toplam maaşları listeleyin
result = df.groupby('occupation')['income'].sum()
print(result)

# mesleklere göre yaş ortalamasını bulun
result = df.groupby('occupation')['age'].mean()
print(result)