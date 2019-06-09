def insert(arr, N):
    alg_count = [0, 0]
    for i in range(N - 1):
        m = arr[i]
        j = i - 1
        alg_count[0] += 1
        while j >= 0 and m < arr[j]:
            arr[j + 1] = arr[j]
            alg_count[1] += 1
            j -= 1
        arr[j + 1] = m
    return alg_count
