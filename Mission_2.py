import random
import time

print('Введите количество строк:')
user_m = input() # Количество строк матрицы
print('Введите количество столбцов:')
user_n = input() # Количество столбцов матрицы
print('Введите минимальный диапазон случайного числа:')
user_min_limit = input() # Минимальный и максимальный диапазон случайного значения
print('Введите максимальный диапазон случайного числа:')
user_max_limit = input()

matrix = [[random.randint(int(user_min_limit), int(user_max_limit)) for _ in range(int(user_n))] for _ in range(int(user_m))]

for row in matrix:
    print(row)
