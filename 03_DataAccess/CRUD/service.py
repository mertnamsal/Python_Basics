
from abc import ABC, abstractmethod

import pymongo

from settings import collection
from pymongo.errors import ProtocolError
from bson.objectid import ObjectId
from pprint import pprint

class BaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass


class CategoryService(BaseService):
    def create(self, item: dict):
        pass
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
