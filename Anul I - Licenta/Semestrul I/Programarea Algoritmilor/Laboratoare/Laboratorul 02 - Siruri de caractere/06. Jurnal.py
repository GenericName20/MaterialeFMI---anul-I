sentence = input().strip()
words = [word for word in sentence.replace(",", " ").replace(".", " ").split()]

spent = 0
for i in range(len(words) - 1):
    if (words[i + 1].upper() == "RON"):
        try:
            spent += int(words[i])
        except:
            continue

print(spent)