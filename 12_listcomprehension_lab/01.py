"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

numbers = range(97, 97+26)
letters = [chr(x) for x in numbers]
print letters

