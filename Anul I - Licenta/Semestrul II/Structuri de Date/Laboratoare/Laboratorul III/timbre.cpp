#include <fstream>
#include <queue>
using namespace std;

ifstream f("timbre.in");
ofstream g("timbre.out");

priority_queue<pair<int, int>> units;
priority_queue<int, vector<int>, greater<>> costs;

int main() {
    int n, m, k;
    f >> n >> m >> k;

    for (int i = 0; i < m; ++i) {
        int upper_bound, price;
        f >> upper_bound >> price;
        units.emplace(upper_bound, price);
    }

    int answer = 0;

    while (n > 0) {
        while (!units.empty() && units.top().first >= n) {
            costs.push(units.top().second);
            units.pop();
        }

        answer += costs.top();
        costs.pop();
        n -= k;
    }

    g << answer;
    return 0;
}