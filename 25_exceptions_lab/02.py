"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""
import sys

file = sys.argv[1]

try:
    with open(file, "rb") as fin:
        print (len(fin.readlines()))
except IOError as e:
    print "Failed to count lines of file: '{}'. Reason: {}".format(e.filename,e.strerror)
except Exception as e:
    print "Unknown Error occurred: {}".format(e.message)