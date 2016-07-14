"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""
import operator

def perform(action, *nums):
    return reduce(action, [x for x in list(nums[0]) if isinstance(x, int)])

def mysum(*nums):
    return perform(operator.add, nums)

def mymul(*nums):
    # add 1 just in case list is empty
    newNums = list(nums)
    newNums.append(1)
    return perform(operator.mul, newNums)

print mysum(10, 20,'hello', 30)
print mymul(10, 20, 30)
print mymul()