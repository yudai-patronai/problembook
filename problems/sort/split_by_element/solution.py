def split_array(arr, n, x):
    l, e = 0, 0
    for i in arr:
        if i < x:
            l += 1
        elif i == x:
            e += 1
    i, j, k = 0, l, l+e
    idx = 0
    while i < l and j < l+e and k < n:
        while i < l and arr[i] < x:
            i += 1
        while j < l+e and arr[j] == x:
            j += 1
        while k < n and arr[k] > x:
            k += 1
        if i < l and arr[i] == x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif i < l and arr[i] > x:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k += 1
        elif j < l+e and arr[j] > x:
            arr[j], arr[k] = arr[k], arr[j]
            k += 1
