text_a = "Python features sequence unpacking where multiple expressions, each evaluating to anything that can be assigned (to a variable, writable property, etc.) are associated in an identical manner to that forming tuple literals—and, as a whole, are put on the left-hand side of the equal sign in an assignment statement. The statement expects an iterable object on the right-hand side of the equal sign that produces the same number of values as the provided writable expressions; when iterated through them, it assigns each of the produced values to the corresponding expression on the left."
# sentences = input().strip()

# Task A
sentences = [sentence.strip() for sentence in text_a.split(".") if sentence != ""]
for i in range(0, len(sentences)):
    try:
        if (not sentences[i][0].isupper()):
            sentences[i - 1] += ". " + sentences[i]
            sentences.remove(sentences[i])
    except: 
        break

for i in range(len(sentences)):
    sentences[i] += "."

print("Task A:")
try:
    sentences.remove("")
    print("Propozitiile sunt OK!")
except:
    print("Propozitiile sunt OK!")
for (i, sentence) in enumerate(sentences):
    print("Propozitia {}: {}".format(i + 1, sentence))

# Task B
text_b = "Salut... bine ai venit. Hai sa bem... de ce nu. Apropo, eu sunt Vlad aka. panseluta."
sentences = []
last = 0
for i in range(len(text_b)):
    if (text_b[i].isupper() and text_b[i - 2] == "."):
        sentences += [text_b[last:i]]
        last = i

# Adaugam ultima propozitie din sir
sentences += [text_b[last:len(text_b)]]

print("\nTask B:")
try:
    sentences.remove("")
    print("Propozitiile sunt OK!")
except:
    print("Propozitiile sunt OK!")

for (i, sentence) in enumerate(sentences):
    print("Propozitia {}: {}".format(i + 1, sentence))