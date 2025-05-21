#include <iostream>
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
void stergereInceput(node* &head)
{
    if(head==NULL)
        return;
    node* p=head;
    head=head->next;
    delete p;


}
int top(node *&head ){
    return head->valoare;
}
void print(node* head){
    node*p;
    p = head;
    while(p){
        cout<<p->valoare <<" ";
        p=p->next;

    }
    cout<<endl;

}
void stergereInceput(node* &head, node* &last)
{
    if(head==NULL)
        return ;
    node* p=head;
    head=head->next;
    delete p;
    if(head==NULL) //cazul cand lista ramane vida- se modifica si last
        last=NULL;

}
void clear(node *&head ){
    node* p=head, *q;
    while(p){
        q=p;
        p=p->next;
        delete q;
    }
    head=NULL;
}

const int NMAX=100; //!!! Atentie la constrangerile problemei

int main() {
    int tata[NMAX],n;
    cin>>n;
    //VARIANTE:
   /*Varianta 1
    node** lista_fii ;
    lista_fii=new node*[n+1];
    */
    /*Varianta 2
    node* lista_fii[n+1] ;
    int niv[n+1] ;
    */
    node* lista_fii[NMAX] ; //vector de liste
    int niv[NMAX] ;


    for(int i=0;i<n;i++) {
        cin >> tata[i];
        lista_fii[i] = NULL; //fiecare lista trebuie initializata cu NULL
    }
    lista_fii[n] = NULL;
    int rad;
    for(int i=0;i<n;i++)
        if (tata[i]!=0)
            adaugareInceput(lista_fii[tata[i] ],i+1);
        else
            rad=i+1;
    for(int i=1;i<=n;i++) {
        cout << "nodul " << i<<" ";
        print(lista_fii[i]);
    }
    //coada cu nodurile pe niveluri
    node *coada_head=NULL, *coada_last=NULL;
    adaugareFinal(coada_head,coada_last,rad);
    niv[rad]=1;
    int niv_curent=1; //nivelul pe care este nodul curent explorat
    while(coada_head){
        int x= top(coada_head);
        if (niv[x]!=niv_curent) {
            niv_curent = niv[x];
            cout << endl;
        }
        stergereInceput(coada_head,coada_last);
        cout<<x<<" ";

        node* p=lista_fii[x];
        while(p){

            adaugareFinal(coada_head,coada_last,p->valoare);
            niv[p->valoare]=niv[x]+1; //nivelul fiului este cu 1 mai mare decat al tatalui

            p=p->next;
        }
    }
}
