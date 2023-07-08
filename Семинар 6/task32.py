# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

def generater_list(len_list):
    list_new = []
    for i in range(len_list):
        list_new.append(random.randint(-20,20))
    return list_new
def index_in_range(list1, min_n, max_n):
    list_index= []
    for i in range(len(list1)):
        if min_n <= list1[i] <= max_n:
            list_index.append(i)
    return list_index
    
min_range = int(input('Enter the minimum range: '))
max_range = int(input('Enter the maximum range: '))
list_1 = generater_list(15)
print(list_1)
print(index_in_range(list_1, min_range, max_range))