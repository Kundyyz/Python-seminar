# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
composition = 1
print(f'{n} -> 0') 
for i in range(n):
    composition = composition * 2
    if composition < n:
       print(f'{n} -> {composition}')    
    
