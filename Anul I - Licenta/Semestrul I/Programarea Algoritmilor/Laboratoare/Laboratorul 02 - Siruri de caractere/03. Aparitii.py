# Nu putem folosi replace(), deoarece daca un cuvant apare ca subsecventa in alt cuvant,
# acesta va fi modificat si nu va mai avea sens propozitia

sentence = input().strip()
oldString = input().strip()
newString = input().strip()

words = [word for word in sentence.split()]
for i in range(len(words)):
    if (words[i] == oldString):
        words[i] = newString

newSentence = " ".join(words)
print(newSentence)


