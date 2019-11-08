def print_2d(arr):
    for r in arr:
        print( ' '.join(map(str, r)) )

def bubble_sort2d(matrix, N, M):
    print_2d(matrix)
    print()
    
    for k in range(0, N*M-1):
        for l in range(0, N*M-k-1):
            i1 = l // M
            j1 = l % M
            i2 = (l+1) // M
            j2 = (l+1) % M
            if matrix[i1][j1] > matrix[i2][j2]:
                matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
                print_2d(matrix)
                print()
