// Stări: 
// d[i] - Numărul de numere formate din i cifre

// Stăre inițială:
// d[1] = 2 - Se termină cu {2} sau {4}
// d[2] = 2 * 3 = 6 - Se termină cu {2} sau {4}, la care se adaugă oricare {1}, {3}, ({2} sau {4})

// Relații de recurență:
// d[i] = 3 * d[i - 1] - Se poate adăuga orice număr diferit de cel setat anterior
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