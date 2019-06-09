# Задача 2
# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наибольшее значение среди средних
# значений для каждой строки матрицы.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")
a = 0
for i in range(M):
    if np.mean(A[:, i], axis=0) > a:
        a = i
k = np.mean(A[:, a], axis=0)
print("Столбец с наибольшим средним значением - ", str(A[:, a]))
print("Наибольшее значение среди средних значений - ", str(k))
