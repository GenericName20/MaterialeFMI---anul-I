/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void adaugareFinal(ListNode* &head, ListNode* &last, int x)
    {
        ListNode* element=new ListNode;
        element->val =x;
        element->next=NULL;
        if(head==NULL) //separat cazul in care lista este vida
            head=element;
        else last->next=element;
        last=element;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //prima cifra din lista este a unitatilor
        ListNode*p1=l1, *p2=l2;
        ListNode*head=NULL,*last=NULL;
        int t=0;
        while(p1 && p2){//parcurgem simultan cifra cu cifra ambele numere, de la unitati
            int r=p1->val+p2->val+t;
            t=r/10;//cifra de transport
            r=r%10;
            adaugareFinal(head,last,r);
            p1=p1->next;
            p2=p2->next;
        }
        //cand se termina unul dintre numere - continui cu cel ramas, !!!la cifra de trasport
        if (p2)
            p1=p2;
        while(p1){
            int r=p1->val+t;
            t=r/10;
            r=r%10;
            adaugareFinal(head,last,r);
            p1=p1->next;
        }
        if (t!=0) //daca mai ramane o cifra de transport
            adaugareFinal(head,last,t);
        return head;
    }



};