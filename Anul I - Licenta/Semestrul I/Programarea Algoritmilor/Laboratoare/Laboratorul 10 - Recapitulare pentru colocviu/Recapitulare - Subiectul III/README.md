# Model 3
## Problema 1 [4 pct]

### Enunt
Fișierul text `teatru.in` conține, pe mai multe linii, un fragment dintr-o piesă de teatru, respectiv pe fiecare linie se află câte o replică a unui personaj, sub forma `personaj: replică`. Numele unui personaj poate fi format din mai multe cuvinte, iar o replică nu va conține niciodată caracterul `':'`. Să se scrie în fișierul text `teatru.out` cuvintele din fragmentul dat grupate în funcție de numărul personajelor care le-au pronunțat, conform modelului din exemplul de mai jos. Cuvintele vor fi scrise în ordinea descrescătoare a numărului de personaje care le-au pronunțat, iar în caz de egalitate se vor scrie în ordine alfabetică. Pentru fiecare cuvânt, numele personajele care l-au pronunțat vor fi ordonate alfabetic. Fiecare cuvânt va fi scris o singură dată și nu se va face distincție între litere mici și litere mari.

### Exemplu

| `teatru.in`                                                                                                                                                                                                        | `teatru.out`                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tipatescu: Misel!<br>Pristanda: Curat misel!<br>Tipatescu: Murdar!<br>Pristanda: Curat murdar!<br>Tipatescu: Ei! Nu s-alege!<br>Pristanda: Nu s-alege!<br>Farfuridi: Vrei sa vorbesc curat si deslusit, stimabile? | curat: Farfuridi,Pristanda<br>misel: Pristanda,Tipatescu<br>murdar: Pristanda,Tipatescu<br>nu: Pristanda,Tipatescu<br>s-alege: Pristanda,Tipatescu<br>deslusit: Farfuridi<br>ei: Tipatescu<br>sa: Farfuridi<br>si: Farfuridi<br>stimabile: Farfuridi<br>vorbesc: Farfuridi<br>vrei: Farfuridi |

Rezolvare
```py
pj_by_cuv = {}

with open("teatru.in") as input_file:
    for line in input_file:
        personaj, replica = line.strip().split(":", maxsplit=1)
        personaj = personaj.strip()

        for x in ",.;!?":
            replica = replica.replace(x, " ")
        cuvinte = replica.split()
        for x in cuvinte:
            x = x.lower()
            if x not in pj_by_cuv:
                pj_by_cuv[x] = {personaj}
            else:
                pj_by_cuv[x].add(personaj)

pj_by_cuv = sorted(pj_by_cuv.items(), key=lambda x : (-len(x[1]), x[0]))

with open("teatru.out", 'w') as output_file:
    for cuvant, pers in pj_by_cuv:
        pers_to_print = ",".join(sorted(pers))
        output_file.write(f"{cuvant}: {pers_to_print}\n")
```

## Problema 2 [3 pct]

### Enunt
a) [0.5 pct] Scrieți o funcție `citire_matrice` care primește un parametru reprezentând numele unui fișier care conține elementele unei matrice pătratice de $$n \times n$$ de numere întregi cu următoarea structură:

- pe prima linie a fișierului este $$n$$
- pe a doua linie sunt $$n \times n$$ numere separate prin câte un spațiu reprezentând elementele matricei transformate în vector prin concatenarea liniilor matricei de la prima la ultima; astfel primele n numere de pe linie sunt elementele primei linii din matrice, urmate de elementele celei de a doua linii etc.

Funcția citește elementele matricei din fișierul cu numele dat ca parametru și returnează matricea cu aceste elemente. Pentru fișierul `"matrice.in"` din exemplul de mai jos matricea este:

    1 2 3
    4 5 6
    7 8 9

b) [1.5 pct] Scrieți o funcție duplicare care primește ca parametri (în această ordine): o matrice (listă de liste) și un număr variabil de numere naturale reprezentând indici ai liniilor din matrice (indicele primei linii din matrice este 0) și inserează după fiecare linie cu indicele dat ca parametru o copie a ei (duplică linia). Funcția va modifica matricea primită ca parametru.

c) [1 pct] Se dă fișierul `matrice.in` cu structura descrisă la punctul a). Folosind apeluri utile ale funcțiilor de la a) și b) să se citească matricea din fișierul `matrice.in`, să se modifice această matrice duplicând prima și a doua linie (după prima linie se va insera o linie egală cu ea, la fel și după a doua) și adăugând apoi 1 la primul element de pe prima linie. Să se afișeze pe ecran matricea obținută.

### Exemplu

| `matrice.in`           | `consola (iesire pe ecran)`               |
| ---------------------- | ----------------------------------------- |
| 3<br>1 2 3 4 5 6 7 8 9 | 2 2 3<br>1 2 3<br>4 5 6<br>4 5 6<br>7 8 9 |

### Rezolvare

```py
import copy


# Subpuctul a)
def citire_matrice(file_name):
    mat = []
    with open(file_name) as file:
        n = int(file.readline().strip())
        values = [int(x) for x in file.readline().strip().split()]
        for i in range(n):
            mat.append(values[i * n : (i + 1) * n])
    return mat

# Subpunctul b)
def duplicare(mat, *linii):
    for linie in sorted(linii, reverse=True):
        ln = copy.copy(mat[linie])
        mat.insert(linie + 1, ln)

# Subpunctul c)
def print_mat(mat):
    for line in mat:
        print(" ".join([str(x) for x in line]))

def main():
    mat = citire_matrice("matrice.in")
    duplicare(mat, 0, 1)
    mat[0][0] += 1
    print_mat(mat)

if __name__ == "__main__":
    main()
```

