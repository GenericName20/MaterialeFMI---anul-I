#include <fstream>
using namespace std;
int main()
{
	int n;
	FILE* f = fopen("cod.in", "r");
	fscanf(f, "%d", &n);
	int** t = (int**)malloc(n * sizeof(int*));
	int** d = (int**)malloc(n * sizeof(int*));
	for (int i = 0; i < n; ++i)
	{
		t[i] = (int*)malloc((i + 1) * sizeof(int));
		d[i] = (int*)malloc((i + 1) * sizeof(int));
		for (int j = 0; j <= i; ++j)
		{
			fscanf(f, "%d", &t[i][j]);
			d[i][j] = 0;
		}
	}
	fclose(f);

	for (int i = 0; i < n; ++i)
		d[n - 1][i] = t[n - 1][i];
	for (int i = n - 2; i >= 0; --i)
		for (int j = 0; j <= i; ++j)
			d[i][j] = t[i][j] + (d[i + 1][j] > d[i + 1][j + 1] ? d[i + 1][j] : d[i + 1][j + 1]);
	
	FILE* g = fopen("cod.out", "w");
	fprintf(g, "%d", d[0][0]);
	fclose(g);
	return 0;
}