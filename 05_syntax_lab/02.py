"""
Write a Python program that randomizes 7 numbers
and prints their sum total.
If the sum is divisable by 7, also print the word "Boom"
"""

from random import randint
sum = 0
for i in range(0,10):
    num = randint(1,100)
    print "generated num:" ,num
    sum+=num
    

print "sum is {}".format(sum)
if sum % 7  == 0:
        print "BOOM!"