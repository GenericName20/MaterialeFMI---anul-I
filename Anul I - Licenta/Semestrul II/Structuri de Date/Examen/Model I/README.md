# SD - Model de Examen (Iunie, 2024)

## Partea I

1. Într-un min-heap faceți operațiile I(9), I(4), I(10), I(2), delete min, I(17), I(3), I(19), I(26) delete min, delete min. Arată arborele după fiecare operație.

- I(9):
```
0: 9
```

- I(4):
```
Primul pas:
0: 9
9: 4

Al doilea pas:
0: 4
4: 9
```

- I(10)
```
0: 4
4: 9, 10
```

- I(2)
```
Primul pas:
0: 4
4: 9, 10
9: 2

Al doilea pas:
0: 4
4: 2, 10
2: 9

Al treilea pas:
0: 2
2: 4, 10
4: 9 
```

- D(min)
```
Primul pas:
0: 10
10: 4, 9

Al doilea pas (ReheapDown):
0: 4
4: 9, 10
```

- I(17)
```
0: 4
4: 9, 10
9: 17
```

- I(3)
```
Primul pas:
0: 4
4: 9, 10
9: 17, 3

Al doilea pas:
0: 4
4: 3, 10
3: 17, 9

Al treilea pas:
0: 3
3: 4, 10
4: 17, 9
```

- I(19)
```
0: 3
3: 4, 10
4: 17, 9
10: 19
```

- I(26)
```
0: 3
3: 4, 10
4: 17, 9
10: 19, 26
```

- D(min)
```
0: 4
4: 9, 19
9: 17, 10
19: 26
```

- D(min)
```
0: 9
9: 10, 19
10: 26, 17
```
---
2. Într-un arbore binar de căutare faceți operațiile I(8), I(3), I(1), I(6), I(10), I(14), I(4), del(6), del(1), I(7), I(9), del(8). Arătați arborele după fiecare 2 operații.

- I(8), I(3)
```
0: 8
8: 3
```

- I(1), I(6)
```
0: 8
8: 3
3: 1, 6
```

- I(10), I(14)
```
0: 8
8: 3, 10
3: 1, 6
10: 14
```

- I(4), del(6)
```
0: 8
8: 3, 10
3: 1, 4
10: 14
```

- del(1), I(7)
```
0: 8
8: 3, 10
3: 4
4: 7
10: 14
```

- I(9)
```
0: 8
8: 3, 10
3: 4
4: 7
10: 9, 14
```

- del(8)
```
0: 9
9: 3, 10
3: 4, 7
10: 14
```

---
3. Ce se întâmplă dacă două chei diferite au aceeași valoare hash într-un tabel hash? 
```
[ ] Valorile sunt stocate împreună în același slot.
[ ] Una dintre valori este ignorată. 
[x] Apare o coliziune și trebuie rezolvată printr-o metodă adecvată. 
[ ] Tabelul hash se redimensionează automat.
```

## Partea 2 - Nr. 1

