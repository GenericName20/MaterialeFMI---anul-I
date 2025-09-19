import string
sentence = input().strip()
targetWord = input().strip()

for pct in string.punctuation:
    sentence = sentence.replace(pct, "")

targetWordFrequency = {}
for letter in targetWord:
    if letter not in targetWordFrequency:
        targetWordFrequency[letter] = 1

sameLettersWords = set()
for word in sentence.split():
    sameLetters = True
    for letter in word:
        if letter not in targetWordFrequency:
            sameLetters = False
            break
    if sameLetters:
        sameLettersWords.add(word)

if (len(sameLettersWords)):
    for i, word in enumerate(sameLettersWords):
        print("Cuvantul {}: {}".format(i, word))
else:
    print("Nu exista cuvinte cu proprietatea din cerinta!")