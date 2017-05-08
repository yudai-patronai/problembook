#!/usr/bin/env python3
import os
import random
import shutil
import sys
import solution
from solution import Node

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
random.seed(100)

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


def rand_numbers(sequence, n):
    return [random.choice(sequence) for i in range(n)]

def gen_test(tests_dir, sequence):
    if not hasattr(gen_test, 'ind'):
        gen_test.ind = 1
    else:
        gen_test.ind += 1

    print(gen_test.ind, len(sequence))

    test = os.path.join(tests_dir, '%.2d' % gen_test.ind)
    ans = test + '.a'

    root = make_tree(sequence)

    with open(test, 'w') as f:
        write_tree(f, root)

    with open(ans, 'w') as f:
        solution.solve(root, f)


shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, 41):
    gen_test(tests_dir, random.sample(range(1, i * 20), i * 3))

gen_test(tests_dir, [100])
gen_test(tests_dir, range(100))
gen_test(tests_dir, range(100, 0, -1))
