""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) > 2:
    (_, strnum1, strnum2) = sys.argv
    num1 = int(strnum1)
    num2 = int(strnum2)
    print "{} + {} = {}".format(num1, num2, num1+num2)
else:
    program_name = sys.argv[0]
    print "Usage: %s <num1> <num2>" % program_name
    