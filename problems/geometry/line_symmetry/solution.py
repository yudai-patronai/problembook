x1, y1, x2, y2 = tuple(map(int, input().split()))
x,  y = tuple(map(int, input().split()))
delta_x = x2 - x1
delta_y = y2 - y1
if delta_x == 0:
    x_ = 2*x1 - x
    y_ = y
elif delta_y == 0:
    y_ = 2*y1 - y
    x_ = x
else:
    k = delta_y / delta_x
    b = (y1 * x2 - y2 * x1) / delta_x
    k_perp = 1 / k
    b_perp = y - k_perp * x
    inter_x = (b_perp - b) / (k - k_perp)
    inter_y = k * inter_x + b
    x_ = 2 * inter_x - x
    y_ = 2 * inter_y - y
print(x_, y_)
