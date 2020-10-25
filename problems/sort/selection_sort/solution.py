def selection_sort(a):
    print(*a)
    for i in range(0, len(a) - 1):
        min_j = i
        for j in range(i, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
        print(*a)


array = [int(e) for e in input().split()]
selection_sort(array)
