newEntry = input().strip()

# Task A & B
entries = []
scores = set()
entryIndex = 0
while (newEntry != "-1"):
    entryIndex += 1
    score, *fullName = newEntry.split()
    fullName = [name.capitalize() for name in fullName]

    if (len(fullName)):
        entries.append((int(score), " ".join(fullName), entryIndex))
        scores.add(int(score))

    newEntry = input().strip()

print("A) Intrarile din concurs: {}\nB) Scorurile obtinute: {}".format(entries, sorted(scores, reverse=True)))

# Task C
standings = {}
for entry in entries:
    if entry[0] not in standings:
        standings[entry[0]] = [entry]
    else:
        standings[entry[0]].append(entry)

standings = dict(sorted(standings.items(), key=lambda item: -item[0]))
print("C) Clasament\n")
for score in standings:
    print("Punctaj: {} | Concurenti: {}".format(score, standings[score]))