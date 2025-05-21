#include <iostream>

using namespace std;

struct node
{
    int value;
    node *next = NULL;
    node()
    {
        value = 0;
    }
    node (int _value)
    {
        value = _value;
    }
};

void insert_node_begin(node *&head, node *&last, int value)
{
    node *x = new node(value);
    /* se putea scrie fara constructor:
     node *x=new node;
     x->value=value;
     x->next=NULL:
     */
    if(head == NULL) //separat inserare in lista vida
    {
        head = x;
        last = x;
    }
    else
    {
        x->next = head;
        head = x;
    }
}

void insert_node_end(node *&head, node *&last, int value)
{
    node * x= new node(value);
    if(head == NULL) //separat inserare in lista vida
    {
        head = x;
        last = x;
    }
    else
    {
        last -> next = x;
        last = x;
    }
}

void delete_node_begin(node *&head, node *&last)
{
    if(head != NULL)
    {
        node *new_head = head->next;
        delete head;
        head = new_head;
        if(head==NULL)//cazul cand lista ramane vida- se modifica si last
            last=NULL;
    }
}

void delete_node_end(node *&head, node *&last)
{
    //daca lista este vida (head=NULL) - nu facem nimic
    if(head == last && head != NULL) //daca lista are un singur element - devine vida
    {
        delete head;
        head = NULL;
        last = NULL; //!!si last devine NULL

    }
    else if(head != NULL) //cel putin doua elemente
    {
        node *x = head;
        while(x->next->next != NULL) ///pentru ca vreau in afara while-ului sa fiu pe penultimul element
        {
            x = x-> next;
        }
        delete x->next;///sterg ultimul element
        x->next = NULL;
        last = x;
    }
}
/*in lucru - inserarea si stergerea pe/de pe o pozitie data */

void insert_node_mid(node *&head, node *&last, int value, int position)
{
    /* ce vrem sa facem daca position>lungimea listei? Variante:
     * - inseram la final - da
     * -nu mai inseram - vezi  implementarea de la cealalta semigrupa*/

    /*separat cazul in care inseram la inceput- se modifica head*/
    if(position==0)
    {
        insert_node_begin(head, last, value);
        return;
    }
    /*!!separat cazul de lista vida in care vrem sa inseram pe pozitie>0*/
    if (head==NULL){
        insert_node_begin(head, last, value);
        return;
    }
    node *x = head;
    while(position-- && x->next != NULL)
        x = x->next;
    node *new_node = new node(value);
    new_node->next = x->next;
    x->next = new_node;
    /*daca este ultimul element - se actualizeaza si last*/
    if (new_node->next==NULL)
        last=new_node;
}




/*
 * void delete_node_mid(node *&head, node *&last, int position){


}*/
//implementarea de la semigrupa 2
 void delete_node_mid(node* &head, node* &last, int position)
{
    if(position==0)
    {
        delete_node_begin(head, last);
        return;
    }
    /*!!separat cazul de lista vida */
    if(head==NULL)
        return;
    int cnt=0;
    node* p=head;
    while(cnt<position-1) //ne pozitionam tot inaine de elementul de sters
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




void print_list(node *head)
{
    node *p = head;
    while(p != NULL)
    {
        cout << p -> value << " ";
        p = p->next;
    }
    cout<<endl;
}

/*
int main()
{
    node *head, *last;
    head = last = NULL;
    insert_node_begin(head, last, 5);
    insert_node_begin(head, last, 6);
    insert_node_end(head, last, 4);
    print_list(head);
    delete_node_end(head, last);
    print_list(head);

    for(int i=0;i<2;i++) {
        delete_node_end(head, last);

        delete_node_begin(head, last);

        print_list(head);

    }


    for(int i=1;i<=5;i++)
    {

        insert_node_mid(head, last,i,i);
        print_list(head);
    }
    /*
    for(int i=1;i<=5;i++)
    {

        insert_node_mid(head, last,i*10,i-1);
        print_list(head);
    }
*/
/*
    for(int i=0;i<=5;i++)
    {

        delete_node_mid(head, last,i);
        print_list(head);
    }
    delete_node_mid(head, last,7);
    print_list(head);
    delete_node_mid(head, last,0);
    print_list(head);
    for(int i=0;i<=3;i++)
    {

        delete_node_mid(head, last,1);
        print_list(head);
    }
    delete_node_mid(head, last,0);
    print_list(head);
    delete_node_mid(head, last,0);
    print_list(head);
    insert_node_begin(head, last, 6);
    insert_node_end(head, last, 4);
    print_list(head);
    return 0;
}
*/