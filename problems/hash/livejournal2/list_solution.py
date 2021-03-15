N = int(input())
following = [input() for _ in range(N)]

M = int(input())
friends = 0
for _ in range(M):
    name = input()
    if name in following:
        friends += 1

print(friends, M - friends, N - friends)
