# Dictionary (Sözlük)
# #Sözlük, list , tuple gibi bir başka verileri depoladığımız yapıdır.
#Sözlük anahtar & değer (key value) mantığıyla çalışırlar

my_dict = {
    'Full Name': 'Mert Namsal',
    'Age': 25,
    'Interested Sport': ['Boxing','Basketball','Tennis'],
    'Favorite Books': {
        'War History': 'Cambridge War History',
        'Scientific': {
            'Karl Poper': 'The Logic Scientific Discovery'
        }
    }
}

release_year_movie = {
    'Fight Club': 1999,
    'The Matrix': 1999,
    'Insterstaller': 2014,
    'Inception': 2010,
    'Dune': 2011,
}

#Herhangi bir value ekrana basın
# Yol I
#print(release_year_movie.get('Fight Club'))

#Yol II
#print(release_year_movie["Fight Club"])

#Tüm anahtarlarını ekranra yazdrıma
# for key in release_year_movie.keys():
#     print(key)

#Tüm valuelarını ekranra yazdrıma
# for value in release_year_movie.values():
#     print(value)

# for key, value in release_year_movie.items():
#     print(f'Movie Name: {key}\n'
#     f'Release Year: {value}')

my_family = [
    ('Burak Yılmaz', 35 , 'beast'),
    ('Hakan Yılmaz', 38 , 'bear'),
    ('İpek Yılmaz', 40 , 'keko')
]

# for x,y,z in my_family:
#     print(x)
#     print(y)
#     print(z)

products = [
    {'name': 'Everlast Pro Boxing Gloves', 'price': 245},
    {'name': 'Everlast Pro Training Gloves', 'price': 200},
    {'name': 'Everlast Heavy Bag', 'price': 445},
    {'name': 'Iphone 15 Pro Max', 'price': 85000},
    {'name': 'Samsung S24 Ultra', 'price': 80000},
    {'name': 'Lenovo X1 Carbon', 'price': 59000},
]

#products Listesindeki tüm ürünlerin fiyatlarını toplayarak ekrana yazdırın
total = 0

# for i in range(len(products)):
#     total = total + products[i].get('price')
# print(total)

# for product in products:
#     total = total + product.get('price')
# print(total)

# for product in products:
#     if product['name'].__contains__("Everlast") and 240 <= product['price'] <=500:
#         print("xxx")

from uuid import uuid4
students = {}

print(students)
print(f'Manuel Guide\n==========\nCreate\nList\nUpdate\nDelete\nExit')
while True:
    process = input("Type your process upon manuel guide: ").lower()

    match process:
        case 'create':
            student_id = str(uuid4())
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone: ")
            students[student_id] = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone
            }
            pass
        case 'list':
            pass
        case 'update':
            pass
        case 'delete':
            pass
        case 'exit':
            print('Application has been closing..!')
            break
        case _:
            print('Please type valid process name..!')

