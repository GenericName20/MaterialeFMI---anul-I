// 90 de puncte
#include <fstream>
#include <vector>
#include <fstream>
std::ofstream g("regine.out");
short n;
long solNr(0);
std::vector<short> x;
std::vector<bool> visited, d1, d2;
 
void printSol() {
	for (short i = 0; i < n; i++)
		g << x[i] << ' ';
	g << '\n';
}
 
void back(short k)
{
	for (short i = 0; i < n; i++)
	{
		if (!visited[i] && !d1[k + i] && !d2[k - i + n - 1])
		{
			visited[i] = d1[k + i] = d2[k - i + n - 1] = 1;
			x[k] = i + 1;
			if (k == n - 1)
			{
				if (solNr < 3)
					printSol();
				solNr++;
			}
			else
				back(k + 1);
			visited[i] = d1[k + i] = d2[k - i + n - 1] = 0;
		}
	}
}
 
int main()
{
	freopen("regine.in", "r", stdin);
	scanf("%hd", &n);
	x.resize(n);
	visited.resize(n);
	d1.resize(2 * n - 1);
	d2.resize(2 * n - 1);
	back(0);
	g << solNr;
	return 0;
}
