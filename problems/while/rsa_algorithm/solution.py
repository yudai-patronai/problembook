M = input()
M = [int(el) for el in M.split()]


def rsa_decode(M):
    M_dec = []
    for el in M:
        el_dec = el**107 % 187
        M_dec.append(el_dec)
    return M_dec


print(*rsa_decode(M))
