max_num = 99

N = int(input())
lst = [0]*(max_num + 1)

for _ in range(N):
    number = int(input())
    lst[number] += 1

print(lst.index(max(lst)))
