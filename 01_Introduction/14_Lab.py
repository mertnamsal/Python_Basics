
#File I/O
#Dosya açma ve kapama üzerinde CRUD işlemleri yapabileceğimiz bize fonksiyonlar tanımlayan file modüşü ile çalışacağız


#Dosya açma
# file = open(file='new_file.txt',mode='w',encoding='utf-8') #Dosyayı siler yeniden yazar
# file.write('Full Name: Mert Namsal\nOccupation: Developer\n')
# file.close()
#
# #Yukarıda yaratılan dosya üzerine yeni bir kayıt ekleyelim
# file = open(file='new_file.txt',mode='a',encoding='utf-8') #Dosyadakilere ekleme yapar silmez.
# file.write('Programing Language: Python\n')
# file.close()
#
# #Dosyadan veri okuyalım
# file = open(file='new_file.txt',mode='r',encoding='utf-8')
# for line in file.readlines():
#     print(line)

# region Task 1
# exam_grades.txt dosyasını yaratın
def create_examn_grades()->None:
    file = open(file='exam_grades.txt',mode='w',encoding='utf-8')
    file.close()
# endregion

# region Task 2
# Kullanıcıdan first_name, last_name, midterm, final, homework bilgilerini alarak exam_grades.txt dosyasına yazalım.
#Format
# Mert Yılmaz:30,30,30
# ilgili dosyayı with open() ile açalım
def take_information(first_name: str, last_name: str, midterm: float, final: float, homework: float):
    with open('exam_grades.txt','a') as my_file:
        my_file.write(f'{first_name} {last_name}:{midterm}, {final}, {homework}' + "\n")
# endregion

# region Task 3
# row example => Mert Namsal:30,30,30
# Harf notunu hesapla ve return et
def calculate_grade(row: str) -> str:
    values = row.split(':')
    full_name = values[0]
    grade_list = values[1].split(',')
    ortalama = float(grade_list[0])*0.3 + float(grade_list[1])*0.6 + float(grade_list[2])*0.1

    if ortalama >= 90:
        return f'{full_name}: AA'
    elif ortalama >= 85:
        return f'{full_name}: BA'
    elif ortalama >= 80:
        return f'{full_name}: BB'
    elif ortalama >= 75:
        return f'{full_name}: CB'
    elif ortalama >= 70:
        return f'{full_name}: CC'
    elif ortalama >= 65:
        return f'{full_name}: DC'
    elif ortalama >= 60:
        return f'{full_name}: DD'
    elif ortalama >= 55:
        return f'{full_name}: FD'
    else:
        return f'{full_name}: FF'
# endregion

# region Task 4
# exam_grades.txt dosyasından verileri satır satır okuyalım
# harf notlarını hesaplatalım ve bir listeye ekleyelim ilgili listeyi return edelim
def read_exam_grades() -> list:
    exam_list = []
    with open('exam_grades.txt', 'r') as my_file:
        for line in my_file:
            exam_list.append(f'{calculate_grade(line)}')
    return exam_list
# endregion

# region Task 5
# result.txt isimli dosyaya öğrencilerin isim soy isim: harf notunu yazdıralım
def register_grades(grade_list: list) -> None:
    with open('result.txt','w',encoding='utf-8') as file:
        for item in grade_list:
            file.write(item + "\n")
# endregion

# region Task 6
#result.txt dosyasının verilerini ekrana bas
def read_result():
    with open('result.txt','r') as file:
        for row in file:
            print(row)
# endregion
def menu():
    print(f"""
    Menu
    =======================
    Read Grades       => 1
    Enter Grades      => 2
    Calculate Result  => 3
    Read Result       => 4
    Exit              => 0
    """)

def main():
    menu()

    while True:
        process = input('Please choose a transaction: ')

        match process:
            case '1':
                read_exam_grades()
                print('Grades has benn read..!')
            case '2':
                take_information(
                    input('First Name: '),
                    input('Last Name: '),
                    float(input('Midterm: ')),
                    float(input('Final: ')),
                    float(input('Homework: ')),
                )
            case '3':
                result = read_exam_grades()
                register_grades(result)
                print('Grades calculated and stored')
            case '4':
                read_result()
            case '0':
                print('Application has been closing..!')
                break
            case _:
                print('Please choose a valid transaction no..!')

main()