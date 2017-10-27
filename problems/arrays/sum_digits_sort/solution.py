N = int(input())
arr = [input() for _ in range(N)]


def bubble_sort(arr, key=None):
    if key is None:
        def key(x):
            return x
    reverse = -1
    while reverse != 0:
        reverse = 0
        for i in range(len(arr) - 1):
            if key(arr[i]) > key(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                reverse += 1


def digit_sum(x):
    s = 0
    for i in x:
        s += int(i)
    return s


bubble_sort(arr, digit_sum)
print(' '.join(arr))
