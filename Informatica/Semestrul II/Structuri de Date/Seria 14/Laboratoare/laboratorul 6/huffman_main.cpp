#include <iostream>
#include <string>
#include <unordered_map>
#include <queue>

using namespace std;





struct node {
    int frecventa;
    char c;
    node* left;
    node* right;


    bool operator ()(node* stanga, node* dreapta) {
        return stanga->frecventa > dreapta->frecventa;
    }

};


unordered_map<char, string> codificare;

void codificari(node* radacina, string cod) {

    if(radacina->left == nullptr && radacina->right == nullptr) {
        codificare[radacina->c] = cod;
    }
    else {
        codificari(radacina->left, cod + "0");
        codificari(radacina->right, cod + "1");
    }
}

string decodificare(string codif, node* radacina) {

    string decodif = "";
    node* start = radacina;

    for(auto c : codif) {
        if(c == '0') {
            radacina = radacina->left;
        }
        else if(c == '1')
            radacina = radacina->right;

        if(radacina->left == nullptr && radacina->right == nullptr) {
            decodif += radacina->c;
            radacina = start;
        }
    }

    return decodif;

}



/// AAAABCCDDEEEE

int main()
{
    unordered_map<char, int> frec;
    string input;
    cin >> input;

    for(int i = 0; i < input.size(); i++) {
        frec[input[i]]++;
    }

    priority_queue<node*, vector<node*>, node> pq;


    for(auto it : frec) {
        node* nod = new node;
        nod->c = it.first;
        nod->frecventa = it.second;
        nod->left = nullptr;
        nod->right = nullptr;
        pq.push(nod);
    }


    while(pq.size() > 1) {
        node* nod1 = pq.top();
        pq.pop();

        node* nod2 = pq.top();
        pq.pop();

        node* newNod = new node;

        newNod->frecventa = nod1->frecventa + nod2->frecventa;
        newNod->c = ' ';
        newNod->left = nod1;
        newNod->right = nod2;

        pq.push(newNod);
    }


    node* arbore = pq.top();

    codificari(arbore, "");


     for(auto it : codificare) {
        cout << it.first << ' ' << it.second << endl;
    }

    string codif = "";

    for(int i = 0; i < input.size(); i++) {

        codif += codificare[input[i]];
    }


    cout << codif << endl;


    cout << decodificare(codif, arbore);



    return 0;
}
