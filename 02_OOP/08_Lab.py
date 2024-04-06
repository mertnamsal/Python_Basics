
# Dünyanın faklrı lokasyonlarından kahve çekirdeği ithal edeceğiz
# Lakin kahve çekirdeklerinin lezzeti ve kalitesi açısından hasat zamanlarına göre ithal edeceğiz
# 4-7 ayalar arasında Columbia
# 8-11 aylar arasında Sumatra
# 1 yada 2 yada 12 ay SouthAfrice
# 3. ayda dünyada hasat olmadığı ithalat işlmei olmayacak


from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def ship_from(self) -> str: pass

    # Not: SOyut sınıflar staticmethod barındırabilirler
    @staticmethod
    def hello(self):
        print('fsf')


class SumatraService(BaseService):
    def ship_from(self) -> str:
        return 'from Sumatra'


class ColumbiaService(BaseService):
    def ship_from(self) -> str:
        return 'from Columbia'


class SouthAfrica(BaseService):
    def ship_from(self) -> str:
        return 'from SouthAfrica'


class DefaultService(BaseService):
    def ship_from(self) -> str:
        return 'shipment not avaliable'

# Bu örnekte size çaktırmadan Creational Design Patterns gruba ait olan factory design pattern kakaladım. Aşağıda shipment method fonskiyonu factory design pattern bize verdiği mantıkta çalışmaktadır.
class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseService:
        if 4 <= month <= 7:
            columbia_service = ColumbiaService()
            return columbia_service
        elif 8 <= month <= 11:
            sumatra_service = SumatraService()
            return sumatra_service
        else:
            if month == 1 or month == 2 or month == 12:
                southafrica_service = SouthAfrica()
                return southafrica_service
            else:
                default_service = DefaultService()
                return default_service


def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'Coffee beans shipment {product_shipment.ship_from()}')


main()
