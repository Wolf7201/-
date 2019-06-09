# Задача 6
# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти сумму элементов всей матрицы.
# Определить, какую долю в этой сумме составляет сумма элементов каждого
# столбца. Результат оформить в виде матрицы из N + 1 строк и M столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

sm = np.sum(A)

m = []
for i in range(M):
    m.append(np.sum(A[:, i]))
for i in range(M):
    m[i] = round(m[i] / sm, 2)
A = np.vstack((A, m))
print(A)