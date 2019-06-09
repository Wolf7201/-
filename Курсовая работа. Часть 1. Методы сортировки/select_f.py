def select(arr, N):
    alg_count = [0, 0]
    for i in range(N - 1):
        m = i
        j = i + 1
        while j < N:
            alg_count[0] += 1
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        alg_count[1] += 1
        i += 1
    return alg_count

