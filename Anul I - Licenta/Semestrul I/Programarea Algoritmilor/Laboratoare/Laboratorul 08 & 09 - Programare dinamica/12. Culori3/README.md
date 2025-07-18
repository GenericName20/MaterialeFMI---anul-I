# Problema [Culori3](https://www.infoarena.ro/problema/culori3)

## Stări:
- d[i][culoare] - Numărul de moduri în care poate fi vopsit un gard cu <b>i</b> scânduri, care are scândura <b>i</b> vopsită în culoarea respectivă
- sum(d[n]) - Numărul total de moduri în care poate fi vopsit un gard cu n scânduri

## Stări inițiale:
Există un singur mod de a vopsi prima scândură cu una dintre culorile puse la dispoziție:
- `d[1][albastru] = 1`
- `d[1][alb] = 1`
- `d[1][rosu] = 1`
- `d[1][verde] = 1`
- `d[1][galben] = 1`

## Relații de recurență:
- `d[i][albastru] = d[i - 1][alb] + d[i - 1][rosu]`
- `d[i][alb] = d[i - 1][albastru]`
- `d[i][rosu] = d[i - 1][albastru] + d[i - 1][verde]`
- `d[i][verde] = d[i - 1][rosu] + d[i - 1][galben]`
- `d[i][galben] = d[i - 1][verde]`

## Observații
<i>Pentru simplitate, vom codifica cele 5 culori astfel:</i>

- Albastru = 0, Alb = 1, Rosu = 2, Verde = 3, Galben = 4

## Soluție - Python (Cu indexare de la 0)
<i>Nu primește punctaj pe InfoArena, dar este un prototip bun pentru implementarea soluției în C++</i>

În schimb, primește 100 de puncte pe [PBInfo - Problema Culori2](https://www.pbinfo.ro/probleme/1031/culori2)

```
inputFileName = "culori3.in"
outputFileName = "culori3.out"

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip())
    
def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n = readInput()
    d = [[0 for _ in range(5)] for _ in range(n)]

    for i in range(5):
        d[0][i] = 1

    for i in range(1, n):
        d[i][0] = d[i - 1][1] + d[i - 1][2]
        d[i][1] = d[i - 1][0]
        d[i][2] = d[i - 1][0] + d[i - 1][3]
        d[i][3] = d[i - 1][2] + d[i - 1][4]
        d[i][4] = d[i - 1][3]
    
    writeOutput(sum(d[n - 1]))

if __name__ == "__main__":
    main()
    exit()
```

## Soluție - 100p - C++ (Cu indexare de la 0)
- Pentru implementarea soluției, ținem cont că trebuie să folosim operații pe numere mari. Avem definite următoarele:

`Funcția 'add(a, b)' pentru a face operația 'a = a + b'.`

`Funcția din <bits/stdc++.h> (sau <bits.h>, <algorithm.h>...) 'memcpy(a, b, sizeof(b))' pentru operația 'a = b'.`

- Redefinim stările:
  
`d[1][culoare] - Numărul de posibilități de a vopsi gardul, pentru fiecare culoare, după adăugarea unei scânduri noi.`

`d[0][culoare] - Numărul de posibilități de a vopsi gardul, pentru fiecare culoare, înainte de adăugarea unei scânduri noi.`

```
#include <bits/stdc++.h>
short d[2][5][3000];
void add(short a[], short b[])
{
    short t = 0;
    a[0] = a[0] < b[0] ? b[0] : a[0];

    for (int i = 1; i <= a[0]; ++i, t /= 10)
    {
        t = a[i] + b[i] + t;
        a[i] = t % 10;
    }

    if (t) a[++a[0]] = t;
}
int main()
{
    int n;
    FILE* f = fopen("culori3.in", "r");
    fscanf(f, "%d", &n);
    fclose(f);
    for (short i = 0; i < 5; ++i)
    {
        d[0][i][0] = 1;
        d[0][i][1] = 1;
    }

    for (int i = 2; i <= n; ++i)
    {
        memcpy(d[1][0], d[0][1], sizeof(d[0][1])); // + d[0][2]
        memcpy(d[1][1], d[0][0], sizeof(d[0][0]));
        memcpy(d[1][2], d[0][0], sizeof(d[0][0])); // + d[0][3]
        memcpy(d[1][3], d[0][2], sizeof(d[0][2])); // + d[0][4]
        memcpy(d[1][4], d[0][3], sizeof(d[0][3]));
        add(d[1][0], d[0][2]);
        add(d[1][2], d[0][3]);
        add(d[1][3], d[0][4]);
        for (int j = 0; j <= 4; ++j)
            memcpy(d[0][j], d[1][j], sizeof(d[1][j]));
    }
    for (int i = 1; i < 5; ++i)
        add(d[1][0], d[1][i]);

    FILE* g = fopen("culori3.out", "w");
    for (int i = d[1][0][0]; i > 0; --i)
        fprintf(g, "%d", d[1][0][i]);
    fclose(g);
    return 0;
}
```
