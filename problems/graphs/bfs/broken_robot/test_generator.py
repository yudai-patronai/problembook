from lib.testgen import TestSet

tests = TestSet()

# public tests
tests.add(
'''
3 3
0 0
2 0
...
##.
...
''',        
'-1')

tests.add(
'''
3 4
0 0
2 0
...#
##.#
....
''',        
'8')

# trivial
tests.add(
'''
3 3
0 0
2 2
...
...
...
''',        
'4')

tests.add(
'''
3 3
0 0
2 2
..#
.#.
#..
''',        
'-1')

tests.add(
'''
5 5
0 0
4 4
.....
.###.
.####
.###.
.....
''',        
'8')

tests.add(
'''
5 5
0 0
4 4
.....
.###.
####.
.###.
.....
''',        
'8')

# a bit more interesting
tests.add(
'''
5 5
1 1
1 3
#...#
..#.#
..#.#
..#.#
#....
''',
'10')

# not enough space, check all directions
tests.add(
'''
2 5
0 0
0 4
..#..
.....
''',        
'-1')

tests.add(
'''
2 5
1 0
1 4
.....
..#..
''',        
'-1')

tests.add(
'''
5 2
0 0
4 0
..
..
#.
..
..
''',        
'-1')

tests.add(
'''
5 2
0 1
4 1
..
..
.#
..
..
''',        
'-1')

# enough space/many paths, check all directions
tests.add(
'''
3 5
0 0
0 4
..#..
.....
.....
''',        
'8')

tests.add(
'''
3 5
2 0
2 4
.....
.....
..#..
''',        
'8')

tests.add(
'''
5 3
0 0
4 0
...
...
#..
...
...
''',        
'8')

tests.add(
'''
5 3
0 2
4 2
...
...
..#
...
...
''',        
'8')

# just some tests
tests.add(
'''
7 6
6 4
2 5
......
.####.
.#..#.
......
.#..#.
.####.
......
''',
'5')

tests.add(
'''
7 6
6 4
2 5
......
.####.
.#..#.
......
.#..#.
.#####
......
''',
'17')

tests.add(
'''
7 6
6 4
2 5
......
.####.
##..#.
......
.#..##
.####.
......
''',
'-1')

tests.add(
'''
8 6
7 4
1 5
......
......
.####.
.#..#.
......
.#..##
.####.
......
''',
'17')

# asymptotic: max graph
open_line = '.' * 1000
tests.add(
'''
1000 1000
0 0
999 999
''' + '\n'.join([open_line] * 1000),        
'1998')

# asymptotic: no way
no_way_field = '''
....
###.
#.#.
#...
'''
no_way_arr = no_way_field.strip().split('\n')
field = [open_line] * 996 + [open_line[:996] + ending for ending in no_way_arr]
tests.add(
'''
1000 1000
0 0
998 997
''' + '\n'.join(field),
'-1')
