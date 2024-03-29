# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

def sum_divider_number(n):
    sum=0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
    return sum

# print(start)

def pair_divider(num):
    for i in range(1, num):
        start = sum_divider_number(i)
        end = sum_divider_number(start)
        if end == i and end != start and i < start:
            print(i, start)

number = int(input('Enter the number: '))
pair_divider(number)

