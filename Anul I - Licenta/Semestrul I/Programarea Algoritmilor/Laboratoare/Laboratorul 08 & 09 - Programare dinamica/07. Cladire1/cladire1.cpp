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