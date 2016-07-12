"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one
"""

import sys

(src, dst) = sys.argv[1:]
bufsize = 64

with open(src, "rb") as fin:
    with open(dst, "ab") as fout:
        data = fin.read(bufsize)
        while data != "":
            fout.write(data)
            data = fin.read(bufsize)