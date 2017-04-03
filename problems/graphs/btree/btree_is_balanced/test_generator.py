#!/usr/bin/env python3
import os
import random
import shutil
import sys
import solution
import math
from solution import Node, Tree

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
random.seed(100)

def rand_numbers(sequence, n):
    return [random.choice(sequence) for i in range(n)]

def gen_balanced_none_tree(h):
    if h == 0:
        return None

    n = Node(None)

    if h == 1:
        return n

    r = random.randrange(3)
    if r == 0:
        n.left = gen_balanced_none_tree(h-1)
        n.right = gen_balanced_none_tree(h-1)
    elif r == 1:
        n.left = gen_balanced_none_tree(h-2)
        n.right = gen_balanced_none_tree(h-1)
    else:
        n.left = gen_balanced_none_tree(h-1)
        n.right = gen_balanced_none_tree(h-2)

    return n


def tree_node_list(node):
    if node is None:
        return []

    ret = tree_node_list(node.left)
    ret.append(node)
    ret.extend(tree_node_list(node.right))

    return ret

def tree_rand_bfs(node):
    ret = []

    if node is None:
        return ret

    queue = [node]
    while queue:
        v = queue.pop(random.randrange(len(queue)))
        ret.append(v)
        if v.left is not None:
            queue.append(v.left)
        if v.right is not None:
            queue.append(v.right)

    return ret

def gen_balanced_tree(sequence):
    h = int(math.log2(len(sequence) + 1))
    tree = gen_balanced_none_tree(h)
    nodes = tree_node_list(tree)

    for n, x in zip(nodes, sorted(sequence)):
        n.data = x

    return tree


def gen_test(tests_dir, sequence, answer=None):
    if not hasattr(gen_test, 'ind'):
        gen_test.ind = 1
    else:
        gen_test.ind += 1

    print(gen_test.ind, len(sequence))

    test = os.path.join(tests_dir, '%.2d' % gen_test.ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(' '.join(map(str, sequence)) + '\n')

    with open(ans, 'w') as f:
        if answer is None:
            solution.solve(sequence, f)
        else:
            f.write(answer + '\n')


def gen_test_balanced(tests_dir, sequence):
    nodes = tree_rand_bfs(gen_balanced_tree(sequence))
    gen_test(tests_dir, [n.data for n in nodes], 'YES')


shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, 41):
    gen_test(tests_dir, random.sample(range(1, i * 20), i * 3))
    gen_test_balanced(tests_dir, random.sample(range(1, i * 20), i * 3))

gen_test(tests_dir, [100])
gen_test(tests_dir, range(100))
gen_test(tests_dir, range(100, 0, -1))
gen_test(tests_dir, [1] * 100)
gen_test(tests_dir, [1, 2, 3, 4, 5] * 100)

