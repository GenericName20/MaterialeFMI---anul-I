```
#include <iostream>
#include <queue>

class Stack {
private:
    std::queue<int> Q1;

public:
    void push(int x) {
        std::queue<int> Q2;
        Q2.push(x);

        while (!Q1.empty()) {
            Q2.push(Q1.front());
            Q1.pop();
        }

        std::swap(Q1, Q2);
    }

    void pop() {
        if (Q1.empty()) {
            std::cout << "Empty stack!" << std::endl;
        } else {
            Q1.pop();
        }
    }

    int top() {
        if (Q1.empty()) {
            std::cout << "Empty stack!" << std::endl;
            return -1;
        }
        return Q1.front();
    }

    bool isEmpty() {
        return Q1.empty();
    }
};

int main() {
    Stack s;

    // Adds [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    for (int i = 0; i < 10; ++i) {
        s.push(i * 10);
    }

    s.pop(); // Pops 90 out of stack
    s.pop(); // Pops 80 out of stack

    // Remaining stack contents
    while (!s.isEmpty()) {
        std::cout << s.top() << " ";
        s.pop();
    }

    return 0;
}