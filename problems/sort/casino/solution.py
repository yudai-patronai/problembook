def bubbleSort(arrayToSort):
    n = len(arrayToSort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arrayToSort[j] > arrayToSort[j + 1] :
                arrayToSort[j], arrayToSort[j + 1] = arrayToSort[j + 1], arrayToSort[j]


n = int(input())
a = list(map(int, input().split()))
bubbleSort(a)
print(sum(a[n // 2 : ]) - sum(a[ : n // 2]))
