referenceWord = input().strip()
referenceLength = len(referenceWord)
sentence = input().strip()

words = set([word for word in sentence.split()])
words = sorted(words)

sameLength = []
for word in words:
    if referenceLength == len(word):
        sameLength += [word]

print("Cuvintele cu aceeasi lungime ca {} sunt: {}".format(referenceWord, sameLength))