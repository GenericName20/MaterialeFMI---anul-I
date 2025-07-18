# Problema [Dinamica02](https://www.pbinfo.ro/probleme/2260/dinamica02)

## Stări
- d[i] - Numarul de cuvinte de i litere, <b>cu ultimele două litere distincte</b>
- e[i] - Numărul de cuvinte de i litere, <b>cu ultimele două litere egale</b>

## Stări inițiale
- d[1] = 26 - Se pot folosi toate literele
- d[2] = 26 * 26 - În continuare, se pot folosi toate litere

## Relații de recurență
- e[i] = d[i - 1]
- d[i] = 25 * d[i - 1] + 25 * e[i - 1] => `d[i] = 25 * d[i - 1] + 25 * d[i - 2]`

## Soluție - 80P (Din cauza dimensiunii insuficiente a vectorului)
```
#include <algorithm>
#define MOD 777013
int main()
{
	int n; scanf("%d", &n); int* d = (int*)malloc((n + 1) * sizeof(int));
	d[1] = 26; d[2] = 26 * 26;
	for (int i = 3; i <= n; ++i)
		d[i] = (25 * d[i - 1] + 25 * d[i - 2]) % MOD;

	printf("%d", d[n]);
	return 0;
}
```

## Soluție - 100P
<i>Soluția presupune o optimizare de spațiu cunoscută din problemele cu Șirul lui Fibonacci</i>
```
#include <algorithm>
#define MOD 777013
int main()
{
	int n; scanf("%d", &n);
	int d(26), e(26 * 26), r;
	for (int i = 3; i <= n; ++i)
	{
		r = (25 * d + 25 * e) % MOD;
		d = e;
		e = r;
	}
	printf("%d", r);
	return 0;
}
```
