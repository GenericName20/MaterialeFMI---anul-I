# Model 1
## Problema 1 [4 pct]

### Enunt
Fișierul text `numere.in` conține, pe fiecare linie, câte un șir de numere întregi despărțite prin spații. Să se scrie în fișierul text `numere.out` șirurile din fișierul de intrare grupate în funcție de suma elementelor lor, conform modelului din exemplul de mai jos. Grupele de șiruri vor fi scrise în ordinea crescătoare a sumelor elementelor lor, iar în fiecare grupă șirurile se vor scrie în ordinea descrescătoare a numărului de elemente.

### Exemplu

| `numere.in`                                                    | `numere.out`                                                                                         |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 10 -5 5 10<br>100 -20 -30<br>11 9<br>5 5 10 20 10<br>-100 -100 | Suma -200:<br>-100 -100<br>Suma 20:<br>10 -5 5 10<br>11 9<br>Suma 50:<br>5 5 10 20 10<br>100 -20 -30 |

### Rezolvare

```py
def read_file(input_file):
    arrays = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            arrays.append([int(x) for x in line.split()])
    return arrays


def main():
    arrays = read_file("numere.in")
    dict = {}
    for array in arrays:
        try:
            dict[sum(array)].append(array)
        except:
            dict[sum(array)] = [array, ]
    with open("numere.out", "w") as f:
        for key in sorted(dict.keys()):
            f.write(f"Suma {key}:\n")
            for array in sorted(dict[key], key=lambda x: -len(x)):
                text = " ".join([str(x) for x in array])
                f.write(text + "\n")


if __name__ == "__main__":
    main()
```


## Problema 2 [3 pct]

### Enunt
Se dă fișierul `matrice.in` cu următoarea structură: pe linia $$i$$ se află separate prin câte un spațiu $$n$$ numere naturale reprezentând elementele de pe linia $$i$$ a unei matrice, ca în exemplul de mai jos. Este cunoscut faptul că în fișier se află $$n \times n$$ elemente numere naturale, unde $$n$$ este un număr natural **impar** $$> 2$$.

### Cerinte
a) [0,25 pct] Să se scrie o funcție `citire_matrice` care citește datele din fișierul `matrice.in` și returnează o matrice de dimensiune $$n \times n$$ formată din aceste numere.

b) [1,5 pct] Să se scrie o funcție care primește ca parametru matricea și returnează matricea bordată după următoarele reguli:

- se va adăuga o coloană nouă la final (pe poziția 𝑛) care va avea pe poziția 𝑘 **suma** valorilor de pe **linia** 𝑘

- se va adăuga o linie nouă la final (poziția 𝑛) care va avea pe poziția 𝑘 **suma** valorilor de pe **coloana** 𝑘

c) [1,25 pct] Se consideră matricea citită la punctul a), peste care se aplică funcția de la punctul b). Să se parcurgă matricea mai întâi pe diagonala principală, apoi pe diagonala secundară și, în final, restul elementelor care nu aparțin diagonalelor (parcurgerea se face pe linii de sus în jos și de la stânga la dreapta) și se afișează elementele în fișierul `matrice.out`.

### Exemplu

| `matrice.in`            | `dupa bordare`                                                             | `matrice.out`                         |
| ----------------------- | -------------------------------------------------------------------------- | ------------------------------------- |
| 7 8 9<br>6 1 2<br>5 4 3 | 7   8    9  24<br>   6   1    2   9<br>   5   4    3  12<br>18  13  14  45 | 7 1 3 45 24 2 4 18 8 9 6 9 5 12 13 14 |

### Rezolvare

```py
def read_file(input_file):
    matrix = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            matrix.append([int(x) for x in line.split()])
    return matrix


def update(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i].append(sum(matrix[i]))
    sum_list = [0] * (n + 1)
    for i in range(n):
        for j in range(n + 1):
            sum_list\[j] += matrix[i\][j]
    matrix.append(sum_list)
    return matrix


def parcurgere(matrix):
    v = []
    n = len(matrix) - 1
    for i in range(n + 1):
        v.append(matrix\[i\][i])
    for i in range(n + 1):
        v.append(matrix\[i\][n - i])
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j and i + j != n:
                v.append(matrix\[i\][j])
    return v


def write_file(output_file, v):
    with open(output_file, "w") as f:
        f.write(" ".join([str(x) for x in v]))


def main():
    write_file("matrice.out", parcurgere(update(read_file("matrice.in"))))


if __name__ == "__main__":
    main()
```

## Problema 3 [4 pct]

Se consideră fișierul text `catalog.in` cu următoarea structură:

