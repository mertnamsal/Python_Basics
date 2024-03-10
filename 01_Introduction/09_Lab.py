
from pprint import pprint
from requests import get

response = get('https://newsapi.org/v2/everything?q=tesla&from=2024-02-10&sortBy=publishedAt&apiKey=52a12867f8c04e1d9bc5a3bc84bae886')

data = response.json()

# pprint(data.get('articles')[0].get('title'))
# for i in range (len(data.get('articles'))):
#     pprint(data.get('articles')[i])

# Kullanıcıdan yazar ismi alınacak ve bu yazarın makalesini ekrana basılacak
# yazar_ismi = input("Yazar ismi : ")
# for article in data.get('articles'):
#     if article.get('author') == yazar_ismi:
#         print(article.get('content'))

#Free api bulup data çekiyoruz Search mekanizması yapın
#Örneğin BIST datası çektiniz SASA search edildiğinde ekrana bilgileri basılacak
response_currency = get('https://api.currencyapi.com/v3/latest?apikey=cur_live_p1bNgm05wqCjq3okO4VKoBGQVjbQvXLQMPb4MBHJ')
data_currency = response_currency.json();
pprint(data_currency)