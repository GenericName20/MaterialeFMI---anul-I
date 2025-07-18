// Stări: 
// d[i] - Numarul de cuvinte de i litere, cu ultimele două litere distincte
// e[i] - Numărul de cuvinte de i litere, cu ultimele două litere egale
// 
// Stări inițiale:
// d[1] = 26
// d[2] = 26 * 26
// 
// Relații de recurență:
// e[i] = d[i - 1]
// d[i] = 25 * d[i - 1] + 25 * e[i - 1] = 25 * d[i - 1] + 25 * d[i - 2]
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