

from models import Category
from bson.objectid import ObjectId
from service import CategoryService

service = CategoryService()

# service.get_all()

# pk = input('Pk : ')
# service.get_by_id(pk)

name = input('Name: ')
description = input('Description: ')

new_category = Category(name,description)

service.create(new_category.__dict__)
