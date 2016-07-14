"""
Write a function that takes two arguments: 
    A string
    And a number
If wrong types were passed in, raise an exception
"""
import numbers

def test(str,num):
    if not isinstance(str, basestring): raise Exception("str must be string")
    if not isinstance(num ,numbers.Number) : raise Exception("num must be a number")

test("uy","uu")

