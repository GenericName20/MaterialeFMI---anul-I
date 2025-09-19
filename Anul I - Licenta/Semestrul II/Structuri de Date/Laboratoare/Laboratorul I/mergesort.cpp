// vlaxcs @ https://infoarena.ro/problema/algsort
#include <vector>
#include <fstream>
using namespace std;
ifstream f("algsort.in");
ofstream g("algsort.out");

void merge(vector<int>& v, int l, int m, int r)
{
	int s1(m - l + 1), s2(r - m), i, j, k;
	vector<int> L(s1 + 1), R(s2 + 1);
	for (i = 0; i < s1; ++i)
		L[i] = v[l + i];

	for (i = 0; i < s2; ++i)
		R[i] = v[m + i + 1];

	i = 0; j = 0; k = l;
	while (i < s1 && j < s2)
		if (L[i] <= R[j])
			v[k++] = L[i++];
		else
			v[k++] = R[j++];

	while (i < s1)
		v[k++] = L[i++];

	while (j < s2)
		v[k++] = R[j++];
}

void mS(vector<int>& v, int l, int r)
{
	if (l >= r)
		return;

	int m = l + (r - l) / 2;
	mS(v, l, m);
	mS(v, m + 1, r);
	merge(v, l, m, r);
}

int main()
{
	int n; f >> n;
	vector<int> v(n + 1);

	for (int i = 0; i < n; ++i) f >> v[i];
	mS(v, 0, n - 1);
	for (int i = 0; i < n; ++i) g << v[i] << " ";

	f.close(); g.close();
	return 0;
}