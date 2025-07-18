# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/teatru.in"
# outputFileName = path + "/teatru.out"

inputFileName = "teatru.in"
outputFileName = "teatru.out"

def getInput():
    words = {}
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            emitent, reply = line.split(":", maxsplit = 1)
            
            import string
            for symbol in string.punctuation.replace("-", ""):
                reply = reply.replace(symbol, "")

            for word in reply.split():
                word = word.lower()
                if word not in words:
                    words[word] = {emitent}
                elif emitent not in words[word]:
                    words[word].add(emitent)
    
    return dict(sorted(words.items(), key=lambda item: (-len(item[1]), item[0])))

def computeFrequencies(words):
    with open(outputFileName, "w") as g:
        for word in words:
            g.write("{}: {}\n".format(word, ",".join([word for word in sorted(words[word])])))

    return

def main():
    words = getInput()
    computeFrequencies(words)
    return

if __name__ == "__main__":
    main()
    exit()