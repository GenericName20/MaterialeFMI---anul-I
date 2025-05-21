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
using namespace std;
int main(){
    int i,n, v[100000];
    node* stiva=NULL;
    cin>>n;
    int *ans=new int[n];

    for(i=0;i<n;i++)
        cin>>v[i];
	//parcurgem elementele de la ultimul catre primul
    for (i=n-1;i>=0;i--){
        ans[i]=-1;
        while (stiva && v[top(stiva)]<=v[i])
            stergereInceput(stiva);
        if (stiva!=NULL)
             ans[i]=v[top(stiva)];
        adaugareInceput(stiva,i);

    }
    for(i=0;i<n;i++)
        cout<<ans[i]<<" ";

}