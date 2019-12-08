def lcs(A, B):
    N, M = len(A), len(B)
    F = [[0]*(M+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                F[i+1][j+1] = F[i][j] + 1
            else:
                F[i+1][j+1] = max(F[i][j+1], F[i+1][j])
            
    return F[N][M]


A = input().split()
B = input().split()

lcs_length = lcs(A, B)

print('YES' if lcs_length <= len(A) // 4 else 'NO')
