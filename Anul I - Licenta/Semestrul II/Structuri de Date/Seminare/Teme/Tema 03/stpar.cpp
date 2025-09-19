#include <iostream>
#include <stack>
#include <queue>
using namespace std;

bool reorder(queue<int> main) {
	queue<int> next;
	stack<int> sec;
	int exp(1);

	while (!main.empty() || !sec.empty()) {
		if (!main.empty() && main.front() == exp) {
			next.push(main.front());
			main.pop();
			exp++;
		}
		else if (!sec.empty() && sec.top() == exp) {
			next.push(sec.top());
			sec.pop();
			exp++;
		}
		else if (!main.empty()) {
			sec.push(main.front());
			main.pop();
		}
		else {
			return false;
		}
	}
	return true;
}

int main() {
	int count, aux, r;
	while (cin >> count) {
		if (count == 0) {
			return 0;
		}

		queue<int> main;
		for (int i = 0; i < count; ++i) {
			cin >> aux;
			main.push(aux);
		}

		if (reorder(main)) {
			cout << "yes" << endl;
		}
		else {
			cout << "no" << endl;
		}
	}
	return 0;
}