1.	Care dintre următoarele secvențe de operații este invalidă într-o stivă care are inițial trei elemente?
```
[ ] PUSH, POP, POP, POP, POP, PUSH
[ ] PUSH, POP, POP, POP, PUSH, POP, POP
[x] PUSH, POP, POP, POP, POP, POP, PUSH, POP
[ ] POP, PUSH, POP, PUSH, TOP, TOP, TOP
[ ] PUSH, PUSH, PUSH, PUSH, PUSH, PUSH
[x] POP, POP, POP, POP, POP, POP, POP
```
---
2.	Care dintre următoarele afirmații sunt adevărate despre ștergerea unui nod dintr-un arbore binar de căutare (BST)?
```
[x] Ștergerea unui nod frunză nu necesită nicio rearanjare a arborelui.
[x] Ștergerea unui nod cu un singur copil implică înlocuirea nodului cu copilul său.
[x] Ștergerea unui nod cu doi copii implică găsirea succesorului sau a predecesorului sau și înlocuirea -odului cu acesta.
[x] După ștergerea unui nod, arborele rezultat poate să nu mai fie echilibrat.
[ ] Ștergerea rădăcinii unui BST este imposibilă.
```
---
3.	Care din următoarele structuri de date permit operații de Insert, Search, si Delete in O(log n)?
```
[x] AVL             | O(log n)      | O(log n)      | O(log n)
[x] Red Black Tree  | O(log n)      | O(log n)      | O(log n)
[ ] Fibonacci Heap  | O(1)          | O(log n)      | No
[ ] Binary Heap     | O(log n)      | O(log n)      | No
[ ] Hash            | O(n)          | O(n)          | O(n)
[ ] Deque           | O(n)          | O(n)          | O(n)
```
---
4. Un arbore ternar cu 19 noduri poate avea înălțimea ? (Considerăm că un arbore cu 1 nod are înălțimea 0).
```
[ ] 1
[ ] 2
[x] 3   | 3 > log3(19)
[x] 4
[x] 5
[x] 6
[x] 7
[x] 8
```
---
5. Dacă vrem să sortăm 10^7 numere naturale mai mici decât 10^6 ce algoritm de sortare ar fi bine să folosim?
```
[ ] Radix Sort (baza 2^6)
[ ] Quick Sort
[ ] Merge Sort
[x] Counting Sort
[ ] Tim Sort
[ ] Radix Sort (baza 2^16)
```
---
6. Să presupunem că avem numerele între 1 și 1000 inserate într-un arbore binar de cautare și că dorim să căutăm valoarea 363. Care dintre următoarele secvente NU ar putea fi secvență de noduri examinate?
```
[ ] 2, 252, 401, 398, 330, 344, 397, 363
[ ] 924, 220, 911, 244, 898, 258, 362, 363
[x] 925, 202, 911, 240, 912, 245, 363
[ ] 2, 399, 387, 219, 266, 382, 381, 278, 363
[x] 935, 278, 347, 621, 299, 392, 358, 363
```
---
7.	In ce complexitate putem construi cat mai eficient un heap dintr-un vector de n elemente ?
```
[x]	O(n)
[ ]	O(1)
[ ]	O(nlogn)
[ ]	O(log(n))
[ ]	O(sqrt(n))
```
---
8. Care dintre următoarele afirmații sunt adevărate despre un heap binar?
```
[x]	Inserarea si stergerea se fac in aceeasi complexitate.
[ ]	Poate avea mai mult de un nivel incomplet
[ ]	Poate avea mai multe radacini la un moment dat.
[x]	Poate fi folosit pentru sortarea unui vector in complexitate O(nlogn)
[ ]	Suportă aceleași operații pe care le suportă un arbore binar echilibrat în aceeași complexitate.
```
---
9. Fie H un max-heap care conține 80 de valori distincte. În câte poziții diferite se poate afla elementul minim?
```
[ ]	32
[ ]	40
[x]	41 = [n / 2] + 1
[ ]	42
[ ]	64
```
---
10.	Care este limita inferioară a complexității în timp (în cel mai rău caz) pentru orice algoritm de sortare care folosește doar comparații între elemente, pentru a sorta un șir de n elemente?
```
[ ]	(a) Ω(n^2)
[ ]	(b) Ω(n)
[x]	(c) Ω(n log n)
[ ]	(d) Ω(log n)
[ ]	(e) Ω(1)
[ ]	(f) Ω(√n)
```
---
11.	Diferența de înălțime dintre două frunze într-un max-heap poate fi?
```
[ ]	2
[x]	1
[ ]	3
[x]	0
[ ]	4
[ ]	5
```
---
12. Care dintre următoarele afirmații sunt adevărate despre stive și cozi?

```
[x] Ambele sunt structuri de date liniare.
[ ] Ambele respectă principiul LIFO (Last In, First Out).
[ ] Ambele respectă principiul FIFO (First In, First Out).
[x] Stiva suportă operațiile PUSH și POP, iar coada suportă operațiile ENQUEUE și DEQUEUE.
[x] Stiva poate fi folosită pentru a evalua expresii postfixate.
[ ] Stiva poate fi folosită pentru a implementa o coadă de așteptare
```

