# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arifmetic_arr(a, d, n):
    list_1 = []
    for i in range(1, n+1):
        list_1.append(a + (i - 1) * d)
    return list_1

first_elem = int(input('Enter the first element: '))
step_arif_progress = int(input('Enter the step: '))
length_arr = int(input('Enter the quantity of elements: '))
print(arifmetic_arr(first_elem, step_arif_progress, length_arr))

