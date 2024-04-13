
from abc import ABC, abstractmethod

import pymongo

from settings import collection
from pymongo.errors import ProtocolError, PyMongoError
from bson.objectid import ObjectId
from pprint import pprint

class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass

    @abstractmethod
    def update(self, filter_value: dict, set_value: dict): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        try:
            collection.insert_one(item)
            print(f'{item["name"]} has been created..!')
        except PyMongoError as err:
            print(err.__doc__)


    # region Read Operations
    # status ü active veya modified durumda olan kayıtları listele
    def get_all(self):
        projection = {
            '_id': 0,
            'name': 1,
            'description': 1
        }
        query = {
            '_BaseEntity__status': {
                "$in": ["Active", "Modified"]
            }
        }
        for item in collection.find(query,projection).sort(key_or_list='name', direction=pymongo.DESCENDING):
            pprint(item)

    def get_by_id(self, pk):
        # 1 gösterilmesini istediğimiz 0 istenilmeyen
        projection = {
            '_id': 0,
            'name':1,
            'description':1
        }
        query = {
            '_id': ObjectId(pk),
            '_BaseEntity__status': {
                "$in": ["Active", "Modified"]
            }
        }
        # sort() fonksiyonunda sıralama yaparken default asc dir
        for item in collection.find(query,projection).sort('name'):
            pprint(item)
    # endregion

    def update(self, filter_value: dict, set_value: dict):
        try:
            result = collection.update_one(
                filter_value,
                {
                    '$set': set_value
                }
            )
            print(f'{result.modified_count} amount record has been updated')

            self.get_by_id(filter_value['_id'])
        except PyMongoError as err:
            print(err.__doc__)
