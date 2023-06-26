n = int(input('Введите количество арбузов: '))
maxweght = int(input('Какой вес: '))
minweight = maxweght
for i in range(n - 1):
    weight = int(input('Какой вес: '))
    if (weight > maxweght):
        maxweght = weight
    elif (weight < minweight):
          minweight = weight
print(minweight, maxweght)     