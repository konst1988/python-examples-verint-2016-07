""" Write a program that selects a random number
and asks the user to guess it.

After each guess print a hint "too large" or "too small" to the user.

Bonus: To make things interesting, the program should cheat once in a white
"""

from random import randint

num = randint(1,100)
guess = 0
while guess != num:
    guess = int(raw_input("Guess a number:"))
    
    if guess > num:
        isSmaller = True
    elif guess < num:
        isSmaller = False
    #add cheating
    if guess != num:
        isCheat = randint(1,10) == 10
        if isCheat:
            isSmaller = not isSmaller
            #print "Cheating.."
        if isSmaller:
            print "Smaller"
        else:
            print "Bigger"

print "Correct!"