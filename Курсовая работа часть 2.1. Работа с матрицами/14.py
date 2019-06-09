# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы матрицы на элемент матрицы
# с наибольшим значением.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

mx = A.max()
A_n = A.flat
for i in range(len(A_n)):
    if A_n[i] != mx:
        A_n[i] = round(A_n[i] / mx, 2)

A_n = np.array(A_n)
A_n = A_n.reshape(N, M)
print(A_n)
