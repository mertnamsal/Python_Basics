# Abstraction (Soyutlama)
# OOP yapıları arasında en önemlisidir.
# Üst seviyeli yazılım prensiplerine ve tasarım desenlerine uymak istiyorsak kod bloklarımızda soyutlama muhakak olmalıdır. Soyutlama ile amaçlanan ana mantık şudur: ata sınıfları soyut yaparak alt sınıflara kural koymak. Bir başka değiş ile ata sınıf ile alt sınıf arasında kontrat yada sözleşme imzalıyoruz. Gerçek hayatta nasıl kontrat bozulamazsa yazılımda da bozulamaz.


# Soyutlamaya geçmeden önce öğrenmemiz gerekn 1-2 husus bulunmaktadır. BUnlardan 1. decorator bir diğeri ise meta class

# region Decorator
# python programalama dilinde kullanılan bir keyword'tür. Bir fonksiyonu bir decorator ile var olan yeteneği üzerine bir yetenek daha ekleyebiliriz. Methodlarımızı yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluyoruz. Python'da bulilt-in bir çok decorator vardır. bunlardan bazıları @abstractmethod, @static, @property vb. tabi ki custom decoretor yazılabilinir.
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
#     return 'mike tyson'
#
#
# print(uppercase_name(get_fullname))
#
#
# @uppercase_name
# def get_name():
#     return 'burak yılmaz'
#
#
# print(get_name)
# from math import pow, factorial
# from time import sleep, time
#
#
# def calcaulate_time_execute(func):
#     def inner_func(*args, **kwargs):
#         start_time = time()
#         sleep(10)
#         func(*args, **kwargs)
#         finis_time = time()
#         print(f'===============\n'
#               f'Process Name: {func.__name__}\n'
#               f'Start Time: {start_time}\n'
#               f'End Time: {finis_time}')
#
#     return inner_func
#
#
# @calcaulate_time_execute
# def us_alma(a: int, b: int):
#     print(f'Sonuç: {pow(a, b)}')
#
#
# @calcaulate_time_execute
# def faktoriyel_hesaplama(number: int):
#     print(f'Sonuç: {factorial(number)}')
#
#
# @calcaulate_time_execute
# def toplama(x: int, y: int, z: int):
#     print(f'Sonuç: {x + y + z}')
#
#
# us_alma(2, 3)
# faktoriyel_hesaplama(5)
# toplama(3, 4, 5)
# endregion


# region metaclass
# Python'da metaclas, başka sınıfların yaratmak için kullanılan bir sınıftır. Bir sınıf kendi instance'nın nasıl davaranacağını tanımlar, lakin metaclass bir sınıfın nasıl davaranağını tanımlar. Genellikle sınıf oluşturma davranışını özelliştirme ve sınıfın otomataik olarak hangi özel fonksiyonlara sahip olacağını belirlemek için kullıyoruz.
# endregion


# region Abstraction Example 1
from abc import ABC, abstractmethod


class BaseMuzikAleti:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand


class Gitar(BaseMuzikAleti):
    def __init__(self, brand, model, tel):
        super().__init__(brand, model)
        self.tel = tel


class Keman(BaseMuzikAleti):
    def __init__(self, brand, model, kasa):
        super().__init__(brand, model)
        self.kasa = kasa


class Muzisyen:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.caldigi_enstrumanlar = []


# BaseService sınıfımız ABC meta sınfından kalıtım alarak artık soyut sınıf özelliğine kavuşmuştur.
class BaseService(ABC):

    # Abstract bir sınıf içerisinde herhangi bir methodu "@abstractmethod" decoratörü ile işaretlersem bu method soyut bir method artık soyut bir method olmuştur.
    # Abstract olarak işaretlenmiş bir fonksiyonun gövdesi olmaz yani ilgili fonksiyona bir business logic yüklenmez. Bu bağlamda aşağıdaki methodu "pass" diyerek ona gövde atamadık.
    # Neden abstact methodlara gövde yazılmaz?
    # Çünkü abstaract olarak işaretlenmiş methodlar alt sınıflarda override edilmeye zorunludur. Bu zorunluk dün konuştuğumuz konrat mevzusudur.
    # Zaten aşağıdaki method alt sınıflarda override edilmeye zorunlu olduğu için burada gövde vermek mantıksızdır.
    @abstractmethod
    def call_sound(self) -> str: pass

    # Abstract sınıf içerisinde abstract olmayan methodlar barındırılabilinir. Bu methodlar override edilmeye zorunlu değildir. Alt sınıfta ihtiyaca göre override edilirler yada edilmezler.
    def hello_everone(self):
        print('Hi')

    # Burada tanımlanan soyut method alt sınıflarda değiştirilemez. Yani bir var olan argümanlarına yenisi eklenemez yada argüman yoksada yeni bir argüman eklenemez.
    # Bu değiştirilemez özelliğini düşündüğümzde aklımaza OCP (Open Closed Principle) yazılım prensibi gelmektedir. Bu prensip bize değişime kapalı geliştirmeye açık sınıflar yaratmamızı salık verir.
    @abstractmethod
    def harmonize(self) -> str: pass


class GitarService(BaseService):

    def harmonize(self) -> str:
        return 'Akord edilidi'

    def call_sound(self) -> str:
        return 'Gitar sesi'

    # Alt sınıfların ihtiyaçlarına göre kendine has methodları olabilir. Lakin başka yaklaşımları bozmamak için genel olarak ataya yazılarak override edilmesi tercih edilir.
    def salve(self):
        print('fsdfds')


class KemanService(BaseService):

    def call_sound(self) -> str:
        return 'Keman sesi'

    def harmonize(self) -> str:
        return 'Akord edildi'

    # Bu methodu ister override ederim istersem etmem çünü ata sınıfta soyut olarak işaretlenmedi
    def hello_everone(self):
        print('Kimseyi selemlamak istemiyorum..!')


def main():
    gitar_serivce = GitarService()
    keman_service = KemanService()

    gitar = Gitar('Fender', 'Classical Gitar', 'Kaliteli Tel')
    keman = Keman('Godrigez', 'Clasical', 'Meşe')

    muzisyen = Muzisyen('Burak', 'Yılmaz')
    muzisyen.caldigi_enstrumanlar.append(gitar)
    muzisyen.caldigi_enstrumanlar.append(keman)

    print(f'Ad: {muzisyen.first_name}\n'
          f'Soyad: {muzisyen.last_name}\n'
          f'Çaldığı Enstrüman: {muzisyen.caldigi_enstrumanlar[0].brand}\n'
          f'Çaldığı Enstrüman: {muzisyen.caldigi_enstrumanlar[0].model}\n'
          f'Çıkardığı Ses: {gitar_serivce.call_sound()}\n'
          f'Akor Edildi: {gitar_serivce.harmonize()}')


main()
# endregion
