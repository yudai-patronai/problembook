#read data
N = int(input())
A = N*[0]

for top in range(N):
	A[top] = int(input())

# other solution
#A = [int(input()) for _ in range(N)]

#reversed print
for top in reversed(range(N)):
	print(A[top])

# other solution
#for top in range(N-1, -1, -1):
#	print(A[top])
