# Tema 3 - Structuri de Date

## Problema I - [Implementarea cu 2 cozi a unei stive](https://leetcode.com/problems/implement-stack-using-queues/)

### Enunț

Explicați cum puteți implementa o stivă cu 2 cozi (complexitatea operațiilor push și pop) / implementare opțională.

### Soluție

Pentru a implementa o stivă folosind 2 cozi, putem proceda astfel:

Considerăm X elementul care urmează să fie inserat în stivă.
Îl inserăm pe X în a doua coadă (Q2) și mutăm elementele din prima coadă (Q1) în continuarea lui (în Q2), păstrându-i prioritate maximă. Ulterior, se interschimbă conținutul celor două cozi pentru ușurință în manipularea repetată a acestora.

#### Operația .push()
- Pentru acest procedeu, vor fi necesare două parcurgeri (una pentru a muta elementele din Q1 în Q2 și încă una pentru a le muta înapoi din Q2 în Q1, după inserarea elementului X). Astfel, complexitatea timp a acestei operații este O(n), iar a doua interschimbare se realizează prin <code>std::swap</code>.

#### Operația .pop()
- Deoarece manipulăm coada Q1 simulând principiile unei stive, operația presupune extragerea elementului cu prioritate maximă și o scădere a dimensiunii cozii, deci complexitatea timp este O(1).

#### [Implementare](dqstack.cpp)
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
```

## Problema II - [Evaluare](https://www.infoarena.ro/problema/evaluare)

### [Soluție](evaluare.cpp)

Complexitate timp: O(n) | Memorie suplimentară: O(n)

```
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
```

## Problema III - [STPAR](https://www.spoj.com/problems/STPAR/)

### [Soluție](stpar.cpp) - AC

Complexitate timp: O(n) | Memorie suplimentară: O(n)

```
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
```

## Problema IV - [Substring with concatenation of all words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)


### [Soluția I](substring-with-concatenation-of-all-words.cpp) - 179 / 182 - Intuitiv, metoda discutată la seminar

```
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <string>

class Solution {
public:
    std::vector<int> findSubstring(std::string s, std::vector<std::string>& words) {
        int word_length(words[0].size());
        if (word_length > s.size()) {
            return std::vector<int>();
        }

        // Set every word's frequency in given list
        std::unordered_map<std::string, int> words_map;

        /*
            if (words_map.find(word) == words_map.end()) {
                words_map[word] = 0;
            }
        */
        words_map.clear();

        for (std::string word : words) {
            ++words_map[word];
        }

        // Find words_map from given list, in the first string
        std::vector<std::string> start(s.size(), "");
        for (int i = 0; i <= s.length() - word_length; ++i) {
            std::string current_word;
            current_word = s.substr(i, word_length);
            if (words_map.find(current_word) != words_map.end()) {
                // Set every word to the position it belongs to, in the first string
                start[i] = current_word;
            }
        }

        // Find subarrays of concatenated words_map from the given list
        std::vector<int> result;
        for (int i = 0; i < s.size(); ++i) {
            if (start[i] != "") {
                std::unordered_map<std::string, int> subarray;
                subarray[start[i]] = 1;
                for (int j = i + word_length;
                    j < s.size()
                    && start[j] != ""
                    && words_map.find(start[j]) != words_map.end();
                    j += word_length) {
                    if (subarray.find(start[j]) == subarray.end()) {
                        subarray[start[j]] = 1;
                    }
                    else if (subarray[start[j]] < words_map[start[j]]) {
                        ++subarray[start[j]];
                    }
                    else {
                        break;
                    }
                }

                if (subarray.size() == words_map.size()) {
                    bool concat(true);
                    for (auto& pair : subarray) {
                        if (subarray[pair.first] != words_map[pair.first]) {
                            concat = false;
                            break;
                        }
                    }

                    if (concat) {
                        result.push_back(i);
                    }
                }
            }
        }

        return result;
    };
};

