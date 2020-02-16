N = int(input())
pList = {}
for i in range(N):
    pName = input()
    pList[pName] = pList.get(pName, 0) + 1
pList = sorted(pList.items(), key=lambda x: x[1], reverse=True)
for p in pList:
    print(p[0])
