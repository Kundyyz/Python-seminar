# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
#  с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power_num(a, b):
    if b == 1:
        return a
    return a * power_num(a, b-1)

a = int(input('Zadaite chislo: '))
b = int(input('V kakoi stepeni? '))
print(power_num(a, b))