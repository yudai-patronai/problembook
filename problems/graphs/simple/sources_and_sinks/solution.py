import urllib.request
import re
import argparse

def solution(n, A):
    istok = []
    stok = []
    
    for i in range(n):
        if sum(A[i]) == 0:
            stok.append(i+1)
    stok.sort()
    
    for i in range(n):
        if sum([sub_list[i] for sub_list in A]) == 0:
            istok.append(i+1)
    istok.sort()

    return stok, istok



n = int(input().strip())
A = []
for _ in range(n):
    A.append(list(map(int, input().strip().split())))

stok, istok = solution(n, A)

print(*istok)
print(*stok)
