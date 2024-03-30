
# Abstraction (Soyutlama)
# ata sınıfıları soyut yaparak alt sınıflara kural koymaktır.

# Soyutlama geçmeden önce meta class ve decorator bilmeliyiz

#region Decorator
# python programlama dilinde kullanılan bir keyword. Bir fonksiyonu bir decorator ile var olan yeteneği üzerine bir yetenek
# daha ekleyebiliriz. Methodlarımızı yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluyoruz.
# Pythonda built-in bir çok decorator vardır. Bunlardan bazıları @abstractmethod, @static, @property vb.
# custom decorator yazılabilir
# def uppercase_name(function):
#     def inner_func():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return inner_func()
#
#
# def get_fullname():
#     return ('mike tyson')
#
# print(uppercase_name(get_fullname))
#
# @uppercase_name
# def get_name():
#     return 'mert namsal'
#
# print(get_name)
from math import pow,factorial
from time import sleep, time

#varargs bide calisma süresi
def calculate_time_execute():
    pass
def us_alma(a: int, b: int):
    print(f'Sonuc: {pow(a,b)}')

def faktoriyel_hesaplama(number: int):
    print(f'Sonuc: {factorial(number)}')

def toplama(x: int, y: int, z: int):
    print(f'Sonuc: {x+y+z}')


us_alma(2,3)
faktoriyel_hesaplama(5)
toplama(3,4,5)
#endregion