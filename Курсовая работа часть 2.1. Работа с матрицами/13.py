# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы каждого столбца матрицы на
# элемент этого столбца с наибольшим значением.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

for i in range(M):
    mx = np.max(A[:, i])
    for k in range(N):
        if A[k, i] != mx:
            A[k, i] = round(A[k, i] / mx, 2)
print(A)

