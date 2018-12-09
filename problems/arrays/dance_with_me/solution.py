from itertools import product

names = input().strip().split()

men = [x for x in names if x[-1] == 'm']
women = [x for x in names if x[-1] == 'w']

pairs = ['{}_{}'.format(x, y) for x, y in product(men, women)]
pairs.sort()

print('\n'.join(pairs))