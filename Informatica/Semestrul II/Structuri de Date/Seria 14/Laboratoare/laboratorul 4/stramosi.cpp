#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
const int NMAX = 250001;
const int LMAX=21;
vector<int> L[NMAX];
int stramos[NMAX][LMAX];
int tata[NMAX];
int main(){
    int n, m;
    ifstream fin("stramosi.in");
    ofstream fout("stramosi.out");
    fin>>n>>m;
    for(int i=1;i<=n;i++){
        int x;
        fin>>x;
        tata[i]=x;
    }
    for(int i=1;i<=n;i++){
        stramos[i][0] = tata[i];
    }
    for(int j=1;j<=20;j++){
        for(int i=1;i<=n;i++){
            stramos[i][j] = stramos[stramos[i][j-1]][j-1];
        }
    }
    for(int i=1;i<=m;i++){
        int p, q;
        fin>>p>>q;
        int j = 0;
        while(q) {
            if ((1 << j) & q) {
                p = stramos[p][j];
                q -= (1 << j);
            }
            j+=1;
        }


        fout<<p<<'\n';
    }
}