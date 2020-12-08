from lib.testgen import TestSet
from lib import random

tests = TestSet()

# Public tests - no fun
tests.add("""3 2
1 2 1
2 3 2
2
1 2""", "YES")

tests.add("""
3 3
1 2 1
2 3 2
3 1 3
2
1 2""", "YES")

tests.add("""
3 3
1 2 1
2 3 2
3 1 3
2
2 3""", "NO")


# Private tests

########################################
# Two valid MSTs for graph in this group
tests.add("""
5 7
1 2 1
2 3 2
3 4 3
4 5 4
5 1 4
2 5 6
2 4 6
4
1 2 3 4""", "YES")

tests.add("""
5 7
1 2 1
2 3 2
3 4 3
4 5 4
5 1 4
2 5 6
2 4 6
4
1 2 3 5""", "YES")

# Too many edges in MST
tests.add("""
5 7
1 2 1
2 3 2
3 4 3
4 5 4
5 1 4
2 5 6
2 4 6
5
1 2 3 4 5""", "NO")

# Non-minimal
tests.add("""
5 7
1 2 1
2 3 2
3 4 3
4 5 4
5 1 4
2 5 6
2 4 6
4
1 2 3 6""", "NO")
########################################

tests.add("""
5 5
1 2 1
2 3 1
3 4 1
4 1 1
3 5 1
4
1 2 3 5""", "YES")

# Not all nodes included
tests.add("""
5 5
1 2 1
2 3 1
3 4 1
4 1 1
3 5 1
4
1 2 3 4""", "NO")

tests.add("""
6 7
1 2 1
2 3 1
1 3 1
4 5 1
5 6 1
4 6 1
3 4 1
5
1 2 4 5 7""", "YES")

# All nodes seen at least once, weight sum matches, but no connectivity
tests.add("""1
6 7
1 2 1
2 3 1
1 3 1
4 5 1
5 6 1
4 6 1
5
1 2 4 5 6""", "NO")

# Big loop, mst
N = 1000000
tests.add(f"""
{N} {N}
""" + "\n".join(f"{i} {i+1} 1" for i in range(1, N)) + f"\n1 {N} 2\n{N-1}\n" + " ".join(map(str, range(1, N))), "YES")

# Big loop, not mst
tests.add(f"""
{N} {N}
""" + "\n".join(f"{i} {i+1} 1" for i in range(1, N)) + f"\n1 {N} 2\n{N-1}\n" + " ".join(map(str, range(2, N+1))), "NO")

