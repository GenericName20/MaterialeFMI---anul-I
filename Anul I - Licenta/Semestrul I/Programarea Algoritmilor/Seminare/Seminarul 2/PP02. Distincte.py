sentence = input().strip()
import string
for symbol in string.punctuation:
    sentence = sentence.replace(symbol, "")

wordCount = len(set([word for word in sentence.split()]))
print("Numarul de cuvinte distincte este: {}".format(wordCount))