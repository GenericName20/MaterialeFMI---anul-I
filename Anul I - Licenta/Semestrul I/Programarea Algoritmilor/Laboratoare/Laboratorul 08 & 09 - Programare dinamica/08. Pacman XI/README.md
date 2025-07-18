# Problema [Pacman XI](https://www.pbinfo.ro/probleme/3265/pacman-xi)

## Stare: 
- d[i][j] - Numărul de moduri în care se poate ajunge în pe poziția <b>i, j</b>

## Stări inițiale
- d[1][i] = 1, pentru orice <b>1 <= i <= m</b> - Se poate ajunge în căsuțele de pe prima linie într-un singur mod (Deplasare la dreapta)

## Relație de recurență
`d[i][j] = d[i][j - 1] + d[i - 1][j - 1]` - În căsuța de pe poziția <b>i, j</b> se poate ajunge:
- printr-o deplasare din camera anterioară, aflată în stânga (d[i][j - 1]) (coloana anterioară, aceeași linie)
- printr-o deplasare din camera anterioară, aflată la stânga-sus (d[i - 1][j - 1]) - (coloana anterioară, linia anterioară)

## Soluție - 100P - C++ (Cu indexare de la 0)
```
#include <fstream>
#include <vector>
using namespace std;
ifstream f("pacman_xi.in");
ofstream g("pacman_xi.out");
int main()
{
	int n, m; f >> n >> m;
	vector<vector<long long>> d(n, vector<long long>(m));

	for (int i = 0; i < m; ++i)
		d[0][i] = 1;

	for (int i = 1; i < n; ++i)
		for (int j = 1; j < m; ++j)
			d[i][j] = d[i][j - 1] + d[i - 1][j - 1];

	g << d[n - 1][m - 1];
	return 0;
}
```
