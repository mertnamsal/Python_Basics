

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies_df = pd.read_csv('data/movies.csv')
rating_df = pd.read_csv('data/ratings.csv')


# region Task 1
# movies_df içerisinde ki title sütununda yılı bilgisini parantezleriyle birlikte söküp alalım bir başka değiş ile silelim
# year sütünu açarak parantezsiz bir şekilde yeni sütuna yazalım
# regex kullanalım
# Step 1: title sütununda bulunan yıl bilgisini söküp yeni bir sütuna yazdık. Örneğin Toy Story (1989) bilgisinden (1989) extract ederek onu 'year' isimli sütuna yazdık.
movies_df['year'] = movies_df.title.str.extract(pat=r'(\W{1}\d{4}\W{1})', expand=False)
# Step 2: year sütunu içerisinde bir önceki adımdan (1989) vb bilgiler oluştu. Bu adımda da parantezlerden kurtulduk
movies_df['year'] = movies_df.year.str.extract(pat=r'(\d{4})', expand=False)
# Step 3: title sütununda bulunan Toy Story (1989) vb bilgilerde ki (1989) bilgisi yerine boşluk karakteri yerleştirelim
movies_df['title'] = movies_df['title'].str.replace(pat=r'(\W{1}\d{4}\W{1})', repl=' ', regex=True)
# movies_df['title'] = movies_df['title'].replace(to_replace=r'(\W{1}\d{4}\W{1})', value=' ', regex=True)
# Step 4: title sütununda bulunan Toy Story (1989) vb bilgilerde ki (1989) bilgisi yerine boşluk karakteri bastık bir önceki adımda şimdi oluşan boşlukları silelim (lambda kullanın)
movies_df['title'] = movies_df['title'].apply(lambda x: x.rstrip())
# print(movies_df.head().to_string())
# endregion

# region Task 2
# movies_df'in bir kopyasını tutun.
movies_genres_df = movies_df.copy()  # movies_df kopyasını oluşturdum
# endregion

# region Task 3
# genre listesi oluşturalım ama her bir tür bir kez içerisinde bulunacak
movies_genres_list = []
for index, column in movies_df.iterrows():
    for i in column["genres"].split('|'):
        movies_genres_list.append(i)

unique_genres = np.unique(movies_genres_list)
unique_genres = np.delete(unique_genres, [0])
# endregion


# region Task 4
# yukarıd elde ettiğimi listenin her bir item'ı için movies_genres_df içerisinde bir sütun yaratın sütunların değerlerine NaN basın
# pandas içerisinde assign() fonksiyonu kullanın
movies_genres_df = movies_genres_df.assign(**{col: np.nan for col in unique_genres})
# print(movies_genres_df.head().to_string())
# print(movies_genres_df.shape)
# endregion


# region Task 5
# yeni yarattığımız ayrı ayrı tür sütunlrına, film bir türe sahip ise 1 değilse 0 basın
for index, column in movies_df.iterrows():
    for genre in column["genres"].split('|'):
        movies_genres_df.loc[index, genre] = 1

movies_genres_df.fillna(0, inplace=True)
# print(movies_genres_df.head().to_string())
# endregion


# region Task 6
user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Father of the Bride Part II', 'rating': 5},
    {'title': 'Heat', 'rating': 1},
    {'title': 'Space Jam', 'rating': 5},
])
# Yukarıda sisteme yeni üye olmuş kullanıcının rate ettiği filmlerin datası var.
# bu veri setinde filmlerin id'leri genres ları bulunmamaktadır. bu bilgilerinde olacağı bir df oluşturalım
merged_df = pd.merge(user_input_df, movies_df, on='title')
# print(merged_df.to_string())

# türleri ==> Comedy|Drama|Romance olan Heat filmi dışındaki Heat filmlerini silin. yani year 1972 olan Heat kalacak
merged_df.drop(index=[3, 5], axis=0, inplace=True)

# genres ve year sütunlarından kurtulalım
merged_df.drop(labels=['genres', 'year'], axis=1, inplace=True)

# yukarıda ki index silme işlemi yüzünden index bozuldu merged_df in index'leirni sıfırlayın
merged_df.reset_index(drop=True, inplace=True)
# print(merged_df.to_string())
# endregion


# region Task 7
# user'in rate ettiği filmlerin id'lerini yukarıda saptadık. şimdi bu filmlerin sahip oldukları türlerin veri setini oluşturalım
user_favorite_genres = pd.merge(merged_df, movies_genres_df, on='movieId')
user_favorite_genres.drop(['title_y', 'year', 'title_x', 'rating', 'movieId', 'genres'], axis=1, inplace=True)
# print(user_favorite_genres.to_string())
# endregion


# region Task 8
# user_profile series oluştun
user_profile = user_favorite_genres.transpose().dot(user_input_df['rating'])
# print(user_profile)
# endregion


# region Task 9
# movie_matrix oluşturalım
movie_matrix = movies_genres_df.drop(labels=['title', 'genres', 'year'], axis=1)
movie_matrix.set_index('movieId', inplace=True)
# endregion

# region Task 10
# recomendation matrix oluşturalım
# filmlerin ağırlık ortalamasını bulduk
recomandation_matrix = pd.DataFrame(
    (movie_matrix * user_profile).sum(axis=1) / user_profile.sum()
)
recomandation_matrix.columns = ['Weighted Avarage']
# print(recomandation_matrix.sort_values(by='Weighted Avarage', ascending=False).head().to_string())
result_df = pd.merge(movies_df, recomandation_matrix, on='movieId')
result_df.sort_values(by='Weighted Avarage', ascending=False, inplace=True)
print(result_df.head().to_string())
# endregion


result_df.head(20).plot(
    x='title',
    y='Weighted Avarage',
    kind='bar'
)

plt.show()



