# Problema [SumTri](https://www.pbinfo.ro/probleme/385/sumtri)

## Stare: 
- d[i][j] - Suma maximă calculată de pe ultima linie până în vârful triunghiului, până în poziția <b>i, j</b>

## Stări inițiale
- d[n][i] preia valoarea corespondentă din triunghi, pentru orice <b>1 <= i <= n</b>

## Relație de recurență
`d[i][j] = triangle[i][j] + max(d[i + 1][j], d[i + 1][j + 1])`
- De pe penultima spre prima linie, de la stânga la dreapta, vom calcula suma curentă ca fiind maximul dintre <b><i>valoarea de pe linia anterioară și aceeași coloană (d[i + 1][j])</i></b> și <b><i>valoarea de pe linia anterioară și coloana vecină la dreapta (d[i + 1][j + 1])</i></b>. La acest maxim adăugăm valoarea corespondentă din triunghi

## Soluție - 100P - Python (Cu indexare de la 0)
```
inputFileName = "sumtri.in"
outputFileName = "sumtri.out"

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip()), [[int(value) for value in line.split()] for line in f.readlines()]

def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n, triangle = readInput()
    d = [[0 for _ in range(i + 1)] for i in range(n)]
    for i in range(n):
        d[n - 1][i] = triangle[n - 1][i]
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            d[i][j] = triangle[i][j] + max(d[i + 1][j], d[i + 1][j + 1])

    writeOutput(d[0][0])
    return
        
if __name__ == "__main__":
    main()
    exit()
```

## Soluție - 100P - C++ (Mai rapidă, cu indexare de la 0)
```
#include <fstream>
using namespace std;
int main()
{
	int n;
	FILE* f = fopen("cod.in", "r");
	fscanf(f, "%d", &n);
	int** t = (int**)malloc(n * sizeof(int*));
	int** d = (int**)malloc(n * sizeof(int*));
	for (int i = 0; i < n; ++i)
	{
		t[i] = (int*)malloc((i + 1) * sizeof(int));
		d[i] = (int*)malloc((i + 1) * sizeof(int));
		for (int j = 0; j <= i; ++j)
		{
			fscanf(f, "%d", &t[i][j]);
			d[i][j] = 0;
		}
	}
	fclose(f);

	for (int i = 0; i < n; ++i)
		d[n - 1][i] = t[n - 1][i];
	for (int i = n - 2; i >= 0; --i)
		for (int j = 0; j <= i; ++j)
			d[i][j] = t[i][j] + (d[i + 1][j] > d[i + 1][j + 1] ? d[i + 1][j] : d[i + 1][j + 1]);
	
	FILE* g = fopen("cod.out", "w");
	fprintf(g, "%d", d[0][0]);
	fclose(g);
	return 0;
}
```
