#include <algorithm>
#define MOD 9001
int main()
{
	int n, k; scanf("%d %d", &n, &k);
	int* d = (int*)malloc(n * sizeof(int)); d[0] = 1;
	int last(1);
	for (int i = 1; i < n; ++i)
	{
		d[i] = last % MOD;
		if (i - k >= 0)
			last -= d[i - k] % MOD;
		last += d[i];
	}
	printf("%d", d[n - 1] % MOD);
	return 0;
}