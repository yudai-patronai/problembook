def printSubArrays(arr, start, end):
    # stop at the end
    if end == len(arr):
        return
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
    # Print the subarray and increment start
    else:
        print(*arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)


# считывание входных данных
arr = input().split()
printSubArrays(arr, 0, 0)
