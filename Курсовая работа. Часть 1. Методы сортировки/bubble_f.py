def bubble(arr, N):
    alg_count = [0, 0]
    for i in range(N - 1):
        alg_count[0] += 1
        j = 0
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
            alg_count[1] += 1
        i += 1
    return alg_count
