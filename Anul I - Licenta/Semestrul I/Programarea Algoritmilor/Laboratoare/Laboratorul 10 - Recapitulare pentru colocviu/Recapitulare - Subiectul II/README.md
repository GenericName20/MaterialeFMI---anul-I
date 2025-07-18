# Model 2
## Problema 1 [4 pct]

**Enunt**
Fișierul text `text.in` conține pe prima linie un cuvânt $$w$$ nevid format din litere mici ale
alfabetului englez, iar pe următoarele linii un text în care cuvintele sunt despărțite prin spații
și semnele de punctuație uzuale. Să se scrie în fișierul text `text.out` toate cuvintele din fișierul `text.in` care au mulțimea literelor inclusă în mulțimea literelor cuvântului $$w$$ sau mesajul *“Imposibil”*dacă în fișierul de intrare nu există nici un cuvânt cu proprietatea cerută,
conform modelului din exemplul de mai jos. Cuvintele vor fi scrise grupat, în funcție de
mulțimile literelor. Grupele vor fi scrise în ordine lexicografică, iar în cadrul fiecărui grup
cuvintele vor fi scrise în ordinea descrescătoare a lungimilor lor. Fiecare cuvânt va fi scris o
singură dată și nu se va face distincție între litere mici și litere mari.

### Exemplu

| `text.in`                                                                                                                          | `text.out`                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| semnificare<br>Mama s-a gandit sa isi puna seara<br>pe masa de ceara<br>o sama de bucate si bauturi care sunt<br>si acre si dulci. | Literele ['a', 'c', 'e', 'r']:<br>ceara<br>care<br>acre<br>Literele ['a', 'e', 'r', 's']:<br>seara<br>Literele ['a', 'm']:<br>mama<br>Literele ['a', 'm', 's']:<br>masa<br>sama<br>Literele ['a', 's']:<br>s-a<br>sa<br>Literele ['i', 's']:<br>isi<br>si |

Cuvântul "semnificare" are mulțimea literelor egală cu {'a', 'c', 'e', 'f', 'i', 'm', 'n', 'r', 's'}, iar cuvintele scrise în fișierul `text.out` sunt singurele din fișierul `text.in` care au mulțimea literelor inclusă în mulțimea literelor sale.

### Rezolvare
```py
# citire
f = open('text.in', 'r')
cuvant = set(f.readline().strip())
text = f.read().lower()
f.close()

# separarea sirului in cuvinte unice
thisdict = {}
separatori = ",.;:!?"

for x in separatori:
    text = text.replace(x, " ")

multime = [x for x in text.split()]

# crearea unui dictionar 'grup' : [cuvinte]
for word in multime:
    new_word = word.replace('-', '')
    letters = {i for i in new_word}
    lista = sorted([letters])
    if letters & cuvant == letters:
        key = ",".join([f"'{x}'" for x in lista])
        if key in thisdict.keys():
            thisdict[key].append(word)
        else:
            thisdict[key] = [word]

# sortarea cuvintelor din fiecare grup dupa lungime
for key in thisdict.keys():
    thisdict[key] = sorted(thisdict[key], key=lambda x: len(x), reverse=True)

# sortarea grupelor alfabetic
word_groups = sorted(thisdict.items(), key=lambda item: item[0])

f = open('text.out', 'w')
if not bool(word_groups):
    f.write("Imposibil\n")
else:
    for grupa, cuvinte in word_groups:
        f.write(f'Literele [{grupa}]:\n')
        for cuvant in cuvinte:
            f.write(cuvant + '\n')

f.close()
```



## Problema 2 [3 pct]

### Enunt
a) [0.5 pct] Scrieți o funcție `citire_matrice` ****care primește un parametru reprezentând numele unui fișier care conține elementele unei matrice pătratice de $$n \times n$$ de numere întregi cu următoarea structură:

- pe prima linie a fișierului este $$n$$
- pe a doua linie sunt $$n \times n$$ numere separate prin câte un spațiu reprezentând elementele matricei transformate în vector prin concatenarea liniilor matricei de la prima la ultima; astfel primele n numere de pe linie sunt elementele primei linii din matrice, urmate de elementele celei de a doua linii etc.