## Partea 2 - Nr. 2

1. Care dintre următoarele secvențe de operații este invalidă într-o stivă care are inițial două elemente?
```
[ ] PUSH, POP, POP, PUSH, POP, PUSH 
[ ] POP, POP, PUSH, PUSH, POP, POP 
[x] POP, POP, POP, POP, POP, PUSH, POP 
[ ] PUSH, PUSH, POP, POP, TOP, TOP 
[ ] PUSH, PUSH, PUSH, PUSH, PUSH, PUSH 
[x] POP, POP, POP, POP, POP
```
---
2. Care este complexitatea în timp în cel mai rău caz pentru ștergerea unui nod dintr-un arbore binar de căutare (BST)?
```
[ ] O(1)
[ ] O(log n)
[x] O(n)
[ ] O(n log n)
[ ] O(sqrt n) (facem cu Batog)
```
---
3. Care din următoarele structuri de date permit operații de Insert, Search, și Delete în O(log n)?
```
[x] AVL
[ ] Binomial Heap
[x] B-Arbori
[ ] Binary Heap
[ ] Hash
[ ] Coada
```
---
4. Un arbore ternar în care fiecare nod intern (non-frunză) are exact trei copii, are 15 de frunze. Care este numărul total de noduri din arbore?
```
[ ] 11 
[ ] 22 
[ ] 15 
[ ] 18 
[ ] 21 
[x] 22 
[ ] 25 
[ ] 42
```
---
5. Doriți să sortați 5 x 10^8 numere întregi mai mici decât 2^32. Care algoritm de sortare ar fi cel mai potrivit să utilizați?
```
[ ] Radix Sort (baza 2)
[x] Radix Sort (baza 2^16) 
[ ] Heap Sort
[ ] Quick Sort 
[ ] Merge Sort 
[ ] Counting Sort
```
---
6. Să presupunem că avem numerele de la 1 la 500 inserate într-un arbore binar de căutare și că dorim să căutăm valoarea 218. Care dintre următoarele secvențe NU ar putea fi secvența de noduri examinate?
```
[ ] 250, 125, 200, 225, 210, 215, 218 
[ ] 300, 150, 250, 200, 210, 220, 218 
[ ] 100, 200, 250, 225, 210, 218 
[ ] 250, 125, 150, 175, 190, 200, 218 
[x] 250, 375, 300, 275, 255, 230, 218
```
---
7.	Dat fiind un arbore binar de căutare cu n noduri, care este complexitatea în timp optimă pentru a obține un vector sortat în ordine crescătoare conținând toate elementele din arbore?
```
[ ]	O(1)
[x]	O(n)
[ ]	O(nlogn)
[ ]	O(log(n))
[ ]	O(sqrt(n))
```
---
8. Care dintre următoarele afirmații sunt adevărate despre un arbore binar de căutare (BST)?
```
[x] Într-un BST, fiecare nod are cel mult doi copii. 
[x] Un BST poate avea mai multe niveluri incomplete. 
[ ] Un BST poate avea mai multe rădăcini la un moment dat.
[ ] Un BST poate fi folosit pentru sortarea unui vector în complexitate O(n). 
[x] Într-un BST, subarborele stâng al oricărui nod conține doar valori mai mici decât nodul respectiv, iar subarborele drept conține doar valori mai mari.
```
---
9. Fie H un max-heap care conține 128 de valori distincte. În câte poziții diferite se poate afla al doilea cel mai mic element?
```
[ ] 32
[ ] 63
[ ] 64
[x] 65
[ ] 127
```
---
10. Se dă un algoritm de sortare care folosește doar comparații între elemente. În cel mai bun caz, acest algoritm sortează un șir de n elemente în timp liniar O(n). Care dintre următoarele afirmații este adevărată despre complexitatea în timp în cel mai rău caz a acestui algoritm?
```
[ ] Complexitatea în cel mai rău caz trebuie să fie, de asemenea, O(n). 
[ ] Complexitatea în cel mai rău caz sigur este O(n log n). 
[ ] Complexitatea în cel mai rău caz sigur este fi O(n^2). 
[ ] Complexitatea în cel mai rău caz poate fi O(1). 
[x] Nu putem determina complexitatea în cel mai rău caz pe baza informației date.
```
---
11. Care este diferența maximă posibilă de înălțime dintre două noduri frunză într-un arbore binar complet?
```
[x] 0
[x] 1
[ ] 2
[ ] log₂ n (unde n este numărul de noduri)
[ ] n - 1 (unde n este numărul de noduri)
```
---

