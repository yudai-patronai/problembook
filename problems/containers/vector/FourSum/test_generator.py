from lib.testgen import TestSet
from lib import random
tests = TestSet()

def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results

def make_test(low, high):
    randomlist = []
    for i in range(300, 500):
        n = random.randint(low, high)
        randomlist.append(n)

    N = random.randint(5*low, 5*high)
    result = map(lambda l: " ".join(map(str, l)), fourSum('', randomlist, N))
    k = str(len(randomlist)) + "\n" + " ".join(map(str, randomlist)) +"\n" +str(N), '\n'.join(map(str, result))
    return k

tests.add('0\n\n-5','')
tests.add('3\n-1 3 1\n-5','')
tests.add('9\n-83 92 -11 104 -51 98 -6 -48 67\n 95', '')
tests.add('1\n-28\n-21','')
tests.add('22\n-38 -31 40 81 42 25 21 -14 -83 81 45 -63 14 -94 -17 -46 76 -50 -6 -90 -27 -3\n106', '-50 -6 81 81\n -38 21 42 81\n -31 14 42 81\n -31 21 40 76\n -17 -3 45 81\n -14 -6 45 81\n -14 -3 42 81\n -14 14 25 81\n -6 25 42 45')
tests.add('10\n-5 -3 4 -2 -3 -4 -4 3 1 -5\n-5','-5 -5 1 4 \n-5 -4 1 3\n -4 -3 -2 4\n -3 -3 -2 3')
tests.add('7\n-3 5 5 4 2 -2 -4\n-5','-4 -3 -2 4')
tests.add('9\n1 1 1 0 1 0 -1 1 0\n2', '-1 1 1 1\n 0 0 1 1')
tests.add('9\n0 1 0 -1 1 1 0 0 0\n0','-1 0 0 1\n 0 0 0 0')
tests.add('8\n-27 89 -47 -58 -49 0 4 95\n95','')
tests.add('18\n-45 13 -71 -38 -97 63 52 82 75 -58 14 -96 -33 -90 93 39 -83 -36\n-57', '-97 -36 13 63\n-96 -38 14 63\n-90 -58 39 52\n-90 -33 14 52\n-71 -38 13 39\n-58 -45 -36 82\n-58 -38 -36 75')
tests.add('8\n97 -31 4 -25 28 -23 -20 -15\n80','-25 -20 28 97')
tests.add('14\n97 -31 4 -25 28 -23 -20 -15 97 -31 -25 28 -23 -20\n80', '-25 -20 28 97')
tests.add('18\n6 6 6 6 6 6 0 0 0 0 0 0 -6 -6 -6 -6 -6 -6\n0', '-6 -6 6 6\n-6 0 0 6\n0 0 0 0')
tests.add('19\n-31 -80 -13 -23 -11 -56 72 62 -64 -46 71 3 43 22 22 10 -27 -28 -30\n25', '-80 -28 62 71\n-56 -13 22 72\n-46 -23 22 72\n-46 -13 22 62\n-46 -11 10 72\n -31 -28 22 62\n-31 3 10 43\n-30 -27 10 72\n-27 -23 3 72\n-27 -13 3 62\n-27 -13 22 43\n-23 -13 -11 72')
tests.add(*make_test(-110, 110))
tests.add(*make_test(-200, 200))
tests.add(*make_test(-300, 300))
tests.add(*make_test(-1000, 1000))
tests.add(*make_test(-700, 700))
tests.add(*make_test(-50, 50))
tests.add(*make_test(-2000, 2000))

