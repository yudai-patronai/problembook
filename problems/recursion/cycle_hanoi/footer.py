n = int(input())
arr = chanoi(n, 1,2,3)
if len(arr) > 200000:
    print("Too long solution")
else:
    flag= True
    fullrod=list(range(n, 0, -1))
    rods=[list(range(n, 0, -1)), [], []]
    for i in range(len(arr)):
        #print(arr[i][0], arr[i][1], arr[i][2])
        if arr[i][0] != rods[(arr[i][1]-1)][len(rods[(arr[i][1]-1)])-1]:
            print('Cannot move disc ', arr[i][0], 'from rod', arr[i][1])
            flag = False
            break
        elif len(rods[(arr[i][2]-1)])>0 and arr[i][0]>rods[(arr[i][2]-1)][len(rods[(arr[i][2]-1)])-1]:
            print('Cannot move disc ', arr[i][0], 'to rod', arr[i][2])
            flag = False
            break
        elif (arr[i][1]-arr[i][2]+3)%3 == 1:
            print("Wrong direction")
            flag = False
            break
        else:
            rods[arr[i][2]-1]=rods[arr[i][2]-1]+ [arr[i][0]]
            rods[arr[i][1]-1].pop()
    if len(rods[0]) == 0 and len(rods[1])==0 and len(rods[2])==n:
        for i in range(n):
            if rods[2][i] != fullrod[i]:
                print("Something's wrong...")
                flag = False
                break
    else:
        flag = False
if flag:
    print ("OK")
