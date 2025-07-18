# Problema [Dinamica06](https://www.pbinfo.ro/probleme/3990/dinamica06)

## Stare: 
- d[i] - Numărul de numere formate din i cifre

## Stări inițiale
- d[1] = 2 - Se termină cu {2} sau {4}
- d[2] = 2 * 3 = 6 - Se termină cu {2} sau {4}, la care se adaugă oricare dintre {1}, {3}, ({2} sau {4})

## Relație de recurență
`d[i] = 3 * d[i - 1]` - Se poate adăuga orice cifră diferită de cea setată anterior

## Soluție - 80P (Din cauza dimensiunii insuficiente a vectorului)
```
#include <algorithm>
#define MOD 123457
int main()
{
	int n; scanf("%d", &n); int* d = (int*)malloc((n + 1) * sizeof(int));
	d[1] = 2; d[2] = 6;
	for (int i = 3; i <= n; ++i)
		d[i] = (3 * d[i - 1]) % MOD;
	printf("%d", d[n]);
	return 0;
}
```

## Soluție - 100P
<i>Soluția presupune o optimizare a exponențierii 3<sup>n-1</sup></i>

Se poate observa că starea de recurență `d[i] = 3 * d[i - 1]` începe cu d[1] = 2, deci d[i] = 3<sup>i-1</sup>, iar d[n] = 3<sup>n-1</sup> * d[1]

```
#include <algorithm>
#define MOD 123457
int main()
{
	int n;
	long long res(1), e(3);
	scanf("%d", &n); n--;
	while (n > 0)
	{
		if (n % 2 == 1) 			// Dacă exponentul este impar
			res = (res * e) % MOD; // Înmulțim rezultatul actual cu e
		e = (e * e) % MOD; // Ridicăm e la pătrat
		n >>= 1;
	}
	printf("%lld", (2 * res) % MOD);
	return 0;
}
```