def solution(n, A):
    istok = []
    stok = []

    for i in range(n):
        if sum(A[i]) == 0:
            stok.append(i+1)

    for i in range(n):
        if sum([row[i] for row in A]) == 0:
            istok.append(i+1)

    return stok, istok


if __name__ == '__main__':
    n = int(input().strip())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().strip().split())))

    stok, istok = solution(n, A)

    print(*istok)
    print(*stok)
