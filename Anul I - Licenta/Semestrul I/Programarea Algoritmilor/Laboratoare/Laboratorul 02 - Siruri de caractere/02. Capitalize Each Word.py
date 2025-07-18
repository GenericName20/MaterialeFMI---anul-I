sentence = input().strip()

sentence = sentence[0].upper() + sentence[1:]
for i in range(1, len(sentence)):
    if (sentence[i].isalpha() and sentence[i - 1] == ' '):
        sentence = sentence[:i] + sentence[i].upper() + sentence[i + 1:]

print(sentence)