"""
Вычисляет постфиксное выражение для 3х мерных векторов.
Операции: + - сумма двух векторов, * - векторное произведение.
Вектор задаётся строкой из 3х чисел, отделённых запятой.

Например:
Если a = (ax, ay, az), b = (bx, by, bz), c = (cx, cy, cz)
и требуется вычислить [(a+b), c], то постфиксная запись такова
ax,ay,az bx,by,bz + cx,cy,cz *
"""

def vecmul(a, b):
    # c = [a, b]
    c = [None for _ in range(3)]
    c[0] = - (a[1]*b[2] - a[2]*b[1])
    c[1] = - (a[0]*b[2] - a[2]*b[0])
    c[2] = - (a[0]*b[1] - a[1]*b[0])

    return c


def vecsum(a, b):
    # c = a + b
    return [ a[i] + b[i] for i in range(len(a)) ]


postfix = input().split()

stack = []
for elem in postfix:    
    if not elem in {'*', '+'}:  # операнд
        l = list(map(int, elem.split(',')))
        stack.append(l)
        continue
    else:  # оператор
        operand2 = stack.pop()
        operand1 = stack.pop()
        if elem == '*':
            res = vecmul(operand1, operand2)
        elif elem == '+':
            res = vecsum(operand1, operand2)
        else:
            raise ValueError(elem)
        stack.append(res)

print( ','.join(map(str, stack.pop())) )
