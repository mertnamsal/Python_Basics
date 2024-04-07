from pymongo import MongoClient
from models import Category

conn = MongoClient('mongodb://localhost:27017')

db = conn['CRUD_db']

collection = db['categories']

# region Seed Data
# Proje ilk çalıştırıldığında veri tabanı yaratırılırken burada ki oluşturulan koleksiyon ile yani data ile yaratılmasına diyoruz.
# Bize sağladığı avantaj örneğin hemen read operasyonlarını hızlıca yazabiliriz. bir tane user yaratılmışsa login olunup belirli testler yapılabilir vs

# Uyarı: bu bloktaki kodları bir kez çalıştırdıktan sonra yoruma alın
# categories = [
#     Category('Gloves','Best gloves').__dict__,
#     Category('Shoes','Best shoes').__dict__,
#     Category('Tshirt','Best tshirt').__dict__,
# ]
#
# collection.insert_many(categories)
# endregion