## Problema 3 [4 pct]

### Enunt
Se consideră fișierul text note.in cu următoarea structură:

- pe prima linie apar, despărțite prin spațiu, numărul $$n$$ reprezentând numărul de elevi dintr-o clasă a unui liceu și numărul $$m$$ reprezentând numărul de materii
- pe următoarele linii avem informații despre cei $$n$$ elevi; pentru fiecare elev informația are următoarea structură:
    - linie de forma `<șir de caractere>` reprezentând numele elevului
    - urmată de $$m$$ linii care conțin notele elevului (numere naturale nenule) la cele $$m$$ materii, fiecare având următoarea structură: 
        `<nume_materie>,<nota_1>,<nota_2>,...,<nota_k>`

### Observații:

- Materiile nu apar în aceeași ordine la toți elevii, dar toți elevii din clasă au același număr de materii. Denumirile materiilor nu conțin caracterul ',' (virgula).
- Numărul de note este variabil, dar nenul.
- Dacă un elev are o singură notă la o materie sau media este strict mai mică decât 5, acesta va avea media egală cu 0 și va rămâne corigent.

### Exemplu fisier de intrare

    5 3
    Ana Maria Pop
    Matematica,10,9,9,10,10
    Limba romana,8,9,9,8
    Fizica,10,9,7,10,10
    Mihai Popescu
    Fizica,10,10
    Matematica,9,7,10,10
    Limba romana,8,3,5,10
    Andrei Mincu
    Matematica,10,9,2
    Fizica,3,7,9
    Limba romana,5,4
    Ioana Matei
    Fizica,10,10
    Limba romana,9,9,10,10
    Matematica,10,10,10,9
    Alin Enache
    Limba romana,10,10,10
    Matematica,10,10,10,10
    Fizica,10

### Cerinte
a) [2 pct] Scrieți o funcție care citește datele din fișierul `note.in` și returnează o structură de date cu informațiile din fișier. Folosiți o structură de date convenabilă pentru a rezolva eficient subpunctele următoare.

b) [1 pct] Scrieți o funcție `despre_elev` care primește structura definită la punctul anterior și un șir de caractere (numele elevului) și returnează o listă care conține tupluri de forma (nume_materie, medie). Se va citi de la tastatură numele unui elev și se vor afișa pe ecran mediile acestuia (rotunjite cu două zecimale) la fiecare materie (sortate descrescător după medie). Dacă numele introdus nu apărea în catalog, se va afișa un mesaj corespunzător.

| `Intrare tastatură` | `Afișare pe ecran`                                 |
| -------------------- | --------------------------------------------------- |
| Ana Maria Pop        | Matematica 9.60<br>Fizica 9.20<br>Limba romana 8.50 |

c) [1 pct] Scrieți o funcție `adauga_nota` care primește structura definită la punctul a), două șiruri de caractere (numele elevului și materia) și un număr variabil de numere naturale reprezentând note ale elevului la acea materie și adaugă în structură notele primite ca parametru la materia respectivă pentru acel elev. Se vor citi de la tastatură numele unui elev, materia și două note și se va afișa pe ecran noua medie a acestuia la materia citită

| `Intrare tastatură`       | `Afișare pe ecran` |
| -------------------------- | ------------------- |
| Ana Maria Pop Fizica 10 10 | Fizica 9.43         |

### Rezolvare

```py
def citire():
    with open("note.in") as f:
        date_elevi = dict()
        n, m = [int(x) for x in f.readline().split()]

        for i in range(n):
            nume_elev = f.readline().strip()
            date_elevi[nume_elev] = dict()

            for j in range(m):
                materie_elev = f.readline().strip().split(",")
                nume_materie = materie_elev[0]
                note_materie = [int(x) for x in materie_elev[1:]]
                date_elevi[nume_elev][nume_materie] = note_materie

    return date_elevi


def calc_medie(note):
    medie = sum(note) / len(note)
    if medie < 5 or len(note) == 1:
        medie = 0
    return medie


def despre_elev(date_elevi, nume_elev):
    medii = []
    for materie, note in date_elevi[nume_elev].items():
        medii.append((materie, calc_medie(note)))
    return medii


def adauga_nota(date_elevi, nume_elev, materie, *note):
    date_elevi[nume_elev][materie].extend(note)


def main():
    # Subpunctul a)
    date_elevi = citire()

    # Subpunctul b)
    nume_elev = input("Introduceti numele elevului: ")
    if nume_elev not in date_elevi:
        print(f"Elevul {nume_elev} nu exista in clasa")
    else:
        medii = despre_elev(date_elevi, nume_elev)
        medii = sorted(medii, key=lambda x: -x[1])
        for materie, medie in medii:
            print(f"{materie} {medie:1.2f}")

    # Subpunctul c)
    de_modificat = input("Introduceti numele elevului, materia si notele: ").strip().rsplit(maxsplit=3)
    nume_elev, materie = de_modificat[:2]
    note = [int(x) for x in de_modificat[2:]]

    adauga_nota(date_elevi, nume_elev, materie, *note)

    medie = calc_medie(date_elevi[nume_elev][materie])
    print(f"{materie} {medie:1.2f}")


if __name__ == "__main__":
    main()
```

