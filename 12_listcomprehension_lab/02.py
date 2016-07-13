numbers = range(97, 97+26)
letters = [chr(x) for x in numbers]

combination = [a+b+c for a in letters for b in letters for c in letters]
print combination