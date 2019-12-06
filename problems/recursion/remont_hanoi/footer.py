

n = int(input())
arr = mov (n,1,3)
if len(arr) > 200000:
    print("Too long solution")
else:
    flag = True
    fullrod = list(range(n, 0, -1))
    rods = [list(range(n, 0, -1)), [], []]
    for i in range(len(arr)):
        old = arr[i][1] - 1
        new = arr[i][2] - 1
        if arr[i][0] != rods[old][len(rods[old])-1]:
            print('Cannot move disc ', arr[i][0], 'from rod', arr[i][1])
            flag = False
            break
        elif len(rods[new])>0 and arr[i][0]>rods[new][len(rods[new])-1]:
            print('Cannot move disc ', arr[i][0], 'to rod', arr[i][2])
            flag = False
            break
        elif abs(arr[i][1]-arr[i][2])> 1:
            print("Wrong direction")
            flag = False
            break
        else:
            rods[new]=rods[new]+ [arr[i][0]]
            rods[old].pop()
    if len(rods[0]) == 0 and len(rods[1])==0 and len(rods[2])==n:
        for i in range(n):
            if rods[2][i] != fullrod[i]:
                print("Something's wrong...", *rods[2])
                flag = False
                break
    else:
        flag = False
if flag:
    print ("OK")


