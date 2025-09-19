#include <vector>
#include <fstream>
using namespace std;
ifstream f("schi.in");
ofstream g("schi.out");
vector <int> v;
int main()
{
    int n, pos;
    f >> n;
    for (int i = 0; i < n; i++)
    {
        f >> pos;
        v.insert(v.begin() + pos - 1, i + 1);
    }

    for (int i = 0; i < v.size(); ++i) {
        g << v[i] << endl;
    }

    f.close();
    g.close();
    return 0;
}