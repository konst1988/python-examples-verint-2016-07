"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""

print "Enter 10 numbers:"
max = int(raw_input("Enter number[1]:"))
for i in range(1,9):
    num = int(raw_input("Enter number[{}]:".format(i+1)))
    if num > max:
        max = num
print "max is:", max
