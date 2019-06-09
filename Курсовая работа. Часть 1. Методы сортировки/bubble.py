from random import randint

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)
i = 0
for i in range(N - 1):
    j = 0
    for j in range(N - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j += 1
    i += 1

print(arr)