Funcția citește elementele matricei din fișierul cu numele dat ca parametru și returnează matricea cu aceste elemente. Pentru fișierul `"matrice.in"` ****din exemplul de mai jos matricea este:

    1 2 3
    4 5 6
    7 8 9

b) [1.5 pct] Scrieți o funcție **duplicare** care primește ca parametri (în această ordine): o matrice (listă de liste) și un număr variabil de numere naturale reprezentând indici ai liniilor din matrice (indicele primei linii din matrice este 0) și **inserează după fiecare linie cu indicele dat ca parametru o copie a ei** (duplică linia). Funcția va modifica matricea primită ca parametru.

c) [1 pct] Se dă fișierul `matrice.in` ****cu structura descrisă la punctul a). Folosind apeluri utile ale funcțiilor de la a) și b) să se citească matricea din fișierul `matrice.in`, să se modifice această matrice duplicând prima și a doua linie (după prima linie se va insera o linie egală cu ea, la fel și după a doua) și adăugând apoi 1 la primul element de pe prima linie. Să se afișeze pe ecran matricea obținută.

### Exemplu

| `matrice.in`           | `consola (iesire pe ecran)`               |
| ---------------------- | ----------------------------------------- |
| 3<br>1 2 3 4 5 6 7 8 9 | 2 2 3<br>1 2 3<br>4 5 6<br>4 5 6<br>7 8 9 |

### Rezolvare
```py
def citire_matrice(fisier):
    A = []
    linii = [line.strip().split() for line in open(fisier)]
    if len(linii) > 0 and len(linii[-1]) == 0:
        linii.pop()
    n = int(linii\[0\][0])
    linie = linii[1]

    for i in range(n):
        lin = []
        for j in range(n):
            lin.append(linie[j])
        linie = linie[n:]
        A.append(lin)

    return A


def duplicare(M, *linii):
    C = []
    cnt = 0
    for i in range(len(M)):
        lin = []
        for j in range(len(M[i])):
            lin.append(M\[i\][j])
        C.append(lin)

    for ind in linii:
        linie = C[ind]
        M.insert(ind + 1 + cnt, linie)
        cnt = cnt + 1


A = citire_matrice("matrice.in")

duplicare(A, 0, 1)

A\[0\][0] = int(A\[0\][0]) + 1

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A\[i\][j], end=" ")
    print("\n", end="")
```


## Problema 3 [4 pct]

### Enunt
Alice și Bob comunică folosind următorul algoritm pentru a-și codifica mesajele:

- Alice și Bob cunosc amândoi o cheie secretă sub forma unui șir de caractere care este o

permutare a celor 26 de litere mici din alfabetul englez, astfel: literei 'a' îi corespunde prima
literă din cheia secretă, literei 'b' îi corespunde a doua literă din cheia secretă, ..., literei 'z' îi
corespunde ultima literă din cheia secretă, după cum se poate observa din următorul
exemplu:

    - Alfabetul englez = `a b c d e f g h i j k l m n o p q r s t u v w x y z`
    -     Cheia secretă = `o b c g s e f h i z j k l m n p q r d t u v a w x y`
- Codificarea unui mesaj presupune înlocuirea fiecărei litere din el cu litera corespunzătoare din cheia secretă. De exemplu, dacă Alice și Bob au cheia secretă `"obcgsefhizjklmnpqrdtuvawxy"`, atunci cuvântul `"astazi"` se va codifica prin cuvântul `"odtoyi"`, deoarece literei 'a' îi corespunde litera 'o', literei 's' îi corespunde litera 'd' ș.a.m.d.
- Decodificarea unui mesaj codificat presupune căutarea fiecărei litere din el în cheia secretă și înlocuirea ei cu litera corespunzătoare din alfabetul englez. De exemplu, dacă Alice și Bob au cheia secretă `"obcgsefhizjklmnpqrdtuvawxy"`, atunci cuvântul codificat `"endt"` se va decodifica în cuvântul `"fost"`, deoarece literei 'e' îi corespunde litera 'f', literei 'n' îi corespunde litera 'o' ș.a.m.d.

