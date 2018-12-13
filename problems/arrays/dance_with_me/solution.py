from itertools import product, combinations, permutations

p, q = [int(x) for x in input().strip().split()]
names = input().strip().split()


def grouper(seq, last, value):
    men = [x for x in seq if x[-1] == last]
    return ['+'.join(x) for x in permutations(men, value)]


men = grouper(names, 'm', p)
women = grouper(names, 'w', q)

pairs = ['{}_{}'.format(x, y) for x, y in product(men, women)]
pairs.sort()

print('\n'.join(pairs))
