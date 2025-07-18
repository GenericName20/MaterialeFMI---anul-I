def task_a(digits):
    digits.sort(reverse = True)
    return int("".join(digits))

def task_b(digits):
    digits.sort()
    zeros = digits.count("0")
    new_number = "".join([digits[zeros]] + digits[:zeros] + digits[zeros + 1:])
    return int(new_number)

number = input()
digits = [digit for digit in number]

largest, smallest = task_a(digits), task_b(digits)
print("Cel mai mare: {}\nCel mai mic: {}".format(largest, smallest))

