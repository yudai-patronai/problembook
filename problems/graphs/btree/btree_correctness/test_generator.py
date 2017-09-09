#!/usr/bin/env python3
import os
from lib import random
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
random.seed(100)


class Node:
    def __init__(self, data):
        self.data = data  # данные в узле
        self.left = None
        self.right = None


def add(root, data):
    p = root
    x = root
    while x:
        p = x
        x = x.left if data < x.data else x.right

    if data < p.data:
        p.left = Node(data)
    else:
        p.right = Node(data)


def make_tree(sequence):
    root = Node(sequence[0])
    for x in sequence[1:]:
        add(root, x)

    return root


def shift_tree(root, shift):
    if root is None:
        return

    root.data += shift
    shift_tree(root.left, shift)
    shift_tree(root.right, shift)


def do_spoil_tree(a, b):
    if b.data < a.data:
        shift = a.data - b.data + 1 + random.randrange(10)
    else:
        shift = a.data - b.data - 1 - random.randrange(10)

    shift_tree(b, shift)


def spoil_tree(root):
    seq = []
    while root:
        seq.append(root)
        root = root.left if random.randrange(2) == 0 else root.right

    if len(seq) < 2:
        return False

    i, j = sorted(random.sample(range(len(seq)), 2))

    do_spoil_tree(seq[i], seq[j])

    return True


def to_list(out, root):
    if root is None:
        return

    cur = [root.data]
    out.append(cur)

    if root.left is None:
        cur.append(-1)
    else:
        cur.append(len(out))
        to_list(out, root.left)

    if root.right is None:
        cur.append(-1)
    else:
        cur.append(len(out))
        to_list(out, root.right)


def write_tree(f, root):
    nodes = []
    to_list(nodes, root)

    f.write(str(len(nodes)) + '\n')
    f.write('\n'.join([' '.join(map(str, x)) for x in nodes]) + '\n')


def gen_test(tests_dir, sequence):
    if not hasattr(gen_test, 'ind'):
        gen_test.ind = 1
    else:
        gen_test.ind += 1

    print(gen_test.ind, len(sequence))

    test = os.path.join(tests_dir, '%.2d' % gen_test.ind)
    ans = test + '.a'

    root = make_tree(sequence)
    answer = 'YES'
    if random.randrange(3) != 0:
        answer = 'NO' if spoil_tree(root) else 'YES'

    with open(test, 'w') as f:
        write_tree(f, root)

    with open(ans, 'w') as f:
        f.write(answer + '\n')


shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, 41):
    gen_test(tests_dir, random.sample(range(1, i * 20), i * 3))

gen_test(tests_dir, [100])
gen_test(tests_dir, range(100))
gen_test(tests_dir, range(100, 0, -1))
# Текущая реализация ГПСЧ слишком медленная для этого теста
# gen_test(tests_dir, random.sample(range(1000000), 500000))
