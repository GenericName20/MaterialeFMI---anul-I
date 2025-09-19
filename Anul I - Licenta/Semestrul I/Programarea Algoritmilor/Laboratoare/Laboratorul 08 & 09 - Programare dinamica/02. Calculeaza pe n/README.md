# Problema [Calculează pe n](https://www.pbinfo.ro/probleme/3672/calculeaza-pe-n)

## Stare
- d[i] - Numărul <b>minim</b> de operații necesare pentru a calcula numărul <b>i</b>

## Stare inițială
- d[1] = 0 - Numărul 1 este la baza celorlalte operații și <i><b>nu poate fi calculat</b></i>

## Relația de recurență
`d[i] = 1 + min(d[i - 1], d[i / 2], d[i / 3])`

## Soluție (bottom-up)
```
#include <algorithm>
using namespace std;
int main()
{
	int n; scanf("%d", &n);
	int* d = (int*)malloc((n + 1) * sizeof(int)); // d.resize(n + 1) cu vector<int> d;
	
	d[1] = 0;
	for (int i = 2; i <= n; ++i)
	{
		int minLastValue(d[i - 1]);
		if (i % 2 == 0) minLastValue = min(minLastValue, d[i / 2]);
		if (i % 3 == 0)	minLastValue = min(minLastValue, d[i / 3]);
		
		d[i] = 1 + minLastValue;
	}
	printf("%d", d[n]);
	return 0;
}
```