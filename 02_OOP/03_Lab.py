

# Kalıtım
# Nasil ki biyolojide olduğu gibi bizler anne ve babalarımızdna kalıtım vasıtasıyla özellikler kazandıysak yazılımda da üst sınıflar (base class) vasıtasıyla alt sınıflara (child class) özellik atratabiliyoruz. Burada ki amaç alt sınıfların ortak özelliklerinin bir ata sınıfta toplanmasıdır. Kod tekrarını engeleyerek merkezi bir yerden yani atadan özellikler alt sınıflara aktarılırlar. Ayrıca üst seviyeli yazıllım prensiplerine ve tasarım desenlerine uymak için atılması gereken adımlarlarda biridir.

# class Human:
#     def __init__(self, height: float, weight: float, alias: str):
#         self.alias = alias
#         self.weight = weight
#         self.height = height
#
#     def show_information(self):
#         return self.__dict__
#
#
# class Knight(Human):
#     pass
#
#
# class Rogue(Human):
#     pass
#
#
# k1 = Knight(height=1.84, weight=98, alias='beast')
# print(dir(k1))
# print(k1.show_information())
# r1 = Rogue(height=1.50, weight=65, alias='hıhız')
# print(r1.show_information())


# Employee objesi için CRUD operasyonları yapalım
# BaseEntity => Projelerde diğer tüm sınıflara kalıtım veren sınıftır.
from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum


employees = []


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self, first_name: str, last_name: str, departmant: str):
        self.departmant = departmant
        self.last_name = last_name
        self.first_name = first_name
        self.id = str(uuid4())
        self.status = Status.Active.name
        self.create_date = datetime.now()
        self.created_ip_address = gethostbyname(gethostname())
        self.created_machine_name = gethostname()


class Employee(BaseEntity):
    pass


class Employee_Serivce:
    def create(self, employee: Employee):
        employees.append(employee)
        print(f'{employee.first_name} {employee.last_name} has been created..!')

    def get_all(self):
        for item in employees:
            print(f'{item.__dict__}')

    def get_by_full_name(self, full_name: str):
        for employee in employees:
            if f'{employee.first_name} {employee.last_name}'.lower().__contains__(full_name):
                print(employee.__dict__)


    def get_not_passive(self):
        for employee in employees:
            if employees.status == 'Active' or employee.status == 'Modifed':
                print(employee.__dict__)


def main():
    service = Employee_Serivce()
    while True:
        process = input('Type process: ')

        match process:
            case 'create':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                departmant = input('Departmant: ')
                employee = Employee(first_name=first_name, last_name=last_name, departmant=departmant)
                service.create(employee)
            case 'get all':
                service.get_all()
            case 'get by name':
                full_name = input('Full Name: ')
                service.get_by_full_name(full_name)



main()