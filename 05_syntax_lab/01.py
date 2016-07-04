#"""
#Write a program that reads 10 numbers from
#the user and prints the largest one
#"""
print "Enter 10 numbers:"
max = 0
for i in range(0,10):
    num = int(raw_input("Enter number[{}]:".format(i+1)))
    if num > max:
        max = num
print "max is:", max
