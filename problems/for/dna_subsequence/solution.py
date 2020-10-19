s = input()
t = input()

if len(s) > len(t):
    print("NO")
    exit()

j = 0
for i in range(len(t)):
    if s[j] == t[i]:
        j += 1
        if j == len(s):
            break
if j == len(s):
    print("YES")
else:
    print("NO")
