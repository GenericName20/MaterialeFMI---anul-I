#include<fstream>
#include<iostream>
using namespace std;

struct node{
    int valoare;
    node* next;
};
void adaugareInceput(node* &head,  int x)
{
    node* element=new node;
    element->valoare=x;
    ///element->next=NULL;
    element->next=head; //devine NULL daca head este NULL

    head=element;

}

const int NMAX=100005;
const int LMAX=20;

int k, n,m;
int nivel[NMAX << 1], euler[NMAX << 1],prima_apar[NMAX]; //euler tur- 2*nr muchii

node* G[NMAX];

node* lastG[NMAX];

ifstream fin("lca.in");

void parcurg(int nod, int niv_curent) {
    k=k+1;
    euler[k] = nod;
    nivel[k] = niv_curent ;
    prima_apar[nod] = k;

    //node* p= G[nod];
    //while(p!=NULL)
    for (node* p= G[nod]; p!=NULL; p=p->next) {
        parcurg(p->valoare, niv_curent +1);

        k=k+1;
        euler[k] = nod;
        nivel[k] = niv_curent ;
        //p=p->next;
    }


}

void adaugareFinal(node* &head, node* &last, int x)
{
    node* element=new node;
    element->valoare=x;
    element->next=NULL;
    if(head==NULL) //separat cazul in care lista este vida
        head=element;
    else last->next=element;
    last=element;
}

int main() {
    int x;
    fin >> n >> m;
    for (int i = 1; i <= n; i++)
        G[i] = lastG[i]= NULL;

    for (int i = 2; i <= n; i++) {
        fin >> x;
        //adaugareInceput(G[x], i);
        adaugareFinal(G[x],lastG[x],i);
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