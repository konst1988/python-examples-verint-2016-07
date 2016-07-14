"""
Write a function that takes minlen and
a list of words, and returns only the words
longer than minlen
"""
def longer_than(length, *strings):
    return [s for s in strings if len(s) > length ]

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')