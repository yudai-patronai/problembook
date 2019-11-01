def bubble_sort(arr_iter):
    arr = list(arr_iter)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


n = int(input())
a = bubble_sort(map(int, input().split()))
s = 0
for i in range(n // 2 + 1):
    s += a[i] // 2 + 1
print(s)
