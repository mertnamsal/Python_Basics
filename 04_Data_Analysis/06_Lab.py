import pandas as pd

# Merge & Join
# İki veri setinde ortak olarak bulunan sütunlardan faydalanılarak bu iki veri setinin birleştirilme işlemlerini yaptığımız fonksiyonlar merge ve joindir.
# Sql de join mantığı birebir aynıdır.

customer = {
    'Customer Id': [1,2,3],
    'First Name': ['Burak','Hakan','İpek'],
    'User Name': ['beast','bear','keko']
}

orders = {
    'Order Id': [1001,1002,1003,1004,1005],
    'Customer Id': [1,2,3,4,5],
    'Order Date': ['2024-04-14','2024-03-13','2024-01-10','2024-04-14','2024-02-24']
}

df_customer = pd.DataFrame(customer)
df_orders = pd.DataFrame(orders)

#inner merge
# print(
#     pd.merge(
#         left=df_customer,
#         right=df_orders,
#         on='Customer Id',
#         how='inner'
#     )
# )
# right merge
# print(
#     pd.merge(
#         left=df_customer,
#         right=df_orders,
#         on='Customer Id',
#         how='right'
#     )
# )
#
# print(
#     pd.merge(
#         left=df_orders,
#         right=df_customer,
#         on='Customer Id',
#         how='right'
#     )
# )

# print(df_orders.merge(df_customer, how='left'))

print(df_orders.set_index('Customer Id').join(df_customer, how='inner',on='Customer Id'))