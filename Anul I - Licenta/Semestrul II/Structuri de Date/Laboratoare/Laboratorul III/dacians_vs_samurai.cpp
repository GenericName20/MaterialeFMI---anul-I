#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
vector<pair<int, int>> poll;
unordered_map<int, int> freq;
int main() {
    int n, a, b;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> a >> b;
        poll.emplace_back(a, i);
        poll.emplace_back(b, i);
    }

    sort(poll.begin(), poll.end());

    int total(0), left(0), answer(INT32_MAX);

    for (int right = 0; right < poll.size(); ++right) {
        ++freq[poll[right].second];
        if (freq[poll[right].second] == 1) {
            ++total;
        }

        while (total == n) {
            int current_diff = poll[right].first - poll[left].first;
            answer = min(answer, current_diff);

            --freq[poll[left].second];
            if (freq[poll[left].second] == 0) {
                --total;
            }
            ++left;
        }
    }

    cout << answer;
    return 0;
}