n = int(input())
code = []
for i in range(n):
    code.append(input())
decoded = []
for i in range(n):
    ind = int(input())
    decoded.append(code[ind])
print(*decoded, end='')
