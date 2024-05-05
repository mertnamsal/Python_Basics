

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


# region Task 1
# xlsx formatındaki excel'in 'Canada by Citizenship' isimli sheet'i okuyoruz.
# ilk 20 satır ve son 2 satır okunmayacak.
df_can = pd.read_excel(
    'data/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),  # lambda x: x in x[0:20],
    skipfooter=2
)
# print(df_can.head(10).to_string())
# endregion

# region Task 2
# OdName => Country
# AreaName => Continet
# RegName => Region
# Eski sütüun isimlerini yenileriyle değiştirin
df_can.rename(columns={
    'OdName': 'Country',
    'AreaName': 'Continent',
    'RegName': 'Region'
}, inplace=True)
# print(df_can.head(10).to_string())
# endregion


# region Task 3
# AREA, REG, Type, Coverage, DevName sütunlarını silin
df_can.drop(
    columns=['AREA', 'REG', 'Type', 'Coverage', 'DevName', 'DEV'],
    axis=1,
    inplace=True
)
# print(df_can.head(10).to_string())
# endregion


# region Task 4
# Soru 1: Sütun başlıklarının tiplerini ekrna basın
# for column in df_can.columns:
#     print(type(column))

# Soru 2: Sütun başlıklarının hepsinin tipini string yapın
# map() ==> bize yenilenebilir bir objedeki (list, tuple) her bir öğe için bir işlem execute eder. Aşağıda ki kulanımında yenilenebilir obje df_can'in sütun başlıkları listesidir. Bu listede ki her bir item'in tipini string tipine map ediyoruz.
df_can.columns = list(map(str, df_can.columns))
# for column in df_can.columns:
#     print(type(column))
# endregion


# region Task 5
# veri setinde'ki var olan index yerine Country sütunun index olarak ayarlayalım.
df_can.set_index(keys='Country', inplace=True)
# print(df_can.head(10).to_string())
# endregion


# region Task 6
# Yıl yıl göçmen sayılarını toplayarak total isimli yeni bir sütuna yazdırın
df_can['Total'] = df_can.sum(axis=1, numeric_only=True)
# print(df_can['Total'])
# endregion


# region Task 7
# Veri setinde ki yılları baz alarak kendimize bir yıl listesi hazırlayalım lakin liste içirisinde ki yıl bilgileri string olsun
years = list(map(str, range(1980, 2014)))
# print(years)
# endregion

# region Task 8
# En çok göç vermiş 5 ülkeyi bulun. df_top_five_country isimli df'e kayıt edin.
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top_five_country = df_can.head()
# print(df_top_five_country.to_string())
# endregion


# region Task 9
# Yukarıda oluşturulan df_top_five_country veri seti ile, year isimli ilstemizi kullanarak yılları satırlara ülkeleri sütunlara dönüştürerek bir df elde edin bu df'i df_top_five_country üzerine assigned edin.
# print(df_top_five_country[years].to_string())
df_top_five_country = df_top_five_country[years].transpose()
# print(df_top_five_country.to_string())
# endregion


# Region Task 10
# Yukarıda oluşturulan df_top_five_country veri setinden faydalanarak alan grafiği yaratalım. plot() function kullanılarak
# df_top_five_country.plot(
#     kind='area',
#     stacked=False,
#     figsize=(10, 7),
#     alpha=0.25
# )
#
# plt.title(label='Immigrant Trend of Top 5 Country', c='r')
# plt.ylabel(ylabel='Number of Immıgrant', c='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.show()
# endregion


# region Task 11
# Histogram grafiği istiyorum
# 2013 yılında ki göçmen hareketliliğini histogram grafiğinde gösterin
# grafiğib x düzleminde ki değerleri numpy kütüphanesinin histogram() fonksiyonu ile bulun
# count, bin_edges = np.histogram(df_can['2013'])
# print(count)
# print(bin_edges)
#
# df_can['2013'].plot(
#     kind='hist',
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color='b'
# )
#
# plt.title(label='Histogram of Immigrant from 195 Countries in 2013', c='r')
# plt.ylabel(ylabel='Number of Country', c='r')
# plt.xlabel(xlabel='Number of Immigrant', c='r')
# plt.grid()
# plt.show()
# endregion


# region Task 12
# Baltık ülkelerinin verdiği göçmen sayısını histogram grafiğinde gösterelim
# yıllar index ülkeler sütun olacak
# ülkeler Denmark, Norway, Sweden olsun
# histogram() fonsiyonuna bins 10 değeri verin
# plot() fonksiyonun color argümanına ['coral', 'darkblue', 'green']
# df_baltic_counties = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
#
# count, bin_edges = np.histogram(df_baltic_counties, bins=10)
#
# df_baltic_counties.plot(
#     kind='hist',
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color=['coral', 'darkblue', 'green'],
#     stacked=False,
#     alpha=0.25
# )
#
# plt.title(label='Histogram from Denmark, Norway & Sweden from 1980 to 2013', c='r')
# plt.ylabel(ylabel='Number of Years', c='r')
# plt.xlabel(xlabel='Number of Immigrant', c='r')
# plt.grid()
# plt.show()
# endregion


# region Task 13
# 1980 -2013 yılları arasında Iceland göçmenlerini çubuk grafikte gösterin
# df_iceland = df_can.loc['Iceland', years]
#
# df_iceland.plot(
#     kind='bar',
#     figsize=(10, 7)
# )
# plt.title(label='Iceland ımmigrants of Canada from 1980 to 2013', c='r')
# plt.ylabel(ylabel='Number of Immigrant', c='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.grid()
# # Annotate arrow
# plt.annotate('',                      # s: str. will leave it blank for no text
#              xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
#              xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
#              xycoords='data',         # will use the coordinate system of the object being annotated
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
#             )
#
# # Annotate Text
# plt.annotate('2008 - 2011 Financial Crisis', # text to display
#              xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
#              rotation=72.5,                  # based on trial and error to match the arrow
#              va='bottom',                    # want the text to be vertically 'bottom' aligned
#              ha='left',                      # want the text to be horizontally 'left' algned.
#             )
# plt.show()
# endregion


# region Task 14
# Kıtalara göre gçömen dağılımını pasta grafiğinde gösterelim
df_continets = df_can.groupby(by='Continent').sum(numeric_only=True)
print(df_continets.head())

df_continets['Total'].plot(
    kind='pie',
    figsize=(10, 7),
    startangle=90,  # başlangıç açısı
    autopct='%1.1f%%',  # her bir dilime gelecek gçömen sayısını formatlayarak yazdırdık
    labels=None,  # ülkelerin pasta dilimleri üzerinde gözükmesini engelledik
    shadow=True,
    pctdistance=1.1,  # yüzde etikeltinin her dilimin merzeinden uzaklığını ayarladık
    explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # pastanın dilimlerini bir birlerinden uzaklaştırmak için yaptık
)
plt.axis('equal')  # pasta grafiğnin dairesel olmasını sağlarak grafiğin en boy oranını kendisi eşitleyecek
plt.legend(
    labels=df_continets.index,
    prop={
        'size': 8
    }
)
plt.show()
# endregion