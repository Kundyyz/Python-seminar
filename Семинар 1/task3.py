import math
a = int(input('Введите количество учащихся в 1 классе: '))
b = int(input('Введите количество учащихся в 2 классе: '))
c = int(input('Введите количество учащихся в 3 классе: '))


tableA = (a+1)//2 
tableB = (b+1)//2 
tableC = (c+1)//2 
print(f'требуется {tableA + tableB + tableC} парты')