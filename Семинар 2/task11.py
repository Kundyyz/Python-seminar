A = int(input('Введите натуральное число больше 1:'))

a = 1
b = 0
count = 1

while b < A:
    print(b)
    n = a + b
    a = b
    b = n
    count += 1
print('Ответ:')
if b != A:
   print(f'Число {b}  не является числом Фибоначчи') 
else: 
 print (f'Число {b} является {count}-числом по счету')
