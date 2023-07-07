# ; Задача №33. Решение в группах
# ; Хакер Василий получил доступ к классному журналу и
# ; хочет заменить все свои минимальные оценки на
# ; максимальные. Напишите программу, которая
# ; заменяет оценки Василия, но наоборот: все
# ; максимальные – на минимальные.
# ; Input: 5 -> 1 3 3 3 4
# ; Output: 1 3 3 3 1
import random
n = int(input('Vvedite dlinu spiska: '))
list = []

def create_list():
    for i in range(n):
        list.append(random.randint(1, 10))
    return list

print(create_list())

min_mark = min(list)
max_mark = max(list)

def changed_list(list):
    for i in range(len(list)):
        if list[i] == max_mark:
            list[i] = min_mark
    return list
print(changed_list(list))