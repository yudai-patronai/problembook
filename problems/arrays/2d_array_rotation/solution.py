def rotate_matrix(m, l):
    w = (l+1) // 2
    h = l // 2
    for i in range(w):
        for j in range(h):
            m[i][j], m[l-1-j][i], m[l-1-i][l-1-j], m[j][l-1-i] = \
            m[l-1-j][i], m[l-1-i][l-1-j], m[j][l-1-i], m[i][j]


m_len = int(input())
m = [input().split() for _ in range(m_len)]
rotate_matrix(m, m_len)
print('\n'.join(' '.join(r) for r in m))
