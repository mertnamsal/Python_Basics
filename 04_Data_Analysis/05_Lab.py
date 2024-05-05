import pandas as pd

df = pd.read_csv('data/youtube-ing.csv')
print(df.shape)


# en çok görüntülenemye sahip ilk 10 farklı videonun title ve views sütunlarını ekrana basın
# print(
#     df.groupby(by='title')[['views']]
#     .sum(numeric_only=True)
#     .sort_values(by='views', ascending=False)
#     .head(10)
# )

# categorilerine göre likes ortalamasını bulun
# print(
#     df.groupby(by='category_id')[['likes']]
#     .mean(numeric_only=True)
#     .sort_values(by='likes', ascending=False)
#     .head(10)
# )

# hangi kanal ne kadar yorum almış
# print(
#     df.groupby(by='channel_title')[['comment_count']]
#     .sum(numeric_only=True)
#     .sort_values(by='comment_count', ascending=False)
#     .head(10)
# )


# her bir video için kullanılan tag sayısını tag_count isimli yeni bir sütun yaratalım
# title ve tag_count ekrana basalım
# custom function yazıyorum
# Path-I
# def calculate_tag_amount(tag: str):
#     return len(tag.split('|'))


# df['tags_count'] = df['tags'].apply(calculate_tag_amount)

# print(df[['title', 'tags_count']].sort_values(by='tags_count', ascending=False))

# Path-II (lambda expression)
# df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))
# print(df[['title', 'tags_count']])


# Her bir videonun like ve dislike oranlarını bulalım
# like_avg isimli yeni bir sütuna yazalım
# yazacağımız function argüman olarak ver setini alcak
def like_dislike_avg(data_set: pd.DataFrame) -> list:
    """
    This function calculate like avarage upon given data set
    :param data_set: pandas.core.DataFrmae
    :return: list
    """
    like_list = list(data_set['likes'])
    dislike_list = list(data_set['dislikes'])

    comb_list = list(zip(like_list, dislike_list))
    avg_list = []
    for like, dislike in comb_list:
        if like + dislike == 0:
            avg_list.append(0)
        else:
            avg_list.append(like / (like+dislike))

    return avg_list


df['like_avg'] = like_dislike_avg(df)

# yukarıda elde ettiğimiz like_avg sütununu kullanarak bir sotgu yazalım
print(df.sort_values(by='like_avg', ascending=False)[['title', 'likes', 'dislikes', 'like_avg']].to_string())