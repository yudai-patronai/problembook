p = int(input())

def ferma_small(p):
  if p == 1 or p == 2:
    return 'YES'
  else:
    N = 2 ** (p-1)
    if N % p == 1:
        return 'YES'
    else:
      return 'NO'

print(ferma_small(p))