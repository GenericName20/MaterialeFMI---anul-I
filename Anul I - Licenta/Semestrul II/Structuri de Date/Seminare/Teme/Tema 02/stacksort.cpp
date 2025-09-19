#include <iostream>
#include <stack>
#include <random>

int random_value() {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<int> range(1, 100);
	return range(gen);
}

int main() {
	std::stack<int> A, B;
	for (int i = 0; i < 10; ++i)
		A.push(random_value());

    while (!A.empty()) {
        int x = A.top();
        A.pop();

        while (!B.empty() && x <= B.top()) {
            A.push(B.top());
            B.pop();
        }

        B.push(x);
    }

    while (!B.empty()) {
        A.push(B.top());
        B.pop();
    }

    while (!A.empty()) {
        std::cout << A.top() << std::endl;
        A.pop();
    }

	return 0;
}