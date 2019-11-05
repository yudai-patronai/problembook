def merge(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    fin = [0] * (len1 + len2)
    pos1 = pos2 = posfin = 0

    while pos1 < len1 and pos2 < len2:
        if arr1[pos1] <= arr2[pos2]:
            fin[posfin] = arr1[pos1]
            pos1 += 1
        else:
            fin[posfin] = arr2[pos2]
            pos2 += 1
        posfin += 1

    fin[posfin:] = arr1[pos1:] if pos1 < len1 else arr2[pos2:]

    return fin


def merge_sort(A, depth=1):
    if len(A) > 1:
        m = len(A) // 2
        l, r = A[:m], A[m:]
        merge_sort(l, depth + 1)
        merge_sort(r, depth + 1)
        A[:] = merge(l, r)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge_sort(a)
merge_sort(b)

i, j = 0, 0
c = None
while i < len(a) and j < len(b):
    while i < len(a) and a[i] == c:
        i += 1
    while j < len(b) and b[j] == c:
        j += 1
    if i >= len(a) or j >= len(b):
        break
    if a[i] != b[j]:
        print('No')
        exit(0)
    c = a[i]
if i < len(a) or j < len(b):
    print('No')
else:
    print('Yes')
