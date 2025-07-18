# Problema [NumarDeSubmultimi](https://www.pbinfo.ro/probleme/3213/numardesubmultimi)

## Stare
- d[i] - Numărul total de submulțimi formate din elemente de la <b>1</b> la <b>i</b>

## Stare inițială 
- d[1] = 1 - Submulțimea <b>{1}</b>
- d[2] = 2 - Submulțimile <b>{1}</b>, <b>{2}</b>

## Relația de recurență
`d[i] = d[i - 1] + d[i - 2] + 1`

- d[i - 1] - <i>Nu îl adăugam pe i submultimile anterioare</i>
- d[i - 2] - <i>Îl adăugăm la orice submulțime anterioară, dar nu în cea învecinată</i>
- 1 - <i>Îl adăugăm în submulțimea formată doar din elementul i</i>

## Soluție
```
#include <algorithm>
#define MOD 777013
int main()
{
	int n; scanf("%d", &n); int* d = (int*)malloc(n * sizeof(int));
	d[1] = 1; d[2] = 2;
	
	for (int i = 3; i <= n; ++i)
		d[i] = (d[i - 1] + d[i - 2] + 1) % MOD;
	
	printf("%d", d[n]);
	return 0;
}
```
