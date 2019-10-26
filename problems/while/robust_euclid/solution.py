a, b = input().split()
a= int(a)
b = int(b)

def robust_euclid(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return abs(a)

print(robust_euclid(a, b))