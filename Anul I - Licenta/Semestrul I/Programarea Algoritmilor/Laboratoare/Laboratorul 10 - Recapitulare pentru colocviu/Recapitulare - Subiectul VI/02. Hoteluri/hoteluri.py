# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/hoteluri.in"
# outputFileName = path + "/hoteluri.out"

inputFileName = "hoteluri.in"
outputFileName = "hoteluri.out"

def citire_date():
    with open(inputFileName, "r") as f:
        structura = {}
        for line in f.readlines():
            destinatie, cazare, distanta = line.split(";", maxsplit=2)
            destinatie = destinatie.split(":")[1].strip()
            cazare = cazare.split(":")[1].strip()
            distanta = float(distanta.split()[0].strip())
            print(destinatie, cazare, distanta)
            if destinatie not in structura:
                 structura[destinatie] = {}
            
            structura[destinatie][cazare] = distanta
    
    return structura

def cazare_centru(structura, *orase, distanta_max = 0.5):
    ans = []
    for oras in orase:
        if oras in structura:
            hoteluri = []
            for hotel in structura[oras]:
                if structura[oras][hotel] <= distanta_max:
                    hoteluri.append(hotel)
            if hoteluri != []:
                ans.append((oras, hoteluri))
        else:
            next

    return sorted(ans, key=lambda item:(-len(item[1]), item[0]))

def actualizeaza(structura, nume_oras, cazari):
    if nume_oras in structura:
        for key in cazari:
            if key in structura[nume_oras]:
                structura[nume_oras][key] = cazari[key]
            else:
                structura[nume_oras][key] = cazari[key]

    dmax = None
    for hotel in structura[nume_oras]:
        if dmax == None or structura[nume_oras][hotel] < dmax:
            dmax = structura[nume_oras][hotel]
            ans = [hotel]
        elif dmax == structura[nume_oras][hotel]:
            ans.append(hotel)

    return ans

def main():
    # Subtask A
    structura = citire_date()
    
    # Subtask B
    task_b1 = cazare_centru(structura, "Busteni", "Sinaia", "Azuga", "Acasa")
    print(task_b1)
    
    task_b2 = cazare_centru(structura, "Busteni", "Brasov", "Sinaia", "Azuga", distanta_max=1)
    print(task_b2)

    # Subtask C
    nume_oras = input().strip()
    nume_hotel = input().strip()
    distanta_noua = float(input().strip())

    task_c = actualizeaza(structura, nume_oras, {nume_hotel: distanta_noua})
    print(task_c)

    exit()

if __name__ == "__main__":
    main()
    exit(0)