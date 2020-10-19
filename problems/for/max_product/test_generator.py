from lib import random
from lib.testgen import TestSet

random.seed(42)


def write_test(nums:list, tests:TestSet):
    unsorted_nums = nums.copy()
    
    nums.sort()
    ans = nums[0]*nums[1] if nums[0]*nums[1] >= nums[-2]*nums[-1] else nums[-2]*nums[-1]
    
    tests.add(
        str(len(nums))+'\n'+'\n'.join(map(str, unsorted_nums)) + '\n',
        str(ans)+'\n'
    )


tests = TestSet()

write_test([6, 0, 3, 7, 1], tests)
write_test([-4, 5, 2, -4, 1, 2, 7], tests)
write_test([-2, 2, -3, -1, -5, 7], tests)
write_test([0, 0], tests)

for _ in range(5):
    count = random.randint(2, 10000)
    nums = [random.randint(-10000, 10000) for _ in range(count)]
    write_test(nums, tests)
