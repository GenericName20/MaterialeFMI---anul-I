#include <iostream>
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
void clear(node *&head ){
    node* p=head, *q;
    while(p){
        q=p;
        p=p->next;
        delete q;
    }
    head=NULL;
}

using namespace std;
int main(){
    int i,n, v[100000];
    node* stiva=NULL;
    cin>>n;
    int *ans=new int[n];
	//parcurgem elementele de la primul catre ultimul
    for(i=0;i<n;i++){
        cin>>v[i];
        ans[i]=-1;
        while (stiva && v[top(stiva)]<v[i]) {
                int j = top(stiva);
                ans[j] = v[i];
                stergereInceput(stiva);
            }
        adaugareInceput(stiva, i);

    }
    clear(stiva);
    for(i=0;i<n;i++)
        cout<<ans[i]<<" ";}