12. Care dintre următoarele afirmații sunt adevărate despre deque (double-ended queue)?
```
[x] Este o structură de date liniară.
[ ] Respectă principiul LIFO (Last In, First Out).
[ ] Respectă principiul FIFO (First In, First Out).
[x] Poate fi implementat folosind un tablou dinamic.
[x] Poate fi folosit pentru a implementa atât o stivă, cât și o coadă.
[x] Operațiile de inserare și ștergere la ambele capete au complexitate O(1) în cel mai rău caz.
```

## Partea 3

1. Inserați următoarele chei și priorități într-un treap: (A, 34), (F, 42), (B, 59), C(87), (J, 77), (L, 10). Arătați arborele după fiecare inserare.

- I(A, 34)
```
Un singur nod: (A, 34)
```

- I(F, 42)
```
(F, 42) → (A, 34)
```

- I(B, 59)
```
(B, 59) → (A, 34)  
(B, 59) → (F, 42)
```

- I(C, 87)
```
(C, 87) → (B, 59)  
(B, 59) → (A, 34)  
(B, 59) → (F, 42)
```

- I(J, 77)
```
(C, 87) → (B, 59)  
(C, 87) → (J, 77)  
(B, 59) → (A, 34)  
(B, 59) → (F, 42)
```

- I(L, 10)
```
(C, 87) → (B, 59)  
(C, 87) → (J, 77)  
(B, 59) → (A, 34)  
(B, 59) → (F, 42)  
(J, 77) → (L, 10)
```

---

2. Construiți sparse table-ul (matricea din algoritmul RMQ) pentru șirul: 4 1 8 2 5 9 13 10. Presupunem că în cadrul unui query am vrea să determinăm minimul pe un interval.

| i | A[i] | ST[i][0] | ST[i][1] | ST[i][2] | ST[i][3] |
|---|------|----------|----------|----------|----------|
| 0 |  4   |    4     |    1     |    1     |    1     |
| 1 |  1   |    1     |    1     |    1     |          |
| 2 |  8   |    8     |    2     |    2     |          |
| 3 |  2   |    2     |    2     |    2     |          |
| 4 |  5   |    5     |    5     |    5     |          |
| 5 |  9   |    9     |    9     |          |          |
| 6 | 13   |   13     |   10     |          |          |
| 7 | 10   |   10     |          |          |          |

---

3. Inserați într-o trie cuvintele: their, there, this, that, does, did. Explicați cum puteți sorta aceste cuvinte în ordine lexicografică folosind trie-ul construit.

```
t
├── h
│   ├── a └── t
│   └── e └── r └── e
│   └── i └── s
├── d
│   ├── o └── e └── s
│   └── i └── d
```

### Liste de muchii:
```
t -> h
t -> d
h -> a
h -> e
h -> i
e -> r
r -> e
i -> s
a -> t
d -> o
d -> i
o -> e
e -> s
i -> d
```

Pentru sortare, DFS.

---
4. Construiți un min_heap cu 11 noduri în care pe ultimul nivel se află printre altele valorile 11, 5 și 7.

```
0: 1
1: 3, 2
3: 4, 6
2: 8, 9
4: 11, 5
6: 7, 10
```

---

