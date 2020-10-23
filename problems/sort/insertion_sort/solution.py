def insertion_sort(A):
    print(*A)
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                print(*A)


array = [int(e) for e in input().split()]
insertion_sort(array)
