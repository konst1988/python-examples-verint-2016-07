from collections import Counter
import sys

anagrams = []
#read all words from file
with open(sys.argv[1], 'r') as f:
    for line in f:
       word = line[:-1]
       wordCount = Counter(line[:-1])
       
       # see if same counter already appeared
       found = False
       for anagram in anagrams:
           if anagram[0] == wordCount :
               found = True
               print "{} {}".format(word, anagram[1])

        # Add to list if not found
       if not found:
            anagrams.append((wordCount, word))

