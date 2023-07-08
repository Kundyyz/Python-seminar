# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

def enter_list(len_list):
    list_new = []
    for i in range(len_list):
        list_new.append(int(input('Enter the elem: ')))
    return list_new
def pait_count(list1):
    count = 0
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[i] == list1[j]:
               count += 1
    return count

n = int(input('Enter the length of list: '))
list_1 = enter_list(n)
print(list_1)
print(pait_count(list_1))