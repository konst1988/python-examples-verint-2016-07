"""
Write a program that reads data
from property files.
Each line in the file can either be:
    An empty line
    A comment line (Start with #)
    A property line (of the form key = value)

Write a program that takes a property file name and key
as command line arguments and prints the requested value
"""
import sys
import re

(_,filename,key) = sys.argv

with open(filename, "r") as f:
    for line in f:
        if line[0] == '\n' or line[0] == '#': continue
        keyvalue = re.search(r'^(\w+)[ ]*=[ ]*(\w+)$',line)
        if keyvalue == None:
            print "'{}' is not a key value line".format(line)
        elif keyvalue.group(1) == key:
            print "{} is {}".format(keyvalue.group(1), keyvalue.group(2))
    print "key '{}' not found".format(key)