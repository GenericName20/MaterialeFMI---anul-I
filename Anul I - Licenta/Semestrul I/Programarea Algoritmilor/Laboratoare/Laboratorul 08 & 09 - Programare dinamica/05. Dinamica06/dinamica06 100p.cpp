#include <algorithm>
#define MOD 123457
int main()
{
	int n;
	long long res(1), e(3);
	scanf("%d", &n); n--;
	while (n > 0)
	{
		if (n % 2 == 1)
			res = (res * e) % MOD;
		e = (e * e) % MOD;
		n >>= 1;
	}
	printf("%lld", (2 * res) % MOD);
	return 0;
}