
#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
const int NMAX = 1e5;
int a[NMAX + 1],n;
int rmq[NMAX + 1][20]; //rmq[lungime vector][cea mai mare putere a lui 2 cane nu depaseste lungimea]
//int LOG[NMAX + 1];
void preproc_rmq(){
    /*programare dinamica
    rmq[i][j]=pozitia mininului pentru secventa care
              incepe pe pozitia i si are lungime 2^j
    */

    //stim direct: pentru j=0, adica secvente de lungime 2^0=1
    for(int i = 0; i < n; i++) {
        rmq[i][0] = a[i];
    }

    /*
    * relatia de recurenta- reducem secvente de lungime 2^j la secvente de lungime 2^{j-1},
    * mai exact, pentru a calcula rmq[i][j]
    * impartim secventa de lungime 2^j care incepe pe pozitia i in doua de lungime 2^{j-1} :
    * => doua subsecvente mai mici, una incepe pe pozitia i si cealalta pe i+2^{j-1}
    * pentru care min este deja calculat
    * Min pentru intreaga secventa(Deci rmq[i][j] este minimul dintre minimele celor doua subsecvente
    *  =>rmq[i][j] va fi  min(a[rmq[i][j-1]], a[rmq[i][i+2^{j-1} ]}
   */
    //ordine de calcul-crescator dupa lungime, pentru 2^j<=n
    for(int j=1; (1 << j) <= n; j++)
        for(int i=0;i+(1 << j)-1<n;i++)
            rmq[i][j] = min(rmq[i][j - 1], rmq[i + (1 << (j - 1))][j - 1]);

}

int query(int x,int y){
    //determinam k maxim cu 2^k<=lungimea secventei x,x+1,...y:
    /*consideram doua secvente de lungime 2^{k-1} care acopera secventa noastra:
    una in stanga, care incepe pe pozitia x,
     una in dreapta, care se termina pe pozitia y, deci incepe pe y - (1 << k) + 1
     */

    int k = log2(y - x + 1);
    //mai bine:
    //int k=lg[y-x+1]; //unde lg - vector in care am precalculat log2 cu relatia de recurenta lg[i] = lg[i / 2] + 1;
    return min(rmq[x][k], rmq[y - (1 << k) + 1][k]);
}
/*
int query2(int x, int y) {
    int diff = y - x + 1;
    int st = x;
    int sol = 1e9;
    for(int i = 0; (1 << i) <= diff; i++) {
        if((1 << i) & diff) {
            sol = min(sol, rmq[st][i]);
            st += (1 << i);
        }
    }
    return sol;
}*/
int main(){
    ifstream f("rmq.in");
    ofstream g("rmq.out");
    int m,x,y;
    f>>n>>m;
    for(int i=0;i<n;i++)
        f>>a[i];
/*
 * for(int i = 2; i <= n; i++) {
        lg[i] = lg[i / 2] + 1;
    }
 */
    preproc_rmq();

    for(int i=0;i<m;i++){
        f>>x>>y;
        g<<query(x-1,y-1)<<endl; //x-1 pentru ca am memorat vectorul  de la 0
    }
    f.close();
    g.close();
}