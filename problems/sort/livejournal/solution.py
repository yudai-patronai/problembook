n = int(input())
f = [input() for _ in range(n)]
m = int(input())
af = [input() for _ in range(m)]
mf = []
for i in list(f):
    if i in af:
        mf.append(i)
        af.remove(i)
print("Friends: " + ', '.join(sorted(f)))
print("Mutual Friends: " + ', '.join(sorted(mf)))
print("Also Friend of: " + ', '.join(sorted(af)))
