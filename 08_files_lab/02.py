"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name
Program should write the lines from the first two 
files interwinded into the output file
"""
import itertools
import sys

(_,srcA, srcB, dst) = sys.argv

with open(srcA, "r") as a:
    with open(srcB, "r") as b:
        with open(dst, "w") as c:
            for item in itertools.izip_longest(a,b, fillvalue=""):
                c.write(item[0])
                c.write(item[1])




