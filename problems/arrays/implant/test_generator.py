from lib.testgen import TestSet

tests = TestSet()
tests.add("""6
1 0 6 3 2 3""",'MEOOOOW')

tests.add("""7
1 0 6 3 2 3 2""",'MEOOOOW')

tests.add("""5
1 0 6 3 2""",'')

tests.add("""12
3 3 2 2 1 1 0 0 0 0 0 0""",'left back')

tests.add("""11
3 3 2 2 1 1 0 6 3 2 3""",'left')

tests.add("""20
0 4 6 5 2 3 3 2 2 1 1 7 5 3 0 0 0 0 0 0""",'left back')

tests.add("""20
1 0 6 3 2 3 4 4 5 5 6 6 0 4 2 7 6 5 3 4""",'MEOOOOW right')
