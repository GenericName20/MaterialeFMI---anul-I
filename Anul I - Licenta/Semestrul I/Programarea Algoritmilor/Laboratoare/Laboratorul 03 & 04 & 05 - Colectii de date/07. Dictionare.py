firstCollection = {
    'tests': 12, 'grades': 20,'students': 15, 'courses': 10, 'resources': 12
}
secondCollection = {
    'children': 120, 'Students': 96, 'RESources': 69, 'SCHOOLS': 12
}

mainCollection = {}
for element in firstCollection:
    mainCollection[element.lower()] = firstCollection[element]

for element in secondCollection:
    if element.lower() not in mainCollection:
        mainCollection[element.lower()] = secondCollection[element]
    else:
        mainCollection[element.lower()] += secondCollection[element]

print(mainCollection)