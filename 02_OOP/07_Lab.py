

from abc import ABC, abstractmethod
from datetime import datetime

# Not: Artık nesnelerimiz temsil eden sınıfların içerisine CRUD operasyonalrını temsil eden fonksiyonları yazmıyoruz. Nesne farklı bir sınıf crud operasynlarını içeren fonksiyonlar ise farklı bir sınıf olacak. BU bağlamda lab_04 teki fatura ödeme uygulmasını soyutlama ile ve yukarıdaki mantığa göre bir daha yapalım.


class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.bill_name = bill_name
        self.amount = amount
        self.value_add_task = value_add_task


class ELectrictyBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw


class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill


class NaturelGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3


class BaseService(ABC):

    @abstractmethod
    def calculate_bill(self, bill: BaseBill) -> float: pass

    def create_log(self, bill: BaseBill, result: float) -> None:
        with open(file='lab_07_bill_info', mode='a', encoding='utf_8') as file:
            file.write(f'Bill Name: {bill.bill_name} ||'
                       f'Total Amount: {result} ||'
                       f'Create Date: {datetime.now()}')


class WaterBillService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.amount * bill.value_add_task * bill.mill


class ElectrictyBillService(BaseService):
    def calculate_bill(self, bill: ELectrictyBill) -> float:
        return bill.amount * bill.value_add_task * bill.kw


class NaturelGasBillService(BaseService):
    def calculate_bill(self, bill: NaturelGasBill) -> float:
        return bill.amount * bill.value_add_task * bill.m3


water_bill = WaterBill('ISKI', 12.3, 34.5, 56.7)
water_service = WaterBillService()
result = water_service.calculate_bill(water_bill)
water_service.create_log(water_bill, result)