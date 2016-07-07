""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""
import os
import sys

(_, threshold, path) = sys.argv
for root, dirs, files in os.walk(path):
    for name in files:
        filename = root + "\\" + name
        size = os.stat(filename).st_size
        if size > int(threshold):
            print "filename:{} size: {}".format(name, size)
            delete = raw_input("Delete File Y\N:")
            if delete == "Y" or delete == "y":
                os.remove(filename)
                print "{} Deleted".format(filename)