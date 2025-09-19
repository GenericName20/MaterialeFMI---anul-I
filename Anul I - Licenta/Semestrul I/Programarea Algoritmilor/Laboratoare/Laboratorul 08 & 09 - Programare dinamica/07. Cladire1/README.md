# Problema [Cladire1](https://www.pbinfo.ro/probleme/393/cladire1)

## Stare: 
- d[i][j] - Numărul de moduri în care se poate ajunge în camera de pe poziția <b>i, j</b>
- b[i][j] - Statusul camerei de pe poziția <b>i, j</b> (blocată = 1 / deblocată = 0)

## Stări inițiale
- d[1][1] = 1 - Se poate ajunge într-un singur mod în camera de start (Nu este blocată niciodată)
- Pentru orice <b>1 <= i <= m</b> - Se poate ajunge în camerele de pe prima linie într-un singur mod (Deplasare la dreapta):
```
- d[1][i] = 1, dacă b[1][i] = 0 și b[1][i - 1] = 0 (dacă avem camera curentă sau cea de pe coloana anterioară deblocate)
- d[1][i] = 0, dacă b[1][i] = 1 sau b[1][i - 1] = 1 (dacă avem camera curentă și cea de pe coloana anterioară blocate)
```

- Pentru orice <b>1 <= i <= n</b> - Se poate ajunge în camerele de pe prima coloană într-un singur mod (Deplasare în jos):
```
- d[i][1] = 1, <b>dacă b[i][1] = 0 și b[i - 1][1] = 0</b> (dacă avem camera curentă sau cea de pe linia anterioară deblocate)
- d[i][1] = 0, <b>dacă b[i][1] = 1 sau b[i - 1][1] = 1</b> (dacă avem camera curentă și cea de pe linia anterioară blocate)
```

## Relație de recurență
`d[i][j] = !b[i][j] * (d[i][j - 1] * !b[i][j - 1] + d[i - 1][j] * !b[i - 1][j])` - În camera de pe poziția <b>i, j</b> se poate ajunge, doar dacă aceasta este deblocată (!b[i][j]), astfel:
- printr-o deplasare din camera anterioară, aflată în stânga (d[i][j - 1]), dacă acea cameră este deblocată (!b[i][j - 1]) (coloana anterioară, aceeași linie)
- printr-o deplasare din camera anterioară, aflată sus (d[i - 1][j]), dacă acea cameră este deblocată (!b[i - 1][j]) (linia anterioară, aceeași coloană)

## Soluție - 100P - C++ (Cu indexare de la 0)
```
#include <fstream>
#include <vector>
using namespace std;
#define MOD 9901
ifstream f("cladire1.in");
ofstream g("cladire1.out");
int main()
{
    int n, m, k;
    f >> n >> m >> k;
    vector<vector<int>> d(n, vector<int>(m, 0)), b(n, vector<int>(m, 0));
    for (int i = 0; i < k; ++i)
    {
        int x, y;
        f >> x >> y;
        b[x - 1][y - 1] = 1;
    }

    d[0][0] = 1;
    for (int i = 1; i < n; ++i)
        d[i][0] = !b[i][0] * !b[i - 1][0] * d[i - 1][0];

    for (int j = 1; j < m; ++j)
        d[0][j] = !b[0][j] * !b[0][j - 1] * d[0][j - 1];

    for (int i = 1; i < n; ++i)
        for (int j = 1; j < m; ++j)
                d[i][j] = !b[i][j] * (d[i - 1][j] * !b[i - 1][j] + d[i][j - 1] * !b[i][j - 1]) % MOD;

    g << d[n - 1][m - 1];
    return 0;
}
```
