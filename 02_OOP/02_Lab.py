
# CRUD
# categories = {}
# Category adında bir sınıfımız olsun name, description object attr
# Category_Service adında bir sınıfımız olsun. Bu sınıf içerisinde CRUD operasyonlarını yürütürken ihtiyaç duyulan fonksiyonlar yazılsın.
# Service de create ,update, delete , get all , get by id olsun

from uuid import uuid4
from pprint import pprint

categories = {}

class Category:
    def __init__(self, name:str, description: str):
        self.name = name
        self.description = description
        self.id = uuid4()


class Category_Service:
    def create(self, cateogry: Category):
        categories[str(cateogry.id)] = {
            'name': cateogry.name,
            'description': cateogry.description
        }
        print(f'{cateogry.name} has been created..!')

    def get_all(self, db: dict) -> None:
        pprint(db)

    def get_by_id(self, id: str) -> dict:
        for i in categories.keys():
            if i == id:
                return categories.get(id)
    def update(self, id: str, name: str, description: str):
        self.get_by_id(id)

def main():
    while True:
        service = Category_Service()
        process = input('Please type a transaction name: ').lower()

        match process:
            case 'exit':
                print('Application has been closing..!')
                break
            case 'create':
                category_name = input('Category name: ')
                category_description = input('Description: ')
                category_obj = Category(name=category_name, description=category_description)
                service.create(category_obj)
                service.get_all(categories)
            case 'get all':
                service.get_all(categories)
            case 'get by id':
                id = input('Id: ')
                pprint(service.get_by_id(id))


main()

