

from models import Category
from bson.objectid import ObjectId
from service import CategoryService

service = CategoryService()

# service.get_all()

# pk = input('Pk : ')
# service.get_by_id(pk)

# name = input('Name: ')
# description = input('Description: ')
#
# new_category = Category(name,description)
#
# service.create(new_category.__dict__)

# id = input('Id: ')
# name = input('Name: ')
# description = input('Description: ')
#
# filter_value = {
#     '_id': ObjectId(id)
# }

# set_values = {
#     'name': name,
#     'description': description,
#     '_BaseEntity_status': 'Modified'
# }
#
# service.update(filter_value, set_values)

id = input('Id: ')

filter_value = {
    '_id': ObjectId(id)
}

set_values = {
    '_BaseEntity_status': 'Passive'
}

service.update(filter_value, set_values)