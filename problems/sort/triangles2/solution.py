
class Triangle(object):
    def __init__(self, id_, a, b, c):
        self.id_ = id_
        self.a, self.b, self.c = a, b, c

        self.perimeter = self.get_perimeter()

    def get_perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return '{} {} {} {}'.format(self.id_, self.a, self.b, self.c)


N = int(input())
triangles = []
for _ in range(N):
    id_, a, b, c = input().split()
    a, b, c = map(int, [a, b, c])
    triangles.append(Triangle(id_, a, b, c))

triangles = sorted(triangles, key=lambda tr: (tr.perimeter, tr.id_))
for triangle in triangles:
    print(triangle)
