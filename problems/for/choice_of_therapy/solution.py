def isprime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


N = int(input())
drugs = list(map(int, input().split()))

max_effect = 0
for i in range(len(drugs)):
    for j in range(i+1, len(drugs)):
        effect = drugs[i] + drugs[j]
        if isprime(effect) and effect > max_effect:
            max_effect = effect

print(max_effect)
