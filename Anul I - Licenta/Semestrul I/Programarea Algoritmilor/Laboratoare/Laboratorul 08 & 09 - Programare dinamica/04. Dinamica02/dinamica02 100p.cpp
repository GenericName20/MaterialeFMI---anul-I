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