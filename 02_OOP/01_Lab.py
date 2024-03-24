# class Vehicle:
#     #attribute
#     door_number = 0
#     brand = ''
#     model = ''
#     engine_size = 0
#     torque = 0
#
#
# x = Vehicle()
# x.brand = 'Mercedes'
# x.model = 'C'
# x.engine_size = 5
# x.torque = 4
# print(f'Brand {x.brand}')
#
# y = Vehicle()
# y.brand = 'Ford'
# y.model = 'Shelby'
# y.door_number = 4
# y.engine_size = 6
# y.torque = 5

# __init__() fonksiyonu ilgili sınıfı başlatmaya (initialize) etmeye yaramaktadır. Bir başka değiş ile sınıfımızı kullanılma hazırlamaktadır.
# Ram in heap alanına çıkarmaktadır.

class Boxer:
    def __init__(self, first_name, last_name, age):
        # aşağıda ki "adi" ve "soyadi" attribute'leri için object attribute denir
        self.adi = first_name
        self.soyadi = last_name
        self.yas = age
        # self sınıfı temsil eder


# boxer_1 = Boxer(first_name='Mike', last_name='Tyson', age=75)
# print(dir(Boxer))
# print(dir(boxer_1))
# boxer_2 = Boxer(first_name='Mahmud', last_name='Tyson', age=57)
# print(dir(boxer_2))

# Circle isminde bir sınıf yaratlım
# pi adında class attribute olsun
# r adında bir object attribute olsun
# alan ve çevre hesaplama fonksiyonları olsun

# class Circle:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.r = r
#
#     def calculate_area(self):
#         return self.pi * self.r**2
#
#     def calculate_perimeter(self):
#         return 2*self.r*self.pi

# yari_cap = float(input('Yarı çap: '))
# c1 = Circle(yari_cap)
# print(f'Çevre: {c1.calculate_perimeter()}')
# print(f'Alan: {c1.calculate_area()}')

# Departmant adında bir sınıf oluşturalım
# departmant_name ve employee_count class attribute
# name, age object attribute
# show_information() olsun
# show_employee_count() fonksiyonu olsun. Departmant sınıfından
# her instance alındığında employee_count 1 arttırılsın ve bu arttırma işleminin sonucu ekrana yazdıralım

# class Departmant:
#     departmant_name = 'Software Developer'
#     employee_count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Departmant.employee_count += 1
#         self.show_information()
#         self.show_employee_count()
#
#     def show_information(self):
#         print(f'Name: {self.name} '
#               f'Age: {self.age} '
#               f'Departmant: {self.departmant_name}\n')
#
#     def show_employee_count(self):
#         print(f'Total Employee: {self.employee_count}')
#
#
# e1 = Departmant('burak', 35)
# e2 = Departmant('hakan', 38)
# e3 = Departmant('ipek', 40)

# Software Developer adında bir sınıf yaratalım
# first_name, last_name object attribute olsun
# knowledge_language = [] class attribute
# show_info()
# add_new_language() yeteneği olsun. Lakin bazen bir dil bazen birden fazla dil girebilsin
#example input => python
#example input => python, c#, vb

# class SoftwareDeveloper:
#     knowledge_language = []
#
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def show_info(self):
#         print(f'Name : {self.first_name}  LastName : {self.last_name} languages: {self.knowledge_language}')
#
#     def split_language(self, input_language: str) -> list:
#         return input_language.split(',')
#
#     def add_new_language(self,lst_language: list) -> None:
#         for item in lst_language:
#             self.knowledge_language.append(item.lstrip())
#
#
# s1 = SoftwareDeveloper(first_name='Burak',last_name='Yılmaz')
# language = input('Type programming language: ')
# language_list = s1.split_language(language)
# s1.add_new_language(language_list)
# s1.show_info()

from random import choice
class Character:
    def __init__(self, name: str, race: str, role: str, level: int, weapon: int,armour: int, hp: int):
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.level = level
        self.role = role
        self.race = race
        self.name = name

    def attack(self):
        return self.level * self.weapon

    def defend(self):
        return self.level * self.armour

    def dodge(self):
        print('Player has dodged..!')

def main():
    c1 = Character(name='Kara Murat', race='Turk', role='Kahraman', level=100, weapon=100, armour=1, hp=100)
    c2 = Character(name='Kostok', race='Bizans', role='Kral', level=50, weapon=20, armour=100, hp=100)

    while True:
        bot_actions = [c2.attack(), c2.defend(), c2.dodge()]

        bot_action = choice(bot_actions)

        c1_action = input('Type action: ')

        match c1_action:
            case 'attack':
                c2.hp -(c2.defend() -c1.attack())
            case 'defend':
                pass
            case 'dodge':
                pass
            case _:
                pass