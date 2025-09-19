def e(x, k):
    if (ord(x) >= 65 and ord(x) <= 90):
        c = 65
    else:
        c = 97
    return chr(((ord(x) - c + k) % 26) + c)

def d(x, k):
    if (ord(x) >= 65 and ord(x) <= 90):
        c = 65
    else:
        c = 97
    return chr(((ord(x) - c - k) % 26) + c)

def encrypt(sentence, key):
    newSentence = []
    for i in range(len(sentence)):
        if (sentence[i].isalpha()):
            newSentence += e(sentence[i], key)
        else:
            newSentence += sentence[i]
    newSentence = "".join(newSentence)
    return newSentence

def decrypt(sentence, key):
    newSentence = []
    for i in range(len(sentence)):
        if (sentence[i].isalpha()):
            newSentence += d(sentence[i], key)
        else:
            newSentence += sentence[i]
    newSentence = "".join(newSentence)
    return newSentence

sentence = input().strip()
key = int(input())

encryptedSentence = encrypt(sentence, key)
print(encryptedSentence)

decryptedSentence = decrypt(encryptedSentence, key)
print(decryptedSentence)