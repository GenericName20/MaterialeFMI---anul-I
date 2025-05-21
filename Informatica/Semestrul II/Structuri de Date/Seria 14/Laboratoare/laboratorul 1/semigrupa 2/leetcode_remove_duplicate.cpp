**
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* p=head, *q;
        if (p==NULL) //separat lista vida
            return p;
        /*idee: daca  valoarea din p = cea din p->next => sterg p->next (!!nu p)
         * */
        while (p->next){ //trebuie sa existe si p si p->next
            if (p->val == p->next->val){
                q=p->next;
                p->next=p->next->next;
                delete q; //eliberez memoria pentru vechiul p->next
            }
            else
                p=p->next;
        }
        return head;
    }
};
