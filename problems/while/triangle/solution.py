N = int(input())

counter = 1
for i in range(1, N+1):
    s = ''
    for j in range(i):
        if j != i-1:
            s += str(counter) + ' '
        else:
            s += str(counter)
        counter += 1
    print(s)
