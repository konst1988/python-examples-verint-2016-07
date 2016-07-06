""" Write a program that takes a count
from sys.argv import and prints "Hello Python"
count times
"""

import sys

if len(sys.argv) > 1:
    count = sys.argv[1]
    for i in range(int(count)):
        print "Hello Python"
else:
    program_name = sys.argv[0]
    print "Usage: %s <count>" % program_name