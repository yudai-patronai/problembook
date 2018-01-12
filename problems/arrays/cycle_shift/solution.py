def cycle_shift(arr, N):
    tmp = arr[0]
    for idx in range(1, N):
        arr[idx - 1] = arr[idx]
    arr[-1] = tmp
