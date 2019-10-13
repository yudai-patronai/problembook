def cycle_shift_N(arr, N, M):
    tmp = arr[0]
    for i in range(0,  M * (N - 1), M):
        arr[i % N] = arr[(i + M) % N]
    arr[M * (N-1) % N] = tmp

