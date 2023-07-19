# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y)
#  1 2   3   4    5    6
#  2 4   6   8    10   12
#  3 6   9   12   15   18
#  4 8   12  16   20   24
#  5 10  15  20   25   30
#  6 12  18  24   30   36

# number_rows = int(input('Vvedite chislo strok: '))
# number_columns = int(input('Vvedite chislo stolbcov: '))

# def input_matrix(m, n):
#     for i in range(1, m+1):
#         row = []
#         for j in range(1, n+1):
#             row.append('{:>3d}'.format(i*j))
#         print(*row)
# matrix = input_matrix(number_rows, number_columns)  

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
            answer.append(operation(i, j))
        print(''.join(f'{e:<5}' for e in answer))

print_operation_table(lambda x, y: x * y)          
       
            



