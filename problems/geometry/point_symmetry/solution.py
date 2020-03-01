def sim_pt(pt, center):
    return 2 * center[0] - pt[0], 2 * center[1] - pt[1]

threeangle = list(map(int, input().split()))
point = list(map(int, input().split()))
v1 = sim_pt(threeangle[0:2], point)
v2 = sim_pt(threeangle[2:4], point)
v3 = sim_pt(threeangle[4:6], point)
print(v1[0], v1[1], v2[0], v2[1], v3[0], v3[1])
