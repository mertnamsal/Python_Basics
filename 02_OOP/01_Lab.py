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

class Departmant:
    departmant_name = 'Police'
    employee_count = 250

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Departmant.employee_count += 1
        self.show_information()

    def show_information(self):
        print(f'Name: {self.name} Age: {self.age}')

    def show_employee_count(self):
        return self.employee_count


police = Departmant('ahmet', 35)
print(f'Employee Count: {police.employee_count}')
