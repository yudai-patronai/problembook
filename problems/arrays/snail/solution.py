def make_snail(array):
    
    if array == [[]]:
        print(-1)
        
    size = len(array)
    
    for n in range((size + 1) // 2):
        for x in range(n, size - n):
            print(array[n][x])
        for y in range(1 + n, size - n):
            print(array[y][-1 - n])
        for x in range(2 + n, size - n + 1):
            print(array[-1 - n][-x])
        for y in range(2 + n, size - n):
            print(array[-y][n])


if __name__ == '__main__':
    
    N = int(input())
    array = [[0] * N for _ in range(N)] 
    
    for i in range(N):
        for j in range(N):
            array[i][j] = int(input()) 
    
    make_snail(array)
