sentence = input().strip()

upper, lower, punctuation = 0, 0, 0
for character in sentence:
    if (character.isalpha()):
        lower += character.islower()
        upper += character.isupper()
    elif (character != " "):
        punctuation += 1

print("Litere mici: {}\nLitere mari: {}\nSemne de punctuatie: {}".format(lower, upper, punctuation))