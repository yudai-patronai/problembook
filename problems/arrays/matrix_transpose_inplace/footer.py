
# пустая строка выше для склейки solution.py + footer.py
# студенты забывают newline в конце решения
N = int(input())
A = []
for _ in range(N):
    A.append(input().split())

prev_A_id = id(A)
transpose(A)
assert prev_A_id == id(A), 'Your function does not work in-place! id(A) is changed after transpose(A) call'

for row in A:
    print(*row)
