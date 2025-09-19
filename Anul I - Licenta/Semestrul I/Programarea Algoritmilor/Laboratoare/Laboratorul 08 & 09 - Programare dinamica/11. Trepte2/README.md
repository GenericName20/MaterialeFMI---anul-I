# Problema [Dinamica01](https://www.pbinfo.ro/probleme/2259/dinamica01)

## Stare
- d[i] - Numărul de moduri în care se poate ajunge pe scara <b>i</b>

## Stare inițială
- d[1] = 1 - Se poate ajunge într-un singur mod pe scara <b>1</b>

## Relații de recurență
- `d[i] = d[i - 1] + d[i - 2] + ... + d[i - k]`, dacă <b>i > k</b>
- `d[i] = d[i - 1] + d[i - 2] + ... + d[1]`, dacă <b>i <= k</b>

## Soluție - 80P - Python (Putem optimiza soluția pentru a obține O(n))
```
MOD = 9001
def main():
    n, k = map(int, input().strip().split())
    d = [0] + [1] + [0] * (n - 1)

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            d[i] += d[i - j] % MOD
        d[i] %= MOD

    print(d[n] % MOD)
    return

if __name__ == "__main__":
    main()
    exit()
```

## Soluție - 100P - Python
```
MOD = 9001
def main():
    n, k = map(int, input().strip().split())
    d = [0] + [1] + [0] * (n - 1)
    last = 1

    for i in range(2, n + 1):
        d[i] = last % MOD
        if (i - k >= 0):
            last -= d[i - k] % MOD
        last += d[i]
        
    print(d[n] % MOD)
    return

if __name__ == "__main__":
    main()
    exit()
```

## Soluție - 100P - C++ (Mai rapidă, cu indexare de la 0)
```
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
```