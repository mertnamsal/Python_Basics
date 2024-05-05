import pandas as pd

df = pd.read_csv('data/nba.csv')

# En yüksek maaşı alan oyuncu kim
# print(
#     df[
#         df['Salary'] == df['Salary'].max()
#     ]
#     [['Name', 'Salary']]
# )

# takımlara göre oyuncuların maaş ortalmaası nedir?
# print(df.groupby('Team')['Salary'].mean().astype('object'))

# veri setinde kaç farklı takım var. (groupby ile yapılır ama bir başka fonksiyon daha var bu iş için)
# bir sütunda ki biricik değerleri nasıl sayarım
# group by ile yaparsam satır sayarken null olan satırlarıda sayabilirim bu yüzden bu örneği gruopby ile rislidir
# print(df['Team'].nunique())


# Yaşı 20 ile 35 arasında olan oyuncuların adı, takımı, yaş bilgilerini ve yaş bilgisine göre çoktan aza sıralayacak şekilde ekrana basın
# print(
#     df[
#         df['Age'].between(20, 50)
#     ]
#     [['Name', 'Age', 'Team']]
#     .sort_values(by='Age', ascending=False)
# )


# İsmi içerisinde 'and' ifadesi geçen oyuncuları listeleyen bir custom function yazın.
# bu fonksiyonu dataframe uygulayın
def str_find(name: str):
    if 'and' in name.lower():
        return True
    else:
        return False


print(df[df['Name'].apply(str_find)])