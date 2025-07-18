#include <iostream>
#include <stack>
#include <queue>

struct node {
	int value;
	node* next;
};

int main()
{
	node* temp;
	std::queue<node*> B;

	int n, value;
	std::cin >> n >> value;

	node* first = new node{ value, nullptr };
	node* current = first;
	
	for (int i = 2; i <= n; ++i){
        std::cin >> value;
        node* new_connection = new node{ value, nullptr };
        current->next = new_connection;
        current = new_connection;
    }

	while (first != nullptr) {
		node* r = first->next;
		if (first->next) {
			node* last = first->next;
			while (last->next && last->next->next) { 
				last = last->next;
			}

			if (last->next) {
				node* temp = last->next;
				last->next = nullptr;
				last = temp;
				first->next = last;
			}
			else {
				r = nullptr;
			}
		}

		B.push(first);
		first = r;
	}

	if (!B.empty()) {
		first = B.front();
		current = first;
		B.pop();
		// stim ca doar ultimul element din coada poate sa nu aiba o conexiune,
		// asadar este garantat ca saritura peste doi pointeri este safe cata vreme coada nu e vida
		while (!B.empty()) {
			current->next->next = B.front();
			B.pop();
			current = current->next->next;
		}
	}

	current = first;
	while (current != nullptr) {
		std::cout << current->value << " ";
		current = current->next;
	}

	return 0;
}