5. Inserați în skip list următoarele valori: 13, 17, 1, 6, 8, 21, 23, 4, 9. La aruncarea banului obțineți următoarele valori: B, S, S, S, B, B, S, S, B, S, B, S, S, B, S, S, S, B, S, B, S, B. Când obțineți B vă opriți și inserați până la acel nivel. Când obțineți S continuați la nivelul următor.

```
Nivel 2:   1 —— 17 —— 23
Nivel 1:   1 —— 4 —— 17 —— 21 —— 23
Nivel 0:   1 —— 4 —— 6 —— 8 —— 9 —— 13 —— 17 —— 21 —— 23
```

Liste de muchii:
```
Nivel 0: 1 -> 4 -> 6 -> 8 -> 9 -> 13 -> 17 -> 21 -> 23
Nivel 1: 1 -> 4 -> 17 -> 21 -> 23
Nivel 2: 1 -> 17 -> 23
```

## Partea 4

1. Care este numărul maxim de elemente dintr-un heap binar de înălțime k? Vom presupune că rădăcina heap-ului se află la înălțime 0.
```
R: 2^(k + 1) - 1
```
---
2. Fie T un arbore binar de căutare și x un nod din T cu 2 fii. Care este numărul maxim de fii pe care îi poate avea predecesorul lui x?
```
R: 1
```
---
3. Care este complexitatea în timp, în cel mai rău caz, pentru a uni (merge) două heap-uri binare de dimensiuni m și n, într-un nou heap binar?
```
R: O(m + n)
```
---
4. Se poate găsi elementul minim dintr-un max-heap în O(log(n))? Justificați.
```
R: Nu. Justificare: Trebuie verificat tot heap-ul, ceea ce înseamnă O(n).
```
---
5. O parcurgere în inordine a unui max-heap produce mereu un șir crescător? Justificați.
```
R: Nu. Justificare: Nu există relație de subordine între arborii și subarborii stângi / drepți.
```

## Partea 5

1. Fie P o permutare cu n elemente. Scopul este să determinăm această permutare știind pentru fiecare poziție i (1 ≤ i ≤ n) câte elemente aflate înaintea ei sunt mai mici decât P[i]. Dacă există mai multe permutări posibile, se va afla cea minim lexicografic.


- Input:
```
N = 4
0 1 1 0
```

- Output:
```
2 4 3 1
```

- Soluție:
```
Introduc într-un set ordonat elementele de la 1 la N și îl parcurg de la dreapta la stânga, cu i de la n - 1 la 0.
Pentru fiecare index i, extrag din set al inv[i]-lea element din set și îl adaug în P[i].
```

---
2. Se consideră un șir S de paranteze rotunde (închise sau deschise) de lungime n și q interogări (i, j). Pentru fiecare interogare, să se răspundă dacă subsecvența de la i la j (S[i…j]) este corect parantezată.

- Soluție
```
Folosesc un vector balance[], unde:
- balance[i] = nr. paranteze deschise - nr. paranteze închise până la i;
- balance[j] - balance[i - 1] == 0 înseamnă că avem același număr de ( și ) pentru un query de forma <i, j>;
- balance[k] >= balance[i - 1], oricare ar fi k în [i, j].
```

---

3. Se dă un vector A cu N elemente. 1 ≤ A[i] ≤ N. Pentru fiecare i să se găsească j minim astfel încât A[j] < A[i].

- Soluție
```
Folosim o stivă monoton descrescătoare. Dacă A[i] < A[st.top()], atunci i este soluția pentru st.top(). Ca răspuns, reținem indicii.
```

---

4. Se dă un vector A cu N elemente. 1 ≤ A[i] ≤ N. Să se numere tripletele (i, j, k) astfel încât 1 ≤ i < j < k ≤ N și A[i] < A[j] < A[k].

- Soluție
```
Pentru fiecare j trebuie să ținem cont de:
- Câte prefixe A[i] < A[j] există pentru i < j
- Câte prefixe A[k] > A[j] există pentru k > j

Folosesc două Fenwich Trees (BIT):
- Unul de la stânga la dreapta
- Unul de la dreapta la stânga
```