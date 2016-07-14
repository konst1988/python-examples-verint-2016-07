"""
Write a function groupby that takes a list
and a function and returns a dictionary
keyd by the return value of the function on the list items

For example:
    groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])
    returns: { 'f': ['foo','fi'], 'h': ['hello', 'hi'] }
"""

from collections import defaultdict

def groupby(func, lst):
    result = defaultdict(list)
    for item in lst:
        key = func(item)
        result[key].append(item)
    return result

print groupby(lambda s: s[0], ['foo', 'fi', 'hello', 'hi'])