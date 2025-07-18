w1 = input().strip()
w2 = input().strip()

if (len(w1) != len(w2)):
    print("Cuvintele nu sunt anagrame")
    exit()

count = len(w1)
for i in range(len(w1)):
    for j in range(len(w2)):
        if (w1[i] == w2[j]):
            w2 = w2[:j] + w2[j + 1:]
            count -= 1
            break

if (count == 0):
    print("Cuvintele sunt anagrame!")
else:
    print("Cuvintele nu sunt anagrame!")

