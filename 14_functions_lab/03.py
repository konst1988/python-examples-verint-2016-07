"""
Write a function that calculates the sum
of the 10th digit from all arguments passed to it
"""

def sum10th(*nums):
    return sum([int(str(x)[-2]) for x in nums])

print sum10th(1120, 220, 140)