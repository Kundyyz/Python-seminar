# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

import random

def generater_list(len_list):
    list_new = []
    for i in range(len_list):
        list_new.append(random.randint(1,15))
    return list_new

def count_greater_elem(list1):
    count = 0
    for i in range(1, len(list1)-1):
        if list1[i] > list1[i-1] and list1[i] > list1[i+1]:
            count += 1
    return count

length_list = int(input('Enter the len og list: '))
list_1 = generater_list(length_list)
print(list_1)
print(count_greater_elem(list_1))