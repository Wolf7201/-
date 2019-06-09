# Задача 3
# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наименьший элемент столбца матрицы A,
# для которого сумма абсолютных значений элементов максимальна.

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print("N =", str(N), " - ", "M =", str(M))
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")
a = 0
for i in range(M):
    if np.sum(A[:, i]) > a:
        a = i
k = np.min(A[:, a])
print("Строка с наибольшей суммой - ", str(A[:, a]))
print("Наименьший эллемент столбца - ", str(k))