Mesajele sunt codificate și transmise cuvânt cu cuvânt. Toate literele din mesaje sunt litere mici din alfabetul englez și nu se folosesc semne de punctuație, cu excepția caracterului ‘-’, care nu se criptează.

Eve este un hacker care interceptează traficul și reușește să găsească algoritmul de decodificare, precum și cheia secretă. Eve are dificultăți în reconstrucția propozițiilor deoarece nu salvează cuvintele în ordinea în care sunt trimise. Să se reconstruiască propozițiile trimise de Alice și Bob.

### Cerinte
a) ****[1 pct] Fișierul text `comunicare.in` are următoarea structură:

- pe prima linie se găsește cheia secretă
- pe fiecare dintre următoarele linii se găsesc informațiile despre un cuvânt (transmis la cel puțin un minut distanță), despărțite printr-un spațiu astfel:
    - primul caracter este A dacă cuvântul este trimis de Alice sau B dacă este trimis de Bob
    - separat printr-un spațiu se va găsi cuvântul în formă codificată
    - ultima informație va fi ora la care este trimis mesajul în format de 5 caractere și 24 de ore (de exemplu, 12:34 sau 21:03)

Să se scrie o funcție `citire_date` care să returneze o structură cu datele din fișier.

b) ****[1,5 pct] Să se scrie o funcție `decodificare` care primește ca parametri un cuvânt codificat și cheia secretă utilizată. Funcția trebuie să decodifice eficient cuvântul codificat și apoi să-l
returneze.

c) [1,5 pct] Să se reconstituie propozițiile trimise de Bob și Alice astfel :

- se decodifică fiecare cuvânt folosind funcția definită la punctul b)
- se determină ordinea în care au fost trimise cuvintele
- se salvează în fișierul text `comunicare.out` propozițiile reconstituite conform exemplului.

### Exemplu

| `comunicare.in`                                                                                                                                                                                             | `după decriptarea datelor`                                                                                                                                                    | `comunicare.out`                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| obcgsefhizjklmnpqrdtuvawxy<br>B cnlprnlido 13:20<br>A ko 12:00<br>A vnl 10:00<br>B o 10:20<br>A dug 12:30<br>B rstrofsti-vo 14:20<br>A odtoyi 09:00<br>B cnlumicorso 09:20<br>A otoco 11:00<br>B endt 12:20 | B compromisa 13:20<br>A la 12:00<br>A vom 10:00<br>B a 10:20<br>A sud 12:30<br>B retrageti-va 14:20<br>A astazi 09:00<br>B comunicarea 09:20<br>A ataca 11:00<br>B fost 12:20 | A : astazi vom ataca la sud<br>B : comunicarea a fost<br>compromisa retrageti-va |

### Rezolvare

```py
def citire_date(f):
    result_a = []
    result_b = []

    i = 0

    for line in f:
        if i == 0:
            key = line.strip()

        split_line = line.split()

        if split_line[0] == "A":
            result_a.append((split_line[1], split_line[2]))
        elif split_line[0] == "B":
            result_b.append((split_line[1], split_line[2]))

        i += 1

    return [key, result_a, result_b]


def decodificare(key, word):
    new_word = ""

    for letter in word:
        if not letter == '-':
            new_word += chr(ord('a') + key.find(letter))
        else:
            new_word += letter

    return new_word


fin = open("comunicare.in", "r")
fout = open("comunicare.out", "w")

structure = citire_date(fin)

for i in range(len(structure[1])):
    decoded = decodificare(structure\[0], structure[1\][i][0])
    hour_split = structure\[1\][i][1].split(":")
    time = int(hour_split[0]) * 60 + int(hour_split[1])
    structure\[1\][i] = (decoded, time)

for i in range(len(structure[2])):
    decoded = decodificare(structure\[0], structure[2\][i][0])
    hour_split = structure\[2\][i][1].split(":")
    time = int(hour_split[0]) * 60 + int(hour_split[1])
    structure\[2\][i] = (decoded, time)

a = structure[1]
a.sort(key=lambda word: word[1])
b = structure[2]
b.sort(key=lambda word: word[1])

output = "A : "

for word in a:
    output += word[0]
    output += " "

output += "\nB : "

for word in b:
    output += word[0]
    output += " "

fout.write(output)

fout.close()
```