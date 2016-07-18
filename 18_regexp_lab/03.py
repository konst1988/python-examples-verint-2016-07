"""
Write a python program that takes a CSV file
reads it line by line and prints each line
with first and second columns reversed.

Sample input:
    Shana,Sargent,shanasargent@isoswitch.com
    Witt,Hampton,witthampton@zaphire.com
    Morgan,Grant,morgangrant@lotron.com

Sample output:
    Sargent,Shana,shanasargent@isoswitch.com
    Hampton,Witt,witthampton@zaphire.com
    Grant,Morgan,morgangrant@lotron.com
"""

import sys
import re

(_,filename) = sys.argv

with open(filename, "r") as f:
    for line in f:
        fields = re.search(r'^(.*),(.*),(.*)$',line)
        if fields == None:
            print "invalid line '{}'".format(line)
            continue
        print "{},{},{}".format(fields.group(2),fields.group(1), fields.group(3))