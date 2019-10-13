def transpose(arr):
    tr = [ len(l) * [ None ] for l in arr ]  # copy 2d
    dim = len(arr)
    for i in range(dim):
        for j in range(dim):
            tr[i][j] = arr[j][i]

    return tr


def arr2d_to_str(arr):
    s = ""
    for row in arr:
        s += " ".join(row) + '\n'
    return s


m = []
dim = int(input())

for _ in range(dim):
    m.append(input().split())

m2 = transpose(m)
print(arr2d_to_str(m2), end='')
