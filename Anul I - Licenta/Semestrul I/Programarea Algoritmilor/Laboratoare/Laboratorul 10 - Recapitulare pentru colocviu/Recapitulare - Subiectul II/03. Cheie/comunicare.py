# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/comunicare.in"
# outputFileName = path + "/comunicare.out"

inputFileName = "comunicare.in"
outputFileName = "comunicare.out"

def citire_date(inputFileName):
    messages = {}
    with open(inputFileName, "r") as f:
        secretKey = f.readline().strip()
        messages['secretKey'] = secretKey

        for line in f.readlines():
            emitent, message, hour = line.split()
            emitent = emitent.strip().capitalize()
            if emitent not in messages:
                messages[emitent] = [(message, hour)]
            else:
                messages[emitent].append((message, hour))

    return messages

def decodificare(message, secretKey):
    secretKey = {character: chr(index + 97) for index, character in enumerate(secretKey)}

    return "".join([secretKey[letter] if letter in secretKey else letter for letter in message])

def reconstituire(messages):
    def sortKey(item):
        return item[1]
    
    messages_a = [(decodificare(message[0], messages['secretKey']), message[1]) for message in messages['A']]
    messages_a = " ".join([message[0] for message in sorted(messages_a, key=sortKey)])

    messages_b = [(decodificare(message[0], messages['secretKey']), message[1]) for message in messages['B']]
    messages_b = " ".join([message[0] for message in sorted(messages_b, key=sortKey)])
    
    with open(outputFileName, "w") as g:
        g.write("A : {}\nB : {}".format(messages_a, messages_b))
    
    return

def main():
    messages = citire_date(inputFileName)
    reconstituire(messages)
    return

if __name__ == "__main__":
    main()
    exit()