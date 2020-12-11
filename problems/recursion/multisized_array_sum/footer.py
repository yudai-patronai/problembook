

from test_collection import __manual_tests

# todo: verbose checker
test_index = int(input())
A = __manual_tests(test_index)[1]
print(multidim_sum(A))
