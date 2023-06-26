# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input('Введите номер билета: '))
number = ticketNumber
sum1 = 0
sum2 = 0

while (ticketNumber>999):
   digit = ticketNumber%10
   ticketNumber = ticketNumber//10
   sum1 += digit

while (ticketNumber>0):
   digit = ticketNumber%10
   ticketNumber = ticketNumber//10
   sum2 += digit
 
print(sum2, sum1)
print(f'{number} -> yes' if(sum1 == sum2) else f'{number} -> no') 
