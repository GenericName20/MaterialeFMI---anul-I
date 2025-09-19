#include <algorithm>
#define MOD 30103
int main()
{
	int n; scanf("%d", &n);
	int** d = (int**)malloc(n * sizeof(int*));
	for (int i = 0; i < n; ++i)
		d[i] = (int*)malloc(2 * sizeof(int));
	d[0][0] = 4; d[0][1] = 5;
	for (int i = 1; i < n; ++i)
	{
		d[i][0] = (4 * d[i - 1][1]) % MOD;
		d[i][1] = (5 * d[i - 1][0]) % MOD;
	}
	printf("%d", (d[n - 1][0] + d[n - 1][1]) % MOD);
	return 0;
}