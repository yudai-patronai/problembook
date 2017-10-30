N = int(input())
M = int(input())
arr = [[int(input()) for j in range(M)] for i in range(N)]

replace = -1
while replace != 0:
    replace = 0
    for i in range(N*M-1):
        if arr[i // M][i % M] > arr[(i + 1) // M][(i + 1) % M]:
            (arr[i // M][i % M], arr[(i + 1) // M][(i + 1) % M]) = (
                                                arr[(i + 1) // M][(i + 1) % M],
                                                arr[i // M][i % M]
                                                )
            replace += 1

for line in arr:
    for item in line:
        print(item, end=' ')
    print()
