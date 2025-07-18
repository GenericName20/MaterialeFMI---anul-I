// Matteo Veroztti (Accepted)
#include <bits/stdc++.h>
#ifdef BLAT
    #include "debug/debug.hpp"
#else
    #define debug(x...) 42
#endif

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<vector<bool>> likes(n, vector(n, true));
    vector<int> sol;
    sol.push_back(0);

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= i; j++) {
            int x;
            cin >> x;
            if (j > (i + 1) / 2)
                likes[i][x] = false;
        }

        // Can I put it next to the first one?
        if (likes[i][sol[0]]) {
            sol.insert(sol.begin(), i);
            continue;
        }
        // Can I put it next to the last one?
        if (likes[i][sol.back()]) {
            sol.push_back(i);
            continue;
        }

        // Else, there surely exists a position in between
        // I can insert i
        for (size_t k = 1; k < sol.size() - 1; k++) {
            if (likes[i][sol[k]] && likes[i][sol[k + 1]]) {
                sol.insert(sol.begin() + k + 1, i);
                break;
            }
        }
    }
    for (auto it : sol)
        cout << it << " ";
    cout << '\n';
    return 0;
}