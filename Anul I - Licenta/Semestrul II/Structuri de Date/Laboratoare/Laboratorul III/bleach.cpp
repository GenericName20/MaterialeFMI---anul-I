#include <fstream>
#include <queue>
using namespace std;
ifstream f("bleach.in");
ofstream g("bleach.out");
int main() {
	int n, k, temp, lowest;
	long long total(0), answer(0);
	f >> n >> k;

	priority_queue<int, vector<int>, greater<>> pws;

	for (int i = 0; i <= k; ++i) {
		f >> temp;
		pws.push(temp);
	}

	while (!pws.empty()) {
		lowest = pws.top(); pws.pop();

		if (lowest - total > answer) {
			answer = lowest - total;
		}

		total += lowest;

		if (++k < n) {
			f >> temp;
			pws.push(temp);
		}
	}

	g << answer;

	f.close();
	g.close();
	return 0;
}