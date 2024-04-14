
import pandas as pd

df = pd.read_csv('data/nba.csv')

# En yüksek maaşı alan oyuncu kim

print(df[df['Salary'] == df['Salary'].max()][['Name','Salary']])

# Takımlara göre oyuncuların maaş ortalaması nedir?
result = df.groupby('Team')['Salary'].mean()
print(result)

# veri setinde kaç farklı takım var ( groupby ile yapılır ama başka bir fonksiyon daha var)
# bir sütunda ki biricik değerli nasıl sayarım
# groupby ile yaparsam satır sayarken null olan satırlarıda sayabilirim bu yüzden bu örneği groupby ile yapmak risklidir.
print(df['Team'].nunique())

#Yaşı 20 ile 35 arasında olan oyuncuların adı, takımı, yaş bilgilerini ve yaş bilgisine göre çoktan aza sıralayacak şekilde ekrana basın
print(
    df[
        (df['Age'] >= 20) & (df['Age'] <= 35) # df['Age'].between(20,50)
    ]
    [['Name','Age','Team']]
    .sort_values(by='Age',ascending=False)
)
# İsmi içerisinde 'and' ifadesi geçen oyuncuları listeleyen bir custom function yazxın
# bu fonskyionu dataframe uygulayın

def str_find(name: str):
    if 'and' in name.lower():
        return True
    else:
        return False


print(df[df['Name'].apply(str_find)])