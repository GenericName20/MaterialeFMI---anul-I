sentence = input().strip()

values = [int(word[1:]) for word in sentence.replace(","," ").split() if word[0] == '$']

# Task A
try:
    x, y = values[0], values[1]
    print(x, y)
except:
    "Nu s-au putut extrage primele doua valori!"

# Task B
try:
    x, y = values[-1], values[-2]
    if (x == y):
        print("Persoanele s-au inteles, iar tranzactia valoreaza ${}".format(x))
    else:
        print("Persoanele nu s-au inteles!")
except:
    "Nu s-au putut extrage ultimele doua valori!"
