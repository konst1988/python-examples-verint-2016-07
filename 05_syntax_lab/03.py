"""
Write a program that randomizes a number
and prints the sum total of its digits.
For example if the number was: 2345
The result should be: 14
"""

from random import randint
num = randint(1,10000)
print "num is:{}".format(num)
result = 0
while num > 0:
    digit = num % 10
    result += digit
    num /= 10;
print "sum of digits is:{}".format(result)