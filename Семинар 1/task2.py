# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input('Введите трехзначное число: '))
digit3 = number%10
digit2 = number//10%10
digit1 = number//100%10

print(f'сумма чисел: {digit1 + digit2 + digit3}')