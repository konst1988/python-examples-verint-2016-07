"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""
import sys
import math

while True:
    number = raw_input("Enter number:")
    if number == 0: sys.exit()
    try:
        result = math.sqrt(int(number))
        print "SQRT of {} is {}".format(number, result)
    except ValueError as e:
        print "Invalid number for sqrt. Error: {}".format(e.message)
    except Exception as e:
        print "Unknown Error occurred: {}".format(e.message)
