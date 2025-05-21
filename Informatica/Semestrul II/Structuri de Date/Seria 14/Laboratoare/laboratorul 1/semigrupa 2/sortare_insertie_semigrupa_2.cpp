#include<iostream>
#include "operatii_liste_semigrupa_2.cpp"
using namespace std;
void insert_in_order(node *&head,node *&last, int x){
    /*
     * cazuri speciale
     * - x se insereaza la inceput(este mai mic decat primul)
     * x se insereaza la final (este mai mare decat ultimul)
     */
    if ((head==NULL) || (x<=head->valoare)){
        adaugareInceput(head,last,x);
    }
    else
    if (last->valoare<=x) {
        adaugareFinal(head, last, x);
    }
    else {

        node *p=head;
        /*
        while(x>=p->info)
            p=p->next;
        cout<<p->info<<endl;
        insert_before(head,last,p,x);*/
        while(!(p->valoare<=x and x<=p->next->valoare)) //cautam intre ce noduri trebuie inserat x
            p=p->next;
        node* q=new node;//inserez nodul q cu informatia x intre p si p->next
        q->valoare=x;
        q->next=p->next;
        p->next=q;
    }

}
void sortare_insertie(){
    node *head=NULL,*last=NULL;
    int n,x;
    cout<<"Cate numere? ";
    cin>>n;
    cout<<"introduceti numerele ";
    for(int i=0;i<n;i++){
        cin>>x;
        insert_in_order(head,last,x);
        afisare(head);
    }


}
int main(){
    sortare_insertie();
    /*TEMA - de adaptat pentru leetcode*/
}