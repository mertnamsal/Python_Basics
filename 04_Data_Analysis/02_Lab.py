
import pandas as pd
from os import path

# os (operation system) modülü ile aşağıda ki fonksiyon ile bir dosyanın tam yolunu  bulabiliriz.
print(path.abspath('imdb.csv'))
df = pd.read_csv('data/imdb.csv')

print(df.to_string())

# Movie_Title sütunun ilk 20 satırını df olarak ekrana basın
#Path 1
print(df[['Movie_Title']].head(20).to_string())
#Path 2
print(df[['Movie_Title']][0:20])
#Path 3
print(df.loc[:20,'Movie_Title'])

# Filtre ==> Rating 7.0 dan olan
# Select ==> Movie_title, Rating, YR_Relased
print(df[['Movie_Title','Rating','YR_Released']][df['Rating'] >= 7.0].sort_values('Rating'))

# YR_Released bilgisi 2014 ile 2018 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin

print(df[['Movie_Title', 'Rating', 'YR_Released']][(df['YR_Released'] > 2014) & (df['YR_Released'] <= 2018)].sort_values('YR_Released'))

#Num_Revies 100'den büyük yada Rating 8 ile 9 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin

print(df[['Movie_Title','Rating','YR_Released']][(df['Rating'] > 8) & (df['Rating'] < 9)].sort_values('Rating'))
