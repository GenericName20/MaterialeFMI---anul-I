#include <fstream>
#include <string>
#include <stack>
#include <map>

std::string getData() {
	std::ifstream f("evaluare.in");
	std::string input;
	f >> input;
	f.close();
	return input;
}

void putData(int output) {
	std::ofstream f("evaluare.out");
	f << output;
	f.close();
}

std::map<char, int> priority = {
	{'*', 2}, {'/', 2},
	{'+', 1}, {'-', 1},
	{'(', 0}
};

int eval(std::stack<int>& numbers, std::stack<char>& ops) {
	int y(numbers.top()); numbers.pop();
	int x(numbers.top()); numbers.pop();
	char op(ops.top()); ops.pop();

	switch (op) {
		case '+': return x + y;
		case '-': return x - y;
		case '*': return x * y;
		case '/': if (y != 0) return x / y; return 0;
		default: return y;
	}
}

int getResult(std::string exp) {
	std::stack<int> numbers;
	std::stack<char> ops;

	for (int i = 0; i < exp.size(); ++i) {
		if (exp[i] == ' ') {
			continue;
		}
		else if (exp[i] >= 48 && exp[i] <= 57) {
			int aux(0);
			while (exp[i] >= 48 && exp[i] <= 57) {
				aux = aux * 10 + (exp[i++] - 48);
			}
			i--;
			numbers.push(aux);
		}
		else if (exp[i] == '(') {
			ops.push('(');
		}
		else if (exp[i] == ')') {
			while (ops.top() != '(') {
				numbers.push(eval(numbers, ops));
			}
			ops.pop();
		}
		else {
			while (!ops.empty() && priority[ops.top()] >= priority[exp[i]]) {
				numbers.push(eval(numbers, ops));
			}
			ops.push(exp[i]);
		}
	}

	while (!ops.empty()) {
		numbers.push(eval(numbers, ops));
	}

	int x = numbers.top();
	numbers.pop();
	return x;
}

int main() {
	std::string exp(getData());
	putData(getResult(exp));
	return 0;
}