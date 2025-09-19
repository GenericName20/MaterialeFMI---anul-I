fullName = input().strip()

def checkNames(*names):
    for name in names:
        if (not name[0].isupper() or not name[1:].islower() or len(name) < 3):
            return 0
        for alpha in name:
            if not alpha.isalpha():
                return 0
            
    return 1

correct = None
try:
    lastName, otherNames = fullName.split()
    firstName, middleName = otherNames.split("-")
    print("Numele de familie: {}\nPrimul prenume: {}\nAl doilea prenume: {}\n".format(lastName, firstName, middleName))
    correct = checkNames(firstName, middleName, lastName)
except:
    try:
        lastName, firstName = fullName.split()
        print("Numele de familie: {}\nPrimul prenume: {}\n".format(lastName, firstName))
        correct = checkNames(firstName, lastName)
    except:
        correct = False

if (correct):
    print("Nume corect!")
else:
    print("Nume incorect!")