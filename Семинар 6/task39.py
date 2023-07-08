# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

def generater_list(len_list):
    list_new = []
    for i in range(len_list):
        list_new.append(random.randint(1,15))
    return list_new
def find_diff_list(list1, list2):
    list_new = []
    for item in list1:
        if item not in list2:
            list_new.append(item)
    return list_new
            
length_list_1 = int(input('Enter the len og list 1: '))
length_list_2 = int(input('Enter the len og list 2: '))
list_1 = generater_list(length_list_1)
print(list_1)
list_2 = generater_list(length_list_2)
print(list_2)
print(find_diff_list(list_1, list_2))