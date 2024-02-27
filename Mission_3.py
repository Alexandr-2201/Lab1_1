import random
import time
import copy

print('Введите количество строк:')
user_m = input() # Количество строк матрицы
print('Введите количество столбцов:')
user_n = input() # Количество столбцов матрицы
print('Введите минимальный диапазон случайного числа:')
user_min_limit = input() # Минимальный и максимальный диапазон случайного значения
print('Введите максимальный диапазон случайного числа:')
user_max_limit = input()

matrix = [[random.randint(int(user_min_limit), int(user_max_limit)) for _ in range(int(user_n))] for _ in range(int(user_m))]

print('Стандартная матрица:')
for row in matrix:
    print(row)



# Сортировка строк выбором закоментирована
#for i in range(len(matrix_1)):
#        min_idx = i
#        for j in range(i+1, len(matrix_1)):
#            if matrix_1[j] < matrix_1[min_idx]:
#                min_idx = j
#        matrix_1[i], matrix_1[min_idx] = matrix_1[min_idx], matrix_1[i]


# Сортировка выбором.
# Берётся срез массива, в котором минимальный элемент переносят в самый левый угол,
# после чего срез уменьшается и цикл повторяется.
def selection_sort(matrix):
    n = len(matrix)
    for row in matrix:
        for i in range(n):
            minimum = i
            for j in range(i + 1, n):
                # Выбор наименьшего значения
                if row[j] < row[minimum]:
                    minimum = j
            row[minimum], row[i] = row[i], row[minimum]
    return matrix

# Сортировка вставкой.
def insertion_sort(matrix):
    n = len(matrix)
    for row in matrix:
        for i in range(n):
            cursor = row[i]
            pos = i
            while pos > 0 and row[pos - 1] > cursor:
                # Меняем местами число, продвигая по списку
                row[pos] = row[pos - 1]
                pos = pos - 1
            # Остановимся и сделаем последний обмен
            row[pos] = cursor
    return matrix

# Пузырьковая сортировка
def bubble_sort(matrix):
    n = len(matrix)
    for row in matrix:
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if row[i - 1] > row[i]:
                    row[i-1], row[i] = row[i], row[i-1]
                    swapped = True
    return matrix

# Сортировка Шелла
def shell_sort(matrix):
    n = len(matrix)
    for row in matrix:
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = row[i]
                j = i
                while j >= gap and row[j - gap] > temp:
                    row[j] = row[j - gap]
                    j -= gap
                row[j] = temp
            gap //= 2
    return matrix

#Быстрая сортировка
def quick_sort_row(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_row(less) + [pivot] + quick_sort_row(greater)

def quick_sort(matrix):
    for row in matrix:
        row=quick_sort_row(row)
    return matrix

# Турнирная сортировка
def tournament_sort_row(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_max_heap(arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)

    def tournament(arr):
        n = len(arr)
        build_max_heap(arr)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)

    tournament(arr)
    return arr

def tournament_sort(matrix):
    for row in matrix:
        row=tournament_sort_row(row)
    return matrix



# Вывод: стандартная сортировка
start_time = time.time()
matrix_sort_standart=sorted(matrix)
print('\nСтандартная сортировка:')
standart_time=round((time.time() - start_time)*1000)
for row in matrix_sort_standart:
    print(row)
print("--- {0} ms ---".format(standart_time))

# Вывод: сортировка выбором
start_time = time.time()
matrix_sort_custom=selection_sort(matrix)
print('\nСортировка выбором:')
selection_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(selection_time))

# Вывод: сортировка вставкой
start_time = time.time()
matrix_sort_custom=insertion_sort(matrix)
print('\nСортировка вставкой:')
insertion_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(insertion_time))

# Вывод: пузырьковая сортировка
start_time = time.time()
matrix_sort_custom=bubble_sort(matrix)
print('\nПузырьковая сортировка:')
bubble_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(bubble_time))

# Вывод: пузырьковая сортировка
start_time = time.time()
matrix_sort_custom=shell_sort(matrix)
print('\nСортировка Шелла:')
shell_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(shell_time))

# Вывод: быстрая сортировка
start_time = time.time()
matrix_sort_custom=quick_sort(matrix)
print('\nБыстрая сортировка:')
quick_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(quick_time))

# Вывод: турнирная сортировка
start_time = time.time()
matrix_sort_custom=tournament_sort(matrix)
print('\nТурнирная сортировка:')
tournament_time=round((time.time() - start_time)*1000)
for row in matrix_sort_custom:
    print(row)
print("--- {0} ms ---".format(tournament_time))

# Итог времени выполнения
print('\n===== Итоги по времени выполнения =====')
print("Стандартная сортировка:    {0} ms".format(standart_time))
print("Сортировка выбором:        {0} ms".format(selection_time))
print("Сортировка вставкой:       {0} ms".format(insertion_time))
print("Пузырьковая сортировка:    {0} ms".format(bubble_time))
print("Быстрая сортировка:        {0} ms".format(quick_time))
print("Турнирная сортировка:      {0} ms".format(tournament_time))