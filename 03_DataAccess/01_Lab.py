import re

# MongoDB erişim
from pymongo import MongoClient
from pprint import pprint

# App den server a erişmek için connection
conn = MongoClient('mongodb://localhost:27017')

# Server üzerinde bir veritabanı yaratlım
db = conn['app_db']

#Veri tabanı içerisine bir collection
collection = db['products']

# region Insert one record
# product_name = input('Name: ')
# price = input('Price: ')
# product = {
#     'name': product_name,
#     'price': price
# }
# result = collection.insert_one(product)
# print(result)
# endregion

# region Insert Many Record
# product_list = [
#     {'_id': 1, 'name': 'Lenovo X1', 'price': 84.999},
#     {'_id': 2, 'name': 'Macbook Pro', 'price': 184.999},
#     {'_id': 3, 'name': 'Asus Zenfone 2', 'price': 144.999},
#     {'_id': 4, 'name': 'Samsung S22', 'price': 60.999},
#     {'_id': 5, 'name': 'Monster Alba', 'price': 30.999},
# ]
# collection.insert_many(product_list)
# endregion

# region Read All Data
# for x in collection.find():
#     print(x)
# endregion

# region Fiyatı 100binden fazla olan ürünleri listeleme
# filter_input = {
#     "price": {
#         "$gt": 100.000
#     }
# }
# for x in collection.find(filter_input):
#     print(x)
# endregion

# region Fiyatı 80inden aşağı ve eşit olan ürünleri listeleme
# filter_input = {
#     "price": {
#         "$lte": 80.000
#     }
# }
# for x in collection.find(filter_input):
#     pprint(x)
# endregion

# region Fiyatı 60.999 a eşit olan ürünleri listeleme
# filter_input = {
#     "price": {
#         "$eq": 60.999
#     }
# }
# for x in collection.find(filter_input):
#     pprint(x)
# endregion

# region Fiyatı 20 bin ile 100 arasında olan ürünleri listeleme
# filter_input = {
#     "price": {
#         "$gt": 20.000,
#         "$lt": 100.000
#     }
# }
# for x in collection.find(filter_input):
#     pprint(x)
# endregion

# region Fiyatı 70binden az ve ürün adı içerisinde monster olan ürünleri listeleme
# filter_input = {
#     'price': {'$lte': 70.000},
#     'name': {'$regex': 'Monster'}
# }
# for x in collection.find(filter_input):
#     pprint(x)
# endregion

# region Baş harfli L olan ürünleri listele
# pattern = re.compile('^L.*')   # (^) başlangıç için
#
# query = {
#     'name': {'$regex': pattern}
# }
# for x in collection.find(query):
#     pprint(x)
# endregion

# region Update
result = collection.update_one(
    #güncellemek istediğimiz kaydı yakalıyoruz
    {'name':'Monster ALba'},
    # yeni değeleri kayıt alanlarına set ediyoruz.
    {
        '$set':{
            'name': 'Dell Vega',
            'price': 68.888
        }
    }
)

print(f'{result.modified_count} adet kayıt güncellendi')