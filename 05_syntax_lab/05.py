"""
Write a program that randomizes integers in a loop
until it finds a number that is divisable by: 7, 13 and 15
"""

from random import randint

while True:
    num = randint(1,1000000)
    if num % 7 == 0 and num % 13 and num % 15 == 0:
        print num
        break