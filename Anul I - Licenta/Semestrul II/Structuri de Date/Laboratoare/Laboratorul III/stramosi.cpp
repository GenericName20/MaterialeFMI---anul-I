#include <fstream>
using namespace std;
ifstream f("stramosi.in");
ofstream g("stramosi.out");

#define NLIM 250000
#define LOG 18

int anc[NLIM + 1][LOG + 1], n, m;
int main() {
	f >> n >> m;

	for (int i = 1; i <= n; ++i) {
		f >> anc[i][0];
	}

	for (int j = 1; j <= LOG; ++j) {
		for (int i = 1; i <= n; ++i) {
			int m = anc[i][j - 1];
			anc[i][j] = anc[i][j - 1] ? anc[m][j - 1] : 0;
		}
	}

	while (m--) {
		int p, q;
		f >> q >> p;
		
		for (int j = LOG; j >= 0 && q; --j) {
			if (p & (1 << j)) {
				q = anc[q][j];
			}
		}
		
		g << q << '\n';
	}
	
	f.close();
	g.close();
	return 0;
}