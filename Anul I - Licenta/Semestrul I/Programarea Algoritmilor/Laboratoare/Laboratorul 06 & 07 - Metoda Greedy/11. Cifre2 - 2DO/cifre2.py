



# PROTOTIP (Nefunctional)
# Pentru editorul de text
import os
path = os.path.dirname(__file__)
inputFileName = path + "/cifre2.in"
outputFileName = path + "/cifre2.out"

# inputFileName = "cifre2.in"
# outputFileName = "cifre2.out"

with open(inputFileName, "r") as f:
    digitsNumber, k = [int(var) for var in f.readline().split()]
    digits = sorted(f.readline().split())

numbers = []

# Cautam cel mai mare numar divizibil cu K (fakeValue)
fakeValue = digitsNumber
while fakeValue % k != 0:
    fakeValue += 1

# Distribuim egal numarul de cifre pentru fiecare numar
for _ in range(k):
    numbers.append([fakeValue // k, 0])

# Reglam numarul de cifre al numerelor, scazand 1 din ultimele abs(fakeValue - digitsNumber) numere care se vor forma
for i in range(-1, digitsNumber - fakeValue - 1, -1):
    numbers[i][0] -= 1

zeros = digits.count("0")
while "0" in digits:
    digits.remove("0")
digitsNumber = len(digits)

digits = digits[:k] + [0] * zeros + digits[k:]
print(digits)

with open(outputFileName, "w") as g:
    g.write("{}".format(sum))