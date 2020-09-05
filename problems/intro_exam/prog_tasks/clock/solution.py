secs = int(input())

hours = secs // 3600
secs %= 3600
minutes = secs // 60
secs %= 60

print(hours)
print(minutes)
print(secs)
