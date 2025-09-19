sentence = input().strip()
wrong = input().strip()
correct = input().strip()

correctedSentence = " ".join(sentence.replace(wrong, correct).split()).strip()
print(correctedSentence)