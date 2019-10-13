def cycle_shift_N(arr, N, M):
    M = M % N
    for i in range(M):
        tmp = arr[0]
        for idx in range(1, N):
            arr[idx - 1] = arr[idx]
        arr[-1] = tmp
