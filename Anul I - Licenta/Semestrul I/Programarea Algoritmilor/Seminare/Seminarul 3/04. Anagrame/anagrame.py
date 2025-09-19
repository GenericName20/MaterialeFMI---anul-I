import os
path = os.path.dirname(__file__)
inputFileName = path + "/anagrame.in"
outputFileName = path + "/anagrame.out"

with open(inputFileName, "r") as f:
    firstWord = f.readline().strip()
    secondWord = f.readline().strip()

# O(log2n)
# with open(outputFileName, "w") as g:
#     if (sorted(firstWord) == sorted(secondWord)):
#         g.write("Anagrame!")
#     else:
#         g.write("Nu sunt anagrame!")

frequencyFirstWord = {letter: 0 for letter in firstWord}
for letter in firstWord:
    frequencyFirstWord[letter] += 1

frequencySecondWord = {letter: 0 for letter in secondWord}
for letter in secondWord:
    frequencySecondWord[letter] += 1

with open(outputFileName, "w") as g:
    if (frequencyFirstWord == frequencySecondWord):
        g.write("Anagrame!")
    else:
        g.write("Nu sunt anagrame!")