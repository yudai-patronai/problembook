def argsort(arr, n):
    arr = list(arr)
    idx = [i for i in range(n)]
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                idx[j], idx[j+1] = idx[j+1], idx[j]
    return idx