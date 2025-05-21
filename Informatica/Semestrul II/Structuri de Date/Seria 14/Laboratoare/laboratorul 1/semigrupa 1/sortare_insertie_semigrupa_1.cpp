#include<iostream>
#include "operatii_liste_semigrupa_1.cpp"
using namespace std;
void insert_in_order(node *&head,node *&last, int x){
    /*
     * cazuri speciale
     * - x se insereaza la inceput(este mai mic decat primul)
     * x se insereaza la final (este mai mare decat ultimul)
     */
    if ((head==NULL) || (x<=head->value)){
        insert_node_begin(head,last,x);
    }
    else
        if (last->value<=x) {
            insert_node_end(head, last, x);
        }
        else {

            node *p=head;
            /*
            while(x>=p->info)
                p=p->next;
            cout<<p->info<<endl;
            insert_before(head,last,p,x);*/
            while(!(p->value<=x and x<=p->next->value)) //cautam intre ce noduri trebuie inserat x
                p=p->next;
            node* q=new node;//inserez nodul q cu informatia x intre p si p->next
            q->value=x;
            q->next=p->next;
            p->next=q;
        }

}
void sortare_insertie(){
    node *head=NULL,*last=NULL;
    int n,x;
    cout<<"cate numere? ";
    cin>>n;
    cout<<"introduceti numerele ";
    for(int i=0;i<n;i++){
        cin>>x;
        insert_in_order(head,last,x);
        print_list(head);
    }


}
int main(){
    sortare_insertie();
    /*TEMA - de adaptat pentru leetcode*/
}