sentence = input().strip()
words = [word.lower() for word in sentence.split()]

dict = {}
for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
    
maxFrequency, maxFrequencyWord, minFrequency, minFrequencyWord = 0, None, 100000, None
for key in dict:
    if dict[key] > maxFrequency:
        maxFrequencyWord = key
        maxFrequency = dict[key]
    elif dict[key] == maxFrequency and key < maxFrequencyWord:
        maxFrequencyWord = key

    if (dict[key] < minFrequency):
        minFrequencyWord = key
        minFrequency = dict[key]
    elif dict[key] == minFrequency and key < minFrequencyWord:
        minFrequencyWord = key

print("Cuvantul care apare de cele mai multe ori este: {}".format(maxFrequencyWord))
print("Cuvantul care apare de cele mai putine ori este: {}".format(minFrequencyWord))
