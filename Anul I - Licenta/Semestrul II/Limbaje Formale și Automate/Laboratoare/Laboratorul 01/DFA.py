# Automat care parcurge o fraza.
# Pur exeperimental.
subjects = ["Maria"]
predicates = ["merge", "cumpara"]
objects = ["magazin", "doua", "mere"]
separators = ["si", "la"]
terminators = ". ! ?".split()

def isSubject(a):
    return a in subjects

def isPredicate(a):
    return a in predicates

def isObject(a):
    return a in objects

def isSeparator(a):
    return a in separators

def isTerminator(a):
    return a in terminators

# Automat de forma
# M = (Q, S, d, q, F)

# Starile
Q = ["currentSentence", "newSentence", "endSentence"]

# Alfabetul
S = [isSubject, isPredicate, isObject, isSeparator, isTerminator]

# Tranzitiile
d = {state: {} for state in Q}

# Starea initiala
q = Q[0]

# Starile finale
F = [Q[2]] 

# Input
import string
rInit = "Maria cumpara doua mere si merge la magazin."
for s in string.punctuation:
    rInit = rInit.replace(s, " "+s)

r = rInit.split()

# Tranzitiile (poate fi minimizat)
d["currentSentence"]["subject"] = "currentSentence"
d["currentSentence"]["predicate"] = "newSentence"
d["currentSentence"]["object"] = "currentSentence"
d["currentSentence"]["separator"] = "currentSentence"
d["currentSentence"]["terminator"] = "endSentence"
d["newSentence"]["subject"] = "currentSentence"
d["newSentence"]["predicate"] = "newSentence"
d["newSentence"]["object"] = "currentSentence"
d["newSentence"]["separator"] = "currentSentence"
d["newSentence"]["terminator"] = "endSentence"

# DFA
for word in r:
    print(f"Processing word: {word}")
    states = []
    
    # Determina categoria fiecarui cuvant
    for i, func in enumerate(S):
        if func(word):
            state = ["subject", "predicate", "object", "separator", "terminator"][i]
            states.append(state)
    
    print(f"Categorii: {states}")
    
    for state in states:
        if state in d[q]:
            q = d[q][state]
            print(f"Tranzitie la starea: {q}")
        else:
            print(f"Nu exista tranzitie de la starea '{state}' la starea '{q}'")

    if q == "endSentence":
        print("Sentence ended.")
        break
