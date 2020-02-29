def distance_sq(a, b):
    dis = (a[0]-b[0])**2 + (a[1]-b[1])**2
    return dis


def dis_square_compare(a, b):
    return 4*a <= b


suslik = list(map(int, input().split()))
sobaka = list(map(int, input().split()))
n = int(input())
nory = []
for i in range(n):
    nora = list(map(int, input().split()))
    nory.append(nora)
suslength = list(map(distance_sq, [suslik]*n, nory))
doglength = list(map(distance_sq, [sobaka]*n, nory))
good_nory = list(map(dis_square_compare, suslength, doglength))
flag = False
for i in range(n):
    if good_nory[i]:
        print(i+1)
        flag = True
        break
if not flag:
    print(-1)
