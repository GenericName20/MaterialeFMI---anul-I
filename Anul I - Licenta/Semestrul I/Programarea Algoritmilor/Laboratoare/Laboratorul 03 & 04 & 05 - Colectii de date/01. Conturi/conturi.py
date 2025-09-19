import os
path = os.path.dirname(__file__)
inputFileName = path + "/conturi.in"
outputFileName = path + "/conturi.out"
f = open(inputFileName, "r")
g = open(outputFileName, "w")

genericEmail = "@myfmi.unibuc.ro"
lineCount = 0
import random
import string
for line in f.readlines():
    lineCount += 1
    try:
        lastName, firstName = line.lower().split()
    except:
        print("Invalid output on line {}, skip...".format(lineCount))
        continue

    email = ".".join([firstName, lastName]) + genericEmail
    password = "".join(random.choices(string.ascii_uppercase) + [chr(random.randint(0, 25) + 97) for _ in range(0, 3)] + [str(random.randint(0, 9)) for _ in range(0, 4)])
    g.write(email + " " + password + "\n")

f.close()
g.close()
    