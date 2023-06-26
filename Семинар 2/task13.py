n = int(input('Введите количество дней: '))
count = 0
maxdays = 0

for i in range(n):
    temperature = int(input('Какая была температура: '))
    if (temperature > 0):
        count += 1
        if (maxdays < count):
            maxdays = count
    else:
        count = 0
print(maxdays)     