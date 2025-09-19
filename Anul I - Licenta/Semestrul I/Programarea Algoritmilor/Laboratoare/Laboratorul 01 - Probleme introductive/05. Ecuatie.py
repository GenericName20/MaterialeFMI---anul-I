try:
    a, b, c = map(int, input().split())
except:
    print("Numar incorect de valori / Format incorect!")
    exit()

delta = b ** 2 - 4 * a * c
match delta:
    case delta if delta < 0:
        print("Ecuatia nu are nicio radacina")

    case delta if delta == 0:
        from math import sqrt
        x = (-b + sqrt(delta)) / (2 * a)
        print(x)

    case delta if delta > 0:
        from math import sqrt
        x1, x2 = round((-b + sqrt(delta)) / (2 * a), 2), round((-b - sqrt(delta)) / (2 * a), 2)
        print(x1, x2)