# Задача 4
# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наименьшее значение среди средних
# значений для каждой строки матрицы.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")
a = np.average(A[0, :])  # Минимальное среднее значение строки
b = 0  # Индекс строки с мин. значением
for i in range(N):
    if np.average(A[i, :]) < a:
        a = np.average(A[i, :])
        b = i
print("Строка с наименьшим средним значением - ", str(A[b, :]))
print("Наименьшее среднее значение - ", str(a))