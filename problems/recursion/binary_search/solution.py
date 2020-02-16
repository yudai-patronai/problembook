def bins(arr, b, left=0):
    if len(arr) == 0:
        return -1
    else:
        mid = len(arr) // 2
        if arr[mid] == b:
            return left + mid+1
        elif arr[mid] < b:
            newarr = arr[(mid+1):]
            return bins(newarr, b, left=left+mid+1)
        else:
            newarr = arr[:mid]
            return bins(newarr, b, left=left)


array = list(map(int, input().split()))
n = int(input())
print(bins(array, n))
