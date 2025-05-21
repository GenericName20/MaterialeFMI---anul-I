#include <iostream>

using namespace std;

struct node{
    int valoare;
    node* next;
};

void adaugareInceput(node* &head, node* &last, int x)
{
    node* element=new node;
    element->valoare=x;
    ///element->next=NULL;
    element->next=head; //devine NULL daca head este NULL
    if(head==NULL) //separat cazul in care lista este vida-> se actualizeaza si last
        last=element;
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

void stergereInceput(node* &head, node* &last)
{
    if(head==NULL)
        return;
    node* p=head;
    head=head->next;
    delete p;
    if(head==NULL) //cazul cand lista ramane vida- se modifica si last
        last=NULL;

}

void stergereFinal(node* &head, node* &last)
{
    node* p=head;
    if(head==NULL)
        return;
    if(head==last) //lista cu un element, echivalent cu head->next==NULL
    {
        delete head;
        head=NULL;
        last=NULL;
        return;
    }
    while(p->next->next) //ne pozitionam pe penultimul element pentru a il sterge pe ultimul
    {
        p=p->next;
    }
    delete p->next;
    last=p;
    p->next=NULL;
}

void inserare(node* &head, node* &last, int x, int poz)
{
    if(poz==0)
    {
        adaugareInceput(head, last, x);
        return;
    }
    /*!!separat cazul de lista vida in care vrem sa inseram pe pozitie>0*/
    if (head==NULL)
        return;
    int cnt=0;
    node* p=head;
    while(cnt<poz-1) //ne pozitionam inainte sa inseram, puteam folosi si for
    {
        p=p->next;
        if(p==NULL) //daca am iesit din lista poz este prea mare->nu inseram
        {
            return;
        }
        cnt++;
    }
    node* q=new node;
    q->valoare=x;
    q->next=NULL;
    q->next=p->next;
    p->next=q;
    if(q->next==NULL) //am adaugat la final daca dupa noul nod nu urmeaza alt nod
        last=q;

}

void stergere(node* &head, node* &last, int poz)
{
    if(poz==0)
    {
        stergereInceput(head, last);
        return;
    }
    /*!!separat cazul de lista vida */
    if(head==NULL)
        return;
    int cnt=0;
    node* p=head;
    while(cnt<poz-1) //ne pozitionam tot inaine de elementul de sters
    {
        p=p->next;
        if(p==NULL) //daca am iesit din lista poz este prea mare->nu inseram
        {
            return;
        }
        cnt++;
    }
    //suntem pozitionati inainte de poz
    //stergem p->next, daca exista
    if(p->next) {
        node *q;
        q = p->next; //elementul care va fi sters
        p->next = p->next->next;
        delete q;
        if (p->next == NULL)
            last = p;
    }



}

void afisare(node* head)
{
    node* p=head;
    while(p)
    {
        cout<<p->valoare<<' ';
        p=p->next;
    }
    cout<<endl;
}


/*

int main()
{
    node* head=NULL;
    node* last=NULL;
    adaugareInceput(head, last, 12);
    adaugareInceput(head, last, 7);
    adaugareFinal(head, last, 29);
    adaugareFinal(head, last, 50);
    for(int i=1;i<=5;i++)
    {
        afisare(head);
        stergereInceput(head, last);
    }
    adaugareFinal(head, last, 15);
    adaugareFinal(head, last, 16);
    stergereFinal(head, last);
    stergereFinal(head, last);
    adaugareFinal(head, last, 16);
    adaugareInceput(head, last, 17);
    adaugareFinal(head, last, 16);
    adaugareInceput(head, last, 17);
    inserare(head, last, 40, 4);
    adaugareFinal(head, last, 39);
    afisare(head);
    for(int i=1;i<=5;i++)
    {
        afisare(head);
        stergereInceput(head, last);
    }
    for(int i=1;i<=5;i++)
    {

        inserare(head, last,i,i);
        afisare(head);
    }
    inserare(head, last,11,11);
    afisare(head);
    inserare(head, last,14,11);
    afisare(head);
    inserare(head, last,10,14);
    afisare(head);
    adaugareFinal(head, last, 100);
    afisare(head);
    for(int i=0;i<=5;i++)
    {

        stergere(head, last,i);
        afisare(head);
    }
    stergere(head, last,7);
    afisare(head);
    stergere(head, last,7);
    afisare(head);
    return 0;
}*/
