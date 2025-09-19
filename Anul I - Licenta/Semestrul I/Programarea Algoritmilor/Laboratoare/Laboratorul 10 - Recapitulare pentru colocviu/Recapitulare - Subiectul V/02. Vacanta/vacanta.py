import os
path = os.path.dirname(__file__)
inputFileName = path + "/vacanta.in"
outputFileName = path + "/vacanta.out"

def citire_date(fileName):
    cazari = {}
    with open(fileName, "r") as f:
        for line in f.readlines():
            if line.startswith("Destinatie"):
                gbg, locatie = [word.strip() for word in line.split(":")]
                if locatie not in cazari:
                    cazari[locatie] = {}
            else:
                hotel, stele, gbg, rating = [word.strip() for word in line.rsplit(maxsplit=3)]
                cazari[locatie][hotel] = (int(stele), float(rating))
    
    return cazari

def recomandari(cazari, *orase, nr_stele_min = 0, scor_min = 0):
    ans = []
    for oras in orase:
        if oras in cazari:
            hoteluri = []
            for hotel in cazari[oras]:
                if cazari[oras][hotel][0] >= nr_stele_min and cazari[oras][hotel][1] >= scor_min:
                    hoteluri.append(hotel)
            if hoteluri != []:
                ans.append((oras, hoteluri))
        else:
            next

    return sorted(ans, key=lambda item: (-len(item[1]), item[0]))

def act_recenzii(cazari, nume_oras, recenzii: dict):
    for key in recenzii:
        if key in cazari[nume_oras]:
            temp = [value for value in cazari[nume_oras][key]]
            temp[1] = (temp[1] + recenzii[key]) / 2
            cazari[nume_oras][key] = tuple(temp)
        else:
            next

    L, rmax = [], -1000
    for hotel in cazari[nume_oras]:
        if cazari[nume_oras][hotel][1] > rmax:
            rmax = cazari[nume_oras][hotel][1]
            L = [hotel]
        elif cazari[nume_oras][hotel][1] == rmax:
            L.append(hotel)
    
    return L

def main():
    # Cerinta A)
    cazari = citire_date(inputFileName)
    
    # Cerinta B)
    task_b1 = recomandari(cazari, "Busteni", "Sinaia", "Predeal", "Brasov")
    print(task_b1)

    task_b2 = recomandari(cazari, "Busteni", "Sinaia", "Predeal", "Brasov", nr_stele_min=4)
    print(task_b2)

    # Cerinta C)
    nume_oras = input().strip()
    nume_unitate = input().strip()
    scor = float(input().strip())
    task_c = act_recenzii(cazari, nume_oras, {nume_unitate: scor})
    print(task_c)

if __name__ == "__main__":
    main()
    exit(0)