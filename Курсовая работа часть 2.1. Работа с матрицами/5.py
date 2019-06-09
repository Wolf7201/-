# Задача 5 Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить средние значения по всем строкам и
# столбцам матрицы. Результат оформить в виде матрицы из N + 1 строк и M
# + 1 столбцов.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

M_sr = np.mean(A, axis=0)
N_sr = np.mean(A, axis=1)

N_sr = np.append(N_sr, None)

A = np.vstack((A, M_sr))
A = np.hstack((A, N_sr.reshape(-1, 1)))
print(A)