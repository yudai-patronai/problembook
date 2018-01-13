def split_array(arr, n, x):
    a, e, g = [], [], []
    for i in arr:
        if i < x:
            a.append(i)
        elif i == x:
            e.append(i)
        else:
            g.append(i)
    j = 0
    for i in a:
        arr[j] = i
        j += 1
    for i in e:
        arr[j] = i
        j += 1
    for i in g:
        arr[j] = i
        j += 1
