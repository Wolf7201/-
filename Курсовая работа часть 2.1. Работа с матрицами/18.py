# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти сумму элементов, стоящих на главной
# диагонали, и сумму элементов, стоящих на побочной диагонали (элементы
# главной диагонали имеют индексы от [0,0] до [N,N], а элементы побочной
# диагонали — от [N,0] до [0,N]).

import numpy as np
import random

N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

b = A.trace()
c = A[::-1].trace()

print("Сумма элементов главной диагонали =", str(b))
print("Сумма элементов побочной диагонали =", str(c))