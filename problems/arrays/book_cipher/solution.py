n = int(input())
code = []
for i in range(n):
    code.append(input())
ans = ""
for i in range(n):
    ind = int(input())
    ans += code[ind] + " "
print(ans)        
