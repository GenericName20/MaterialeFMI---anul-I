try:
    x, y = map(int, input().split())
except:
    print("Numar incorect de valori / Format gresit!")
    exit()

x = x ^ y
print("x = x ^ y -> x = {}, y = {}".format(x, y))
y = x ^ y
print("y = x ^ y -> x = {}, y = {}".format(x, y))
x = x ^ y
print("x = x ^ y -> x = {}, y = {}".format(x, y))