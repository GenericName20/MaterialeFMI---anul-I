import os
path = os.path.dirname(__file__)
inputFileName = path + "/anagrame.in"
outputFileName = path + "/anagrame.out"

def anagram(firstWord, secondWord):
    v = [[0, 0] for _ in range(26)]

    for letter1, letter2 in zip(firstWord, secondWord):
        v[ord(letter1) - 97][0] += 1
        v[ord(letter2) - 97][1] += 1

    for letter1, letter2 in v:
        if (letter1 != letter2):
            return False
        
    return True

with open(inputFileName, "r") as f:
    firstWord = f.readline().strip().lower()
    secondWord = f.readline().strip().lower()

answer = False if len(firstWord) != len(secondWord) else anagram(firstWord, secondWord) 

with open(outputFileName, "w") as g:
    g.write("{}".format("Anagrame" if answer else "Nu sunt anagrame"))