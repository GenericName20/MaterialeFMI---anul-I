# Problema [Dinamica01](https://www.pbinfo.ro/probleme/2259/dinamica01)
<i>Considerăm cifre de la 1 la 9</i>

## Stare
- d[i][j] - Numărul submulțimilor cu n cifre, care se termină cu o cifră de paritate <b>j</b>

## Stări inițale
- d[1][0] = 4 - Se pot alege 4 cifre pare pentru început: 2, 4, 6, 8
- d[1][1] = 5 - Se pot alege 5 cifre impare pentru început: 1, 3, 5, 7, 9

## Relații de recurență
- `d[i][0] = 4 * d[i - 1][1]` - Adăgăm o nouă cifră pară din {2, 4, 6, 8} în fiecare dintre submulțimile construite până acum, care se termină cu o cifră impară
- `d[i][1] = 5 * d[i - 1][0]` - Adăgăm o nouă cifră impară din {1, 3, 5, 7, 9} în fiecare dintre submulțimile construite până acum, care se termină cu o cifră pară

## Soluție - 100P - Python (Cu indexare de la 0)
```
MOD = 30103
def main():
    n = int(input().strip())
    d = [[0 for _ in range(2)] for _ in range(n + 1)]
    d[0][0] = 1
    d[0][1] = 1

    for i in range(1, n + 1):
        d[i][0] = (4 * d[i - 1][1]) % MOD
        d[i][1] = (5 * d[i - 1][0]) % MOD

    answer = (d[i][0] + d[i][1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
    exit()
```

## Soluție - 100P - C++ (Cu indexare de la 0)
```
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
```
