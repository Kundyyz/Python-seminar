list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input('Введите число: '))

result = list_1[len(list_1) - k:len(list_1)] + list_1[0:len(list_1) - k]
print(result)