

# Dictionary (Sözlük)
# Sözlük, list, tuple gibi bir başka verileri depoladığımız yapıdır.
# Sözlükler anahtar & değer (key & value) mantığında çalışırlar

my_dict = {
    'Full Name': 'Burak Yılmaz',
    'Age': 34,
    'Interested Sport': ['Boxing', 'Wrestling', 'UFC'],
    'Favorite Books': {
        'War History': 'Cambridge War History',
        'Scientfic:': {
            'Karl Poper': 'The Logic Scientifc Discovery'
        }
    }
}


release_year_movie = {
    'Fight Club': 1999,
    'The Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2010,
    'Dune': 2011
}


# Herhangi bir value ekrana basın
# Yol I
# print(f'Interstaller Relase: {release_year_movie.get("Interstaller")}')
# # Yol II
# print(f'Interstaller Relase: {release_year_movie["Interstaller"]}')


# Sözlüğün tüm anahtarlarını ekrana yazdırın
# for key in release_year_movie.keys():
#     print(key)

# Sözlüğün tüm valuelarını ekrana yazdırın
# for value in release_year_movie.values():
#     print(value)

print(release_year_movie.items())
for key, value in release_year_movie.items():
    print(f'Movie Name: {key}\n'
          f'Release Year: {value}')

# CRUD (Create-Read-Update-Delete)
# products = [
#     {'name': 'Everlast Pro Boxing Gloves', 'price': 245},
#     {'name': 'Everlast Training Gloves', 'price': 200},
#     {'name': 'Everlast Heavy Bag', 'price': 445},
#     {'name': 'Iphone 15 Pro Max', 'price': 85000},
#     {'name': 'Samsung S24 Ultra', 'price': 80000},
#     {'name': 'Lenevo X1 Carbon', 'price': 59000},
# ]

# products listesindeki tüm ürünlerin fiyatlarını toplayarak ekrana basın
# total_price = 0
# for product in products:
#     total_price += product.get('price')  # total_price = total_price + product.get('price')
#
# print(f'Total Price: {total_price}')


# products listesinde ki ürünlerin fiyatı 30000'den büyük olan ürünleri listeleyin
# for product in products:
#     if product['price'] >= 30000:
#         print(f'Product Name: {product["name"]} - Price: {product["price"]}')


# ürün adı içerisnde Everlast geçen ve fiyat aralığı 240 ile 500 arasında olan ürünleri listeleyiniz
# for product in products:
#     if product['name'].__contains__("Everlast") and 240 <= product['price'] <= 500:
#         print(f'Product Name: {product["name"]} - Price: {product["price"]}')

# Boş bir students sözlüğü yaratalm
# Dictionary Structure
# students = {
#     'student_id': {
#         'first_name': 'fdasa',
#         'last_name': 'fdfds',
#         'phone': 'fdsfds'
#     },
#     'student_id': {
#         'first_name': 'fdasa',
#         'last_name': 'fdfds',
#         'phone': 'fdsfds'
#     }
# }
# öğrenci id'lerini uuid4 ile yaratın
# from uuid import uuid4
# from pprint import pprint
# students = {}
# while True:
#     print('Manuel Guide\n'
#           '==============\n'
#           'Create\n'
#           'List\n'
#           'Update\n'
#           'Delete\n'
#           'Exit')
#
#     process = input('Type your process upon manuel guide: ').lower()
#
#     match process:
#         case 'create':
#             student_id = str(uuid4())
#             first_name = input('First Name: ')
#             last_name = input('Last Name: ')
#             phone = input('Phone: ')
#             students[student_id] = {
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'phone': phone
#             }
#         case 'list':
#             pprint(students)
#         case 'update':
#             student_id = input('Type id: ')
#             first_name = input('First Name: ')
#             last_name = input('Last Name: ')
#             phone = input('Phone: ')
#
#             students.update({
#                 student_id: {
#                     'first_name': first_name,
#                     'last_name': last_name,
#                     'phone': phone
#                 }
#             })
#
#             print(f'{student_id} has been edited..!')
#         case 'delete':
#             student_id = input('Type id: ')
#             del students[student_id]
#             print(f'{student_id} has been removed..!')
#         case 'exit':
#             print('Application has been closing..!')
#             break
#         case _:
#             print('Please type valid process name..!')
#
