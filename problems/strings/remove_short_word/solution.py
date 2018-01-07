raw_sorted = input().split(' ')
print(*[sum([ord(i) for i in word]) for word in raw_sorted if len(word) > 4])
