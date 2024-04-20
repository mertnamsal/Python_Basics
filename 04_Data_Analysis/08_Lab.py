import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

# region Task 1
# xlsx formatındaki excel'in 'Canada by Citizienship' isimli sheet'i okuyoruz.
# ilk 20 satır ve son 2 satır okunmayacak.
df_can = pd.read_excel(
    'data/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20), # lambda x: x in x[0,20],
    skipfooter=2,
)
# print(df_can.head(10).to_string())
# endregion

# region Task 2
# OdName => Country
# AreaName => Continet
# RegName => Region
# Eski sütun isimlerini yenileriyle değiştiriniz
df_can.rename(columns={
    'OdName': 'Country',
    'AreaName': 'Continet',
    'RegName': 'Region'
}, inplace=True)
# print(df_can.head(10).to_string())
# endregion

#region Task 3
#AREA REG TYPE COVERAGE DEVNAME sütunlarını silin
df_can.drop(
    columns=['AREA','REG','Type','Coverage','DevName', 'DEV'],
    axis=1,
    inplace=True
)
# print(df_can.head(10).to_string())
# endregion

# region Task 4
# Soru 1: Sütun başlıklarının tiplerini ekrana basın
# for column in df_can.columns:
#     print(type(column))
# endregion

# Soru 2: Sütun başlıklarının hepsinin tipini string yapın
# map() => bize yenilebilir bir objedeki (list, tuple) her bir öğe için bir işlem execute eder. Aşağıda ki kullanımında yenilebilir onje df_can'in sütun başlıkları listesidir.
# Bu listede ki her bir itemö'in tipini string tipine map ediyoruz.
df_can.columns = list(map(str, df_can.columns))
# for column in df_can.columns:
#     print(type(column))
# endregion

# region Task 5
# veri setindeki var olan index yerine Country sütunun idnex olarak ayarlayalım
df_can.set_index(keys='Country', inplace=True)
# print(df_can.head(10).to_string())
# endregion

# region Task 6
# Yıl yıl göçmen sayılarını toplayarak total isili yeni bir sütuna yazdırın
df_can['Total'] = df_can.sum(axis=1,numeric_only= True)
# print(df_can['Total'])
# endregion

# region Task 7
# Veri setinde ki yılları baz alarak kendimize bir yıl listesi hazırlayalım lakin liste içerisinde ki yıl bilgileri string olsun
years = map(str,range(1980, 2014))
# print(df_can['Total'])
# endregion

# region Task 8
# En çok göç vermiş 5 ülkeyi bulun. df_top_five_country isimli df'e kayıt edin.
df_can.sort_values(by='Total',ascending=False,axis=0,inplace=True)
df_op_five_country = df_can.head()
print(df_op_five_country.to_string())
# print(df_can['Total'])
# endregion

# region Task 9
# Yukarıda oluşturulan df_top_five_country veri seti ile, year isimli listemizi kullanarak yılları satırlara ülkeleri sütunlara dönüştürerek bir df elde edin bu df'i df_top_five_country üzerine assigned edin

# print(df_can['Total'])
# endregion

