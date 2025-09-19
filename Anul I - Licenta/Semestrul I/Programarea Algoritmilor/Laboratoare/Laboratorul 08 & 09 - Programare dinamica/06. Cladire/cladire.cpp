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