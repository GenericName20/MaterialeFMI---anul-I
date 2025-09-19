# Problema [Cladire](https://www.pbinfo.ro/probleme/392/cladire)

## Stare: 
- d[i][j] - Numărul de moduri în care se poate ajunge în camera de pe poziția <b>i, j</b>

## Stări inițiale
- d[1][i] = 1, pentru orice <b>1 <= i <= m</b> - Se poate ajunge în camerele de pe prima linie într-un singur mod (Deplasare la dreapta)
- d[i][1] = 1, pentru orice <b>1 <= i <= n</b> - Se poate ajunge în camerele de pe prima coloană într-un singur mod (Deplasare în jos)

## Relație de recurență
`d[i][j] = d[i][j - 1] + d[i - 1][j]` - În camera de pe poziția <b>i, j</b> se poate ajunge:
- printr-o deplasare din camera anterioară, aflată în stânga (d[i][j - 1]) - Coloana anterioară
- printr-o deplasare din camera anterioară, aflată sus (d[i - 1][j]) - Linia anterioară

## Soluție - 100P - C++ (Cu indexare de la 0)
```
#include <fstream>
#include <algorithm>
using namespace std;
ifstream f("cladire.in");
ofstream g("cladire.out");
#define MOD 9901
int main()
{
	int n, m; f >> n >> m;
    // vector<vector<int>> d(n, vector<int>(m));
	int** d = (int**)malloc(n * sizeof(int*));

	for (int i = 0; i < n; ++i)
	{
		d[i] = (int*)malloc(m * sizeof(int));
		d[i][0] = 1;
	}

	for (int i = 0; i < m; ++i)
		d[0][i] = 1;

	for (int i = 1; i < n; ++i)
		for (int j = 1; j < m; ++j)
			d[i][j] = (d[i][j - 1] + d[i - 1][j]) % MOD;
	
    g << d[n - 1][m - 1];
	return 0;
}
```
