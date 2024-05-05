

import pandas as pd
from os import path

# os (operation system) modülü ile aşağıda ki fonksiyon ile bir dosyanın tam yolunu bulabiliriz.
# print(path.abspath('imdb.csv'))

df = pd.read_csv(filepath_or_buffer='data/imdb.csv', encoding='utf-8')
print(df.head().to_string())


# Movie_Title sütunun ilk 20 satırını df olarak ekrana basın
# Path-I
print(df[['Movie_Title']].head(20).to_string())
# Path-II
print(df[['Movie_Title']][0:20])
# Path-III
print(df.loc[:20, 'Movie_Title'])

# Filtre ==> Rating 7.0 'dan olan
# Select ==> Movie_Title, Rating, YR_Released
# 20 ile 50 satırları getirin
print(df[['Movie_Title', 'Rating', 'YR_Released']][df['Rating'] >= 7.0][20:50].sort_values('Rating', ascending=False))


# YR_Released bilgisi 2014 ile 2018 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin
# print(df[(df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2018)][['Movie_Title', 'Rating', 'YR_Released']])
print(df[df['YR_Released'].between(2014, 2018)][['Movie_Title', 'Rating', 'YR_Released']].sort_values('YR_Released', ascending=False))

# Num_Reviews 100.000'den büyük yada Rating 8 ile 9 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin
print(
    df[
        (df['Num_Reviews'] >= 100.000) | (df['Rating'] >= 8) & (df['Rating'] <= 9)
    ]
    [['Movie_Title', 'Rating', 'Num_Reviews']]
)

