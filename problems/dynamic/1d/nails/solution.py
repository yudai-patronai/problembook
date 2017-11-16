arr = sorted([int(i) for i in input().strip().split(' ')])
N = len(arr)

weight = [float('Inf'), arr[1] - arr[0]]
for i in range(2, N):
    weight.append(min(weight[i - 1], weight[i - 2]) + (arr[i] - arr[i - 1]))
   
print(weight[-1])