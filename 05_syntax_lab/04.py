"""
Write a program that reads lines from the user
until an empty line is inserted.
After the user typed in an empty line,
print all previously inserted lines in reverse
order (from last to first)
"""

line = raw_input()
reverse = ""
while len(line) > 0:
    reverse = line + "\n" + reverse
    line = raw_input()
print reverse