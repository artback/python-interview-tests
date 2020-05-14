import sys
def first_non_repeated(s):
    return findFirstDuplicate(s,checkNumberofSpecificLetterInString(s))

def checkNumberofSpecificLetterInString(s):
    d ={}
    for letter in s:
        d[letter] = 1 if letter not in d else d[letter]+1
    return d
def findFirstDuplicate(s,d):
    for letter in s: 
        if d[letter]==1: return letter 

print(first_non_repeated( sys.argv[1] ))
