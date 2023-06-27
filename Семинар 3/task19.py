list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input('Введите число: '))
k = k%len(list_1)
result = list_1[len(list_1) - k:] + list_1[:len(list_1) - k]
print(k, result)