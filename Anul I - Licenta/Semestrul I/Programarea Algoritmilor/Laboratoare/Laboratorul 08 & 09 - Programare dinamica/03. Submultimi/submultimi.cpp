// Stare: d[i] - Numarul de submultimi formate din elemente de la 1 la i
// Stare initiala: d[1] = 1 - Submultimea {1}
//				   d[2] = 2 - Submultimile {1}, {2}
// Relatie de recurenta: d[i] = d[i - 1] (Nu il adaugam la submultimile anterioare)
//                            + d[i - 2] (Il adaugam la orice submultime anterioara, dar nu vecina)
//                            + 1 (Il adaugam in submultimea formata doar din elementul valoarea i)
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