def getInput():
    text = input().strip().lower()
    if(len(text) == 0):
        print("Input invalid!")
        exit()
    else:
        return text, text[::-1]

def op(text1, text2):
    if(len(text1) < 2 and len(text2) < 2):
        if (text1[-1] == text2[0]):
            text1 = text2 = ""
        print(text1, text2)
        return (text1, text2)
    
    last = text1[-1]
    while (text1[-1] == last and len(text1) > 1):
        text1 = text1[:len(text1) - 1]
    while (text2[0] == last and len(text2) > 1):
        text2 = text2[1:]
    print(text1, text2)
    return (text1, text2)

def computeStrings(text1, text2):
    print(text1, text2)
    while (text1[-1] == text2[0]):
        text1, text2 = op(text1, text2)
        if(len(text1) < 2 or len(text2) < 2):
            break

    text1, text2 = op(text1, text2)
    return text1 + text2

def main():
    text, oglindit = getInput()

    # Text <op> Oglindit
    print("Text <op> Oglindit:")
    initRev = computeStrings(text, oglindit)
    print("Text <op> Oglindit (Rezultat): {}\n\n\n".format(initRev))

    # Olgindit <op> Text
    print("Oglindit <op> Text:")
    revInit = computeStrings(oglindit, text)
    print("Oglindit <op> Text (Rezultat): {}".format(revInit))

    if(revInit == initRev):
        print("Ambele operatii rezulta un sir vid!")
    else:
        print("Sirul mai lung este: {}".format(max(initRev, revInit)))

if __name__ == "__main__":
    main()