"""
3) сортировочное действие Хоара на массиве строк.
Элемент массива - скорость вида 'X L/T', где X - натуральное число, L - размерность длины (мм, см, м, км),
T - размерность времени (с, мин, час)

Действие совершать, опираясь на величину скорости.
"""

def velocity_mmpersec(s):
    # возвращает значение скорости в mm/s по строке
    num, dim = s.split()
    num = int(num)

    dim_l, dim_t = dim.split('/')

    l = -1
    if   dim_l == 'mm': l = 1
    elif dim_l == 'cm': l = 10
    elif dim_l == 'm':  l = 10**3
    elif dim_l == 'km': l = 10**6
    else:
        raise(ValueError(dim))

    t = -1
    if   dim_t == 's':      t = 1
    elif dim_t == 'min':    t = 60
    elif dim_t == 'h':      t = 3600
    else:
        raise(ValueError(dim))

    return num * l / t


def split_barrier(A):
    barrier = velocity_mmpersec(A[0])
    L, M, R = [], [], []
    for elem in A:
        if velocity_mmpersec(elem) < barrier:
            L.append(elem)
        elif elem == barrier:
            M.append(elem)
        else:
            R.append(elem)
    j = 0
    for elem in L + M + R:
        A[j] = elem
        j += 1
