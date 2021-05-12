#!/usr/bin/env python3
import random
import shutil
import os
from lib.graphs import task


simple_tests = [
    ("""4 4
0 1
1 2
2 3
3 0
""", "YES\n"),

    ("""3 2
0 1
1 2
""", "NO\n"),

    ("""1 0
""", "YES\n"),

    ("""2 1
0 1
""", "NO\n"),

    ("""6 6
0 1
2 1
0 2
3 4
4 5
5 3
""", "NO\n"),

    ("""6 7
0 1
2 1
0 2
3 4
4 5
5 3
0 5
""", "NO\n"),

    ("""6 7
0 1
2 1
0 2
3 4
4 5
5 2
2 3
""", "YES\n"),
]

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

t = 1
for q, a in simple_tests:
    test = os.path.join(tests_dir, '%.2d' % t)
    ans = test + '.a'
    with open(test, 'w') as f:
        f.write(q + "\n")

    with open(ans, 'w') as f:
        f.write(a)
    t += 1

for i in range(5):
    n = 2 + i * 2
    task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, i))
    t += 1

for i in range(5):
    n = 4 + i * 2
    task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 0))
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 100))
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 10000))
    t += 1