int main() {
    std::string s;
    std::getline(std::cin, s);

    std::string all_words;
    std::getline(std::cin, all_words);

    std::stringstream ss(all_words);
    std::string word;
    std::vector<std::string> words;
    while (ss >> word) {
        words.push_back(word);
    }

    Solution sol;
    for (auto it : sol.findSubstring(s, words)) {
        std::cout << it << " ";
    }
    return 0;
}
```

### [Soluția II](https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1605105953/) - Beats 94% / Sliding Window
```
class Solution {
public:
    std::vector<int> findSubstring(std::string s, std::vector<std::string>& words) {
        int word_length(words[0].size());
        if (word_length > s.size()) {
            return std::vector<int>();
        }

        std::unordered_map<std::string, int> words_map;
        for (std::string word : words) {
            ++words_map[word];
        }

        std::vector<int> result;
        for (int i = 0; i < word_length; ++i) {
            int window_size = 0;
            std::unordered_map<std::string,  int> visited_word;
            for (int j = i; j + word_length <= s.size(); j += word_length) {
                std::string current_word = s.substr(j, word_length);

                auto it = words_map.find(current_word);
                if (it == words_map.end()) {
                    visited_word.clear();
                    window_size = 0;
                    continue;
                }

                ++visited_word[current_word];
                ++window_size;
                while (visited_word[current_word] > it->second) {
                    std::string first = s.substr(j - (window_size - 1) * word_length, word_length);
                    --visited_word[first];
                    --window_size;
                }
                
                if (window_size == words.size()){
                    result.push_back(j - (window_size - 1) * word_length);
                }
            }
        }

        return result;
    };
};
```

## Problema V - [Happy Number](https://leetcode.com/problems/happy-number/)

Intuind, am vrut să invalidez toate cazurile în care ajung la numere ireductibile prin aplicarea operației din enunț. Am plecat *greșit* de la ideea că un număr prim e invalid, dar totuși a dat bine pe 300/450 de cazuri.

Țin într-un set toate numerele pe care le pot forma aplicând repetat operația descrisă în enunț.
Dacă noul număr obținut există deja în set-ul cu numere vizitate sau dacă noul număr este egal cu 1, opresc loop-ul.
Validarea/Invalidarea este dată de condiția ca numărul final să fie egal cu 1.

### Soluție
```
class Solution {
private:
    int digit_sum(int n){
        int x = 0;
        while (n > 0){
            int d = n % 10;
            x += pow(d, 2);
            n /= 10;
        }
        return x;
    }

public:
    bool isHappy(int n) {
        unordered_set<int> set;
        while (n != 1 && !set.count(n)){
            set.insert(n);
            n = digit_sum(n);
        }
        return n == 1;
    }
};
```

## Problema VI - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

### Soluție

- Metoda lentă, dar intuitivă:

Parcurg legăturile head-ului cu head.next, cât timp head nu este null. La fiecare pas, țin minte adresa accesată, iar dacă trec din nou prin ea, înseamnă că am găsit un ciclu și mă opresc. Dacă ajung prin head->next la pointer-ul null, înseamnă că nu am niciun ciclu.

```
class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::set<ListNode*> visited;
        while (head != nullptr){
            if (visited.find(head) != visited.end()){
                return true;
            }
            visited.insert(head);
            head = head->next;
        }
        return false;
    }
};
```

- Metoda rapidă:

Pot folosi doi pointeri pentru a parcurge lista. Unul se va deplasa din două în două adrese (cel rapid), iar cel lent se va deplasa pe fiecare adresă în parte. Atunci când se vor suprapune, cu siguranță există un ciclu. Altfel, dacă cel rapid nu mai are continuitate, înseamnă că în listă nu există niciun loop.

```
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *s(head), *f(head);

        while (f != nullptr && f->next != nullptr){
            s = s->next;
            f = f->next->next;
            if (s == f){
                return true;
            }
        }
        return false;
    }
};
```