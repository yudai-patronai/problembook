import math
a = int(input())
b = int(input())
c = int(input())
if a >= b+c or b >= a+c or c >= a+b:
    print("impossible")
    exit(0)
alpha = math.acos((a**2-b**2-c**2)/(-2*b*c))
beta = math.acos((b**2-a**2-c**2)/(-2*a*c))
gamma = math.acos((c**2-a**2-b**2)/(-2*a*b))
if alpha == math.pi/2 or beta == math.pi/2 or gamma == math.pi/2:
    print("right")
elif alpha > math.pi/2 or beta > math.pi/2 or gamma > math.pi/2:
    print("obtuse")
else:
    print("acute")