- pe prima linie apare numărul $$n$$ reprezentând numărul de elevi dintr-o clasă a unui liceu
- pe următoarele linii avem informații despre cei $$n$$ elevi, respectiv pentru fiecare elev informațiile sunt structurate astfel:
    - linie de forma `<șir de caractere> <m>`, unde șirul de caractere este numele elevului (acesta este unic), iar $$m$$ este un număr natural reprezentând numărul de materii
    - urmată de $$m$$ linii care conțin notele elevului (numere naturale) la $$m$$ materii, fiecare având următoarea structură: 
        `<nume_materie>,<nota_1>,<nota_2>,...,<nota_k>`

### Observație:

- Orice elev are la fiecare materie cel puțin o notă, iar denumirile materiilor nu conțin caracterul ',' (virgulă).

### Exemplu de fisier de intrare

    5
    Ana Maria Pop 3
    Matematica,10,9,9,10,10
    Limba romana,8,9,9,8
    Fizica,10,9,7,10,10
    Mihai Popescu 3
    Matematica,9,7,10,10
    Limba romana,8,3,5,10
    Fizica,10,10
    Andrei Mincu 2
    Matematica,10,9,2
    Fizica,3,7,9
    Ioana Matei 3
    Fizica,10,10
    Matematica,10,10,10,9
    Limba romana,9,9,10,10
    Alin Enache 3
    Limba romana,10,10,10
    Matematica,10,10,10,10
    Fizica,10

### Cerinte
a) [2 pct] Scrieți o funcție care citește datele din fișierul `catalog.in` și returnează o structură de date cu informațiile din fișier. Folosiți o structură de date convenabilă pentru a rezolva
eficient subpunctele următoare.

b) [1 pct] Scrieți o funcție `detalii_elev` care primește ca parametri structura în care s-au memorat datele la cerința a) și un șir de caractere reprezentând numele unui elev și returnează mediile la toate materiile elevului cu numele primit ca parametru, memorate sub formă de listă de tupluri de tipul `(nume_materie, medie)`. Dacă un elev are o singură notă la o materie sau media este mai mică strict decât 5, acesta va avea media egală cu 0 și va rămâne corigent. Să se citească de la tastatură numele unui elev și să se afișeze pe ecran mediile acestuia (rotunjite cu două zecimale) la fiecare materie (sortate lexicografic) folosind această funcție.

| `Intrare trastatura` | `Afisare pe ecran`                                  |
| -------------------- | --------------------------------------------------- |
| Ana Maria Pop        | Fizica 9.20<br>Limba romana 8.50<br>Matematica 9.60 |

c) [1 pct] Scrieți o funcție clasament care primește structura de date în care s-au memorat datele la cerința a) și un număr variabil de parametri de tip șir de caractere reprezentând nume de elevi. Funcția returnează o listă de tupluri de tipul (nume_elev, medie_generala) cu mediile generale ale elevilor ale căror nume au fost primite ca parametru ordonată descrescător după medii. Media generală a unui elev este egală cu media aritmetică a mediilor de la fiecare materie, dacă acesta nu este corigent, altfel media este 0.

### Exemplu:
Dacă se apelează funcția pentru elevii Alin Enache și Ioana Matei se va returna lista
[(Ioana Matei,9.75), (Alin Enache,0)], deoarece Alin Enache are o singură notă la
fizică, deci este corigent.

### Rezolvare

```py
def read_file(input_file):
    dict = {}
    with open(input_file, "r") as f:
        n = int(f.readline())
        for i in range(n):
            info_elev = f.readline().split()
            nume_elev = " ".join(info_elev[:-1])
            m = int(info_elev[-1])
            dict[nume_elev] = {}
            for j in range(m):
                info_materie = f.readline().split(",")
                nume_materie = info_materie[0]
                dict\[nume_elev\][nume_materie] = [int(x) for x in info_materie[1:]]
    return dict


def detalii_elev(dict, nume_elev):
    medii = []
    for materie in dict[nume_elev]:
        note = dict\[nume_elev\][materie]
        if len(note) == 1 or sum(note) / len(note) < 5:
            medii.append((materie, 0))
        else:
            medii.append((materie, round(sum(note) / len(note), 2)))
    medii.sort()
    return medii


def clasament(dict, *argv):
    clasament_medii = []
    for nume_elev in argv:
        medii = detalii_elev(dict, nume_elev)
        suma = 0
        ok = 1
        for materie, nota in medii:
            suma += nota
            if nota == 0:
                ok = 0
        if ok == 0:
            clasament_medii.append((nume_elev, 0))
        else:
            clasament_medii.append((nume_elev, round(suma / len(medii), 2)))
    return sorted(clasament_medii, key=lambda x: -x[1])


def main():
    dict = read_file("catalog.in")
    medii = detalii_elev(dict, input())
    for materie, medie in medii:
        print(materie, medie)
    clasament_medii = clasament(dict, "Ioana Matei", "Alin Enache")
    print(clasament_medii)


if __name__ == "__main__":
    main()
```