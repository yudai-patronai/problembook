def input_room():
    size = int(input())
    res = [[0.0, ''] for _ in range(size)]
    for i in range(size):
        str_ = input().split()
        res[i][0] = float(str_[0])
        res[i][1] = str_[1]
    return res


def merge(a1, a2, comp: (lambda x, y: x <= y)):
    len1, len2 = len(a1), len(a2)
    fin = [0] * (len1 + len2)
    pos1 = pos2 = posfin = 0

    while pos1 < len1 and pos2 < len2:
        if comp(a1[pos1], a2[pos2]):
            fin[posfin] = a1[pos1]
            pos1 += 1
        else:
            fin[posfin] = a2[pos2]
            pos2 += 1
        posfin += 1

    fin[posfin:] = a1[pos1:] if pos1 < len1 else a2[pos2:]

    return fin


def non_less(x1, x2):
    return False if x1[0] < x2[0] else x1[0] > x2[0] or x1[1] <= x2[1]


def merge_rooms(a1, a2):
    return merge(a1, a2, comp=non_less)


def print_res(a):
    print(len(a))
    print(*('{:.2f} {}'.format(*x) for x in a), sep='\n')


room_n = int(input())
res = []
for _ in range(room_n):
    res = merge_rooms(res, input_room())
print_res(res)
