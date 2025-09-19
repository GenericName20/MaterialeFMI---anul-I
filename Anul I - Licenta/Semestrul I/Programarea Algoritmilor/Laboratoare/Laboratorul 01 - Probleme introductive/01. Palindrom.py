number = input()
digits = [int(digit) for digit in number]
if (digits == digits[::-1]):
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")