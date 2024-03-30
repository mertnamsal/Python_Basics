
# Method overriding

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

# class Status(Enum):
#     Active = 1
#     Modified = 2
#     Passive = 3
#
#
# class BaseEntity:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#         self.id = str(uuid4())
#         self.status = Status.Active.name
#         self.create_date = datetime.now()
#         self.created_ip_address = gethostbyname(gethostname())
#         self.created_machine_name = gethostname()
#
#     def show_info(self):
#         print(f'Id: {self.id}\n'
#               f'Name: {self.name}\n'
#               f'Description: {self.description}')
#
# class Category(BaseEntity):
#     pass
#
# class Product(BaseEntity):
#     def __init__(self,name: str, description: str, price: float, stock: float):
#         super().__init__(name,description)
#         self.stock = stock
#         self.price = price
#
#     def show_info(self):
#         super().show_info()
#         print(f'Stock: {self.stock}\n'
#               f'Price: {self.price}')
#
# c1 = Category('Boxing Gloves', 'Best boxing gloves')
# c1.show_info()
# p1 = Product('Training Gloves','Best training gloves',12.2,34)
# p1.show_info()

# BasePhone adında bir ata sınıf oluşturalım. phone_id, brand, model, price attribute olsun
# show_info() olsun. phone_ring_sound() fonksiyonu 'genel telefon sesi' string ifadesini return
# Samsung adında bir sınıf oluşturalım. BasePhone dan kalıtım. operating_system attribute olsun. phone_ring_sound() ' samsung telefon sesi return etsin
# aynısını iphone ve huawei içinde

# class BasePhone:
#     def __init__(self,phone_id: float , brand: str, model: str, price: float):
#         self.price = price
#         self.model = model
#         self.brand = brand
#         self.phone_id = phone_id
#
#     def show_info(self):
#         print(f'Stock: {self.phone_id}\n'
#               f'Model: {self.model}\n'
#               f'Brand: {self.brand}\n'
#               f'Price: {self.price}')
#     def phone_ring_sound(self):
#         return 'genel telefon sesi'
#
#
# class Samsung(BasePhone):
#     def __init__(self, phone_id: int, brand: str, model: str, price: float, operation_system: str):
#         super().__init__(phone_id, brand, model, price)
#         self.operation_system = operation_system
#
#     def phone_ring_sound(self):
#         return 'Samsung telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.operation_system}')
#
# class Iphone(BasePhone):
#     def __init__(self, phone_id: float, brand: str, model: str, price: float, camera: str):
#         super().__init__(phone_id, brand, model, price)
#         self.camera = camera
#
#     def phone_ring_sound(self):
#         return 'Iphone telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.camera}')
#
# class Huawei(BasePhone):
#     def __init__(self, phone_id: float, brand: str, model: str, price: float):
#         super().__init__(phone_id, brand, model, price)
#
#     def phone_ring_sound(self):
#         return 'Huawei telefon sesi'
#
#
# s1 = Samsung(1,'Samsung','Galaxy 20',76.00,'Android')
# print(s1.phone_ring_sound())
# s1.show_info()
#
# i1 = Iphone(2,'Iphone','15 Pro Max',80.0, '5x')
# print(i1.phone_ring_sound())
# i1.show_info()