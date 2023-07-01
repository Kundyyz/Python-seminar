# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n= int(input('Введите натуральное число:'))
arr = [None] * n
close_num = 0
for i in range(n):
    arr[i] = random.randint(1, 50)
print(arr)
x = int(input('Введите натуральное число:'))
diff_num = arr[0]
for i in range(n):
    if (arr[i] > diff_num):
        diff_num = arr[i]  #Нахожу наибольший элемент в массиве

for i in range(n):
    a = arr[i] - x     #Ищу разницу между каждым элементом и х
    if -1 < a < diff_num:    #Сравниваю разницу
       diff_num = a
       close_num =  arr[i]    
print (close_num)
