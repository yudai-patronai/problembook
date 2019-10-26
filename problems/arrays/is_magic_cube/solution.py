def is_magic(arr):
    #  slow method

    dim = len(arr)
    sum_rows = [0] * dim
    sum_columns = [0] * dim
    sum_diag_1 = 0
    sum_diag_2 = 0
    for i in range(dim):
        for j in range(dim):
            elem = arr[i][j]
            sum_rows[i] += elem
            sum_columns[j] += elem

            if i == j:
                sum_diag_1 += elem
            if i == dim - j - 1:
                sum_diag_2 += elem

    if len(set([sum_diag_1, sum_diag_2] + sum_rows + sum_columns)) > 1:
        return False
    else:
        return True


m = []
dim = int(input())

for _ in range(dim):
    m.append( list( map(int, input().split()) ) ) 

ans = is_magic(m)
print("YES" if ans else "NO")
