def matryoshka(n):
    if n == 1:
        print('matryoshechka')
    else:
        print('verh matryoshki', n)
        matryoshka(n-1)
        print('niz matryoshki', n)
        