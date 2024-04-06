

# Method Overriding
# Ata sınıflarda (parent class) bulunan methodların alt sınıflarda ezilerek onlara yeni işlevler kazandırılmasına method overriding diyoruz. Ata sınıftan gelen fonksiyonun illa var olan yeteneğini geçersiz kılıp ona yeni yetenek kazandırmaya gerek yoktur. Bazen var olan yetenek extend edilebilinir.

# from uuid import uuid4
# from datetime import datetime
# from socket import gethostname, gethostbyname
# from enum import Enum
# from pprint import pprint
#
#
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
#
# class Category(BaseEntity):
#     pass
#
#
# class Product(BaseEntity):
#     def __init__(self, name: str, description: str, price: float, stock: float):
#         super().__init__(name, description)
#         self.stock = stock
#         self.price = price
#
#     def show_info(self):
#         super().show_info()
#         print(f'Stock: {self.stock}\n'
#               f'Price: {self.price}')
#
#
# c1 = Category('Boxing Gloves', 'Best boxing gloves')
# c1.show_info()
# p1 = Product('Training Gloves', 'Best training gloves', 12.2, 34)
# p1.show_info()


# BasePhone adında bir ata sınıf oluşturalım. phone_id, brand, model, price attribute'leri olsun.
# show_info() fonksiyonu olsun. phone_ring_sound() fonksiyonu 'genel telefon sesi' string ifadesini return
# Samsung adında bir sınıf oluşturalım. BasePhone kalıtım alacak . operatiog_system attribute olsun. phone_ring_sound() 'samsung telefon sesi' return etsin
# Iphone adında bir sınıf oluşturalım. BasePhone kalıtım alacak. camera attribute olsun. phone_ring_sound() 'iphone telefon sesi' return etsin
# Huaweie adında bir sınıf oluşturalım. BasePhone kalıtım alacka. anten attribute olsun. phone_ring_sound() 'huawie telefon sesi' return etsin

# class BasePhone:
#     def __init__(self, phone_id: int, brand: str, model: str, price: float):
#         self.price = price
#         self.model = model
#         self.brand = brand
#         self.phone_id = phone_id
#
#     def show_info(self):
#         print(f'Id: {self.phone_id}\n'
#               f'Model: {self.model}\n'
#               f'Brand: {self.brand}\n'
#               f'Price: {self.price}')
#
#     def phone_ring_sound(self):
#         return f'Genel telefon sesi'
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
#
# class Iphone(BasePhone):
#     def __init__(self, phone_id: int, brand: str, model: str, price: float, camera: str):
#         super().__init__(phone_id, brand, model, price)
#         self.camera = camera
#
#
#     def phone_ring_sound(self):
#         return 'Iphone rişng sound'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.camera}')
#
#
# s1 = Samsung(1, 'Samsung', 'Galaxy 20', 76.00, 'Android')
# s1.show_info()
# print(s1.phone_ring_sound())
#
# i1 = Iphone(2, 'Iphone', '15 Pro Max', 89.89, '5x')
# i1.show_info()
# print(i1.phone_ring_sound())


# BaseBill sınıfımız olsun. bill_name, value_add_task, amount attribute sahip olsun. calculate_bill ve create_log fonksiyonları olsun.
# log'lar bill_info.txt dosyasına yazılsın. bill_name ve total_amount yazmanız ve tarih yeterli
# calculate_bill() amount * value_add_task
# Water_Bill, Electricity_Bill, Natural_Gas_Bill child classes
# su faturasının mill adında bir özelliği olsun.
# elektrik kw adında bir özelliği olsun.
# doğalgaz m3 adında bir özelliği olsun.
from datetime import datetime


class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.amount = amount
        self.value_add_task = value_add_task
        self.bill_name = bill_name

    def calculate_bill(self):
        return self.amount * self.value_add_task

    def create_log(self):
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Bill Name: {self.bill_name}\n'
                       f'Total Amount: {self.calculate_bill()}\n'
                       f'Create Date: {datetime.now()}')


class Electricty_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return super().calculate_bill() * self.kw


class Water_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

    def calculate_bill(self):
        return super().calculate_bill() * self.mill


class Naturel_Gas_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return super().calculate_bill() * self.m3


electricy = Electricty_Bill('BEDAŞ', 45.6, 190.1, 12.3)
electricy.create_log()

water = Water_Bill('Iski', 45.7, 123.5, 45)
water.create_log()

gas = Naturel_Gas_Bill('IGDAŞ', 45.6, 123.4, 56)
gas.create_log()

