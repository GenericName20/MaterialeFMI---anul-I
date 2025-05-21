#include<fstream>
#include<queue>
using namespace std;
ifstream f("radixsort.in");
ofstream g("radixsort.out");
const int NMAX = 1000002;
long v[NMAX + 1];
queue<long> B[11];
int main(){
    int n;
    long nr_max=0;
    f>>n;
    for(int i=0;i<n;i++) {
        f >> v[i];
        nr_max = max(nr_max, v[i]);
    }
    int nr_cifre_max = 0;
    while(nr_max > 0) {
        nr_cifre_max++;
        nr_max /= 10;
    }
    int p = 1;
    //impartim in bucketuri pe rand vectorul dupa cifrele de la ultima la prima
    for(int i = 1; i <= nr_cifre_max; i++) {
        //determinam cifra c corespunzatoare puterii p
        //punem v[i] in bucketul c
        for (int j = 0; j < n; j++) {
            int c = (v[j] / p) % 10;
            B[c].push(v[j]);
        }
        //lipim bucketurile inapoi in v (!!buketurile raman goale)
        int j = 0;
        for (int c = 0; c <= 9; c++)
            while (!B[c].empty()) {
                v[j] = B[c].front();
                B[c].pop();
                j++;
            }

        //trecem la urmatoarea cifra (De la dreapta la stanga)
        p = p * 10;
    }
    for(int i = 0; i < n; i++) {
        g << v[i] << ' ';
    }
    g.close();
    return 0;
}



