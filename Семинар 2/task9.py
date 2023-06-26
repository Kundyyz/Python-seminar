n = int(input('Введите натуральное число: '))
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f'n! = {factorial}')
