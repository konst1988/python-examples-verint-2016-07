"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one
"""

import sys

(src, dst) = sys.argv[1:]

with open(src, "r") as fin:
    with open(dst, "a") as fout:
        for line in fin:
            fout.write(line.title())
            