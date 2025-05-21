#include<fstream>
#include<iostream>
#include<vector>
using namespace std;


const int NMAX=100005;
const int LMAX=20;

int k, n,m;
int nivel[NMAX << 1], euler[NMAX << 1],prima_apar[NMAX]; //euler tur- 2*nr muchii

vector<int> G[NMAX];



ifstream fin("lca.in");

void parcurg(int nod, int niv_curent) {
    k=k+1;
    euler[k] = nod;
    nivel[k] = niv_curent ;
    prima_apar[nod] = k;


    for (auto it: G[nod]) {
        parcurg(it, niv_curent +1);

        k=k+1;
        euler[k] = nod;
        nivel[k] = niv_curent ;

    }


}


int main() {
    int x;
    fin >> n >> m;


    for (int i = 2; i <= n; i++) {
        fin >> x;
        G[x].push_back(i);
    }
    k = -1;
    parcurg(1, 0);
    for (int i = 0; i <= k; i++)
        cout<<euler[i]<<" ";
    cout<<"\n";
    for (int i = 0; i <= k; i++)
        cout<<nivel[i]<<" ";
    cout<<"\n";
}