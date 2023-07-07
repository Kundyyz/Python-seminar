# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Lenght of first list: '))
m = int(input('Lenght of second list: '))
list_1, list_2 = [], []

for i in range(n):
    i = int(input('Input elements for first list: '))
    list_1.append(i)
    a = set(list_1)
for i in range(m):
    i = int(input('Input elements for second list: '))
    list_2.append(i)
    b = set(list_2)
similar_elements = a.intersection(b)

list_sim = list(similar_elements)
for j in range(len(list_sim)-1):
    for i in range(len(list_sim)-1):
        if (list_sim[i] > list_sim[i+1]):
            temp = list_sim[i+1]
            list_sim[i+1] = list_sim[i]
            list_sim[i] = temp
print(list_sim)
     
