from random import randint

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)
i = 0

for i in range(N - 1):
    m = arr[i]
    j = i - 1
    while j >= 0 and m < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = m

print(arr)
