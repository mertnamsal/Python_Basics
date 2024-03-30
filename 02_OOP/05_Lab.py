
#Encapsulation (Veri Gizleme)

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

class Status(Enum):
    Active = 1,
    Modified = 2,
    Passive = 3

class BaseEntity:
    def __init__(self):
        self.__id = '' ## iki tane __ varsa dış erişime kapalıdır
        self.__created_date = ''
        self.__created_computer_name = ''
        self.__created_ip_address = ''
        self.__status = ''

    # Not : double underscore ile tanımladığımız alanlara ne sınıfın örnekleminden ( instance) nede bu sınıfın
    # kalıtım alan alt sınıfın örnekleminden erişebiliyorum. Encapsule ettiğim alanlara sadece bu sınıfın yaşam alanından erişebiliyorum
    # custom metod yazararak değişiklik yapabiliyoruz

    def set_values_private_attribute(self):
        self.__id = uuid4()
        self.__created_date = datetime.now()
        self.__created_computer_name = gethostname()
        self.__created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name

    def show_information(self):
        return self.__dict__


# class Product(BaseEntity):
#     def __init__(self, name: str, description: str):
#         super().__init__()
#         self.description = description
#         self.name = name
#         self.__price = 0
#         self.__stock = 0
#
#     def set_value_product_attribute(self, price: float, stock:int):
#         super().set_values_private_attribute()
#         if price > 0 and stock >0:
#             self.__price = price
#             self.__stock = stock
#             print('Product has been created..!')
#             pprint(self.__dict__)
#         else:
#             print('Invalid input..!\n'
#                   'Products stock and price can not be negative value or zero...!')
#
#
# p1 = Product('Training gloves','best')
# p1.set_value_product_attribute(90.0,10)


class Car(BaseEntity):
    def __init__(self,brand: str, model:str):
        super().__init__()
        self.model = model
        self.brand = brand
        self.__price = 0
        self.__sase_no = 0

    def set_value_car_attribute(self, price):
        if price > 0:
            super().set_values_private_attribute()
            self.__sase_no = uuid4()
            self.__price = price
            print('Car has been created..!')
            pprint(self.__dict__)


c1 = Car('Dodge','TRX 4810')
c1.set_value_car_attribute(35.000)