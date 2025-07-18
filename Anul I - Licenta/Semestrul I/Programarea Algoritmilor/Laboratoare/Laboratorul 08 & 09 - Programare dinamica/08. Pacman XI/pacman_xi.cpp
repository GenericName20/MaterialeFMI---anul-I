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