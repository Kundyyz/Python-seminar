# # from pathlib import Path


# # file_path = Path('data', 'new_info.txt')
# # print(file_path)

# from pathlib import Path

# Пример
# file_path = Path('new_info.txt')
# print(file_path)

# with open(file_path, 'r') as file:
#     for i, line in enumerate(file):
#         print(i, line.strip())


# Пример 
# from pathlib import Path


# file_path = Path('new_info.txt')
# print(file_path)

# with open(file_path, 'w') as file:
#     file.write('\nПерезаписали файл')

# Пример 
# from pathlib import Path


# file_path = Path('new_info.txt')
# print(file_path)

# with open(file_path, 'a') as file:
#     file.write('\nTest A')


# Пример 
# from pathlib import Path


# file_path = Path('new_info.txt')
# print(file_path)

# with open(file_path, 'w', encoding='utf8') as file:
#     file.write('\nПерезаписали файл')

# Задача 55

# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, 
# имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Ф-я вывода контактов
# 2. Ф-я поиска контакта
# 3. Ф-я добавления контакта

# Имя1,Фамилия1,Телефон1
# Имя2,Фамилия2,Телефон2
# Имя3,Фамилия3,Телефон3
# Имя4,Фамилия4,Телефон4

import codeop
from pathlib import Path

FILE_PATH = Path('phonebook.txt')

with open(FILE_PATH, 'w', encoding='utf8') as file:
    file.write(input('Введите данные: '))

def add_contact():
    with open(FILE_PATH, 'a', encoding='utf8') as file: 
        info=input('Введите данные: ') 
        file.write(f'\n{info}')

def show_contact():
    with open(FILE_PATH, 'r', encoding='utf8') as file: 
        print(*[line for line in file])
        print(file.readlines())

def find_contact():
    list_1=[]
    search=input('Введите искомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contact in file:
            if search in contact:
                list_1.append(contact)
        print(*[line for line in list_1])      

def delete_contact():
    list_1=[]
    search=input('Введите какой контакт хотите удалить из списка: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contact in file:
            if search not in contact:
                list_1.append(contact)
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        for line in list_1:
            file.write(line)

def change_contact():
    list_1=[]
    search=input('Введите какой контакт хотите редактировать: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contact in file:
            if search not in contact:
                list_1.append(contact)
            else:
                new_contact = input('Новый текст: ').strip()
                list_1.append(new_contact+'\n')
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        for line in list_1:
            file.write(line)
                 
def choice():
    flag=True
    while flag:
        n=input(f'Если хотите добавить контакт, введите "1"\nЕсли хотите посмотреть телефонную книжку, введите "2"\nЕсли хотите найти контакт, введите "3"\nЕсли хотите удалить контакт, введите "4"\nЕсли хотите изменить контакт, введите "5"\nЕсли хотите выйти, введите "6":\n ')
        match n:
            case '1':
                add_contact()         
            case '2':
                show_contact()                
            case '3':
                find_contact()               
            case '4':
                delete_contact()
            case '5':
                change_contact()
            case '6':
                flag=False
                print('Bye-bye')
choice()