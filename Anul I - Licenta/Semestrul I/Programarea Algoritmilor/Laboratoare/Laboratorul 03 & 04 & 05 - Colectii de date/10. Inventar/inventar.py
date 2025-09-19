import os
path = os.path.dirname(__file__)
inputFileName = path + "/inventar.in"
outputFileName = path + "/inventar.out"

f = open(inputFileName, "r")
g = open(outputFileName, "w")

# Task A
stores = {}
for line in f.readlines():
    storeName,  *products = line.split()
    products = set(products)
    if storeName not in stores:
        stores[storeName] = products
    else:
        stores[storeName] = stores[storeName].union(products)

f.close()

# Task B
commonProducts = set(stores[next(iter(stores))])
for store in stores:
    commonProducts = commonProducts.intersection(stores[store])

g.write("B) Produsele care se gasesc in toate magazinele: {}\n".format(commonProducts if len(commonProducts) else "Nu exista"))

# Task C
allProducts = set()
for store in stores:
    allProducts = allProducts.union(stores[store])

g.write("C) Toate produsele din toate magazinele: {}\n".format(allProducts))

# Task D
for currentStore in stores:
    currentStoreStocks = set(stores[currentStore])
    for store in stores:
        if store != currentStore:
            currentStoreStocks = currentStoreStocks - stores[store]
    g.write("D) Magazinul {} are urmatoarele produce exclusiviste: {}\n".format(currentStore, currentStoreStocks if len(currentStoreStocks) else "N/A"))

g.close()
