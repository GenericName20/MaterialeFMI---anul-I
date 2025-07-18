import os
path = os.path.dirname(__file__)
inputFileName = path + "/persoane.in"
outputFileName = path + "/persoane.out"

persons = []
citizens = {}

import string
f = open(inputFileName, "r")
for line in f.readlines():
    person = {'adresa':{}}
    
    for symbol in ["{", "}", "adresa:"]:
        line = line.replace(symbol, "")

    valuePairs = [pairs for pairs in line.strip().split(",")]

    for pair in valuePairs:
        try:
            key, value = pair.split(":")
            if (key == "nume" or key == "prenume"):
                person[key] = value.capitalize()
            else:
                person['adresa'][key] = value.capitalize()
        except:
            continue

    if person['adresa']['oras'] not in citizens:
        citizens[person['adresa']['oras']] = [(person['nume'], person['prenume'])]
    else:
        citizens[person['adresa']['oras']].append((person['nume'], person['prenume']))
   
    persons.append(person)

f.close()
    
g = open(outputFileName, "w")

g.write("\nTask A:\n")
for person in persons:
    g.write(str(person) + "\n")

g.write("\nTask B:\n")
for city in citizens:
    g.write("In orasul {} traiesc cetatenii: {}\n".format(city, [(nume, prenume) for (nume, prenume) in citizens[city]]))
g.close()