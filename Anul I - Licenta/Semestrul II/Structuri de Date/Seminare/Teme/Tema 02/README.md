# Tema 2 - Stack, queue, deque

## Problema I - Sortarea unei stive

### Enunț

Ai o stivă de numere întregi nesortate. Folosind doar operațiile de bază ale stivei (push, pop, peek, isEmpty) și având la dispoziție o stivă suplimentară ca spațiu auxiliar, sortează stiva astfel încât, la final, elementele să fie în ordine ascendentă (cu cel mai mic element în partea de sus).

### [Soluție bazată pe principii ale Inserion Sort](stacksort.cpp)

Inițial, considerăm o `stivă nesortată (A)`, `o stivă vidă (B)` și o variabilă `x` pentru comparații.

Ulterior, în `x` se reține `vârful stivei A`, iar acesta este îndepărtat. 
- Dacă în `stiva B` există elemente mai mari decât acest `x`, vor fi adăugate în `stiva A`, iar `x` va fi amplasat deasupra acestora.
- În stiva `B` se adaugă `x`.

```
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

```

Algoritmul prezentat are complexitate O(n<sup>2</sup>), unde n este numărul de elemente din stiva inițială. Acest maxim este atins atunci când fiecare element este mutat de mai multe ori din stiva A în B.

### Alte abordări

- Putem considera stiva indexată de la 1, iar valoarea pentru comparații să fie ținută în A[0], dar nu s-ar mai respecta principiul LIFO.
- Dacă avem la dispoziție 3 stive, soluția este aceeași ca cea a problemei 'Turnurile Hanoi'
- Dacă nu putem utiliza o altă variabilă pentru comparații, problema nu are soluție. (Încercările sunt similare cu cele ale problemei prezentate la Seminarul II.)

## Problema II - Sortarea unui deque cu operații limitate

### Enunț (?)

Ai un `deque` ce conține `n` numere întregi într-o ordine arbitrară. Singurele operații permise sunt:

- Scoate elementul din partea din față și inserează-l la coada `deque`-ului.
- Scoate elementul din partea din spate și inserează-l la începutul `deque`-ului.

Determină un număr cât mai eficient de operații necesare pentru a sorta `deque`-ul în ordine ascendentă.

### Abordare

Alegem arbitrar un `deque = {3, 2, 4, 6, 3}`. Nu avem control asupra elementelor din mijloc, ci doar în capete. 

- Aplicăm operația 1 (mutarea capătului din dreapta în stânga) 

Obținem `deque = {3, 3, 2, 4, 6}`. În acest moment, ar trebui să aducem elementul `2` în capătul din stânga:

Fără o structură de date auxiliară, problema ne limitează la o reconstituire prin permutări circulare, deci elementele aflate pe poziții interioare pot fi accesate doar prin aducerea acestora la unul dintre capete. 

- Aplicăm operația 2 de 2 ori:

Obținem `deque = {2, 4, 6, 3, 3}`. Primele 3 elemente sunt sortate, subsecvența `{3, 3}` trebuie introdusă într-o poziție interioară. 

Încercăm să o introducem favorabil pe poziția 2, motiv pentru care ar trebui să 

- Aplicăm operația 2 încă o dată:

Obținem `deque = {4, 6, 3, 3, 2}`, dar nu mai avem acces la secvența `{3, 3}`. Indiferent ce operație am aplica, am obține o permutare circulară, care nu favorizează obținerea unei secvențe contigue crescătoare.

Așa cum am arătat, problema se rezumă la reconstituirea unei permutări circulare, având constrângerea că dacă input-ul nu este constituit dintr-o singură secvență crescătoare și una descrescătoare, problema nu are soluție.

Rezolvarea problemei dacă input-ul este alcătuit dintr-o singură secvență crescătoare și una singură descrescătoare se rezumă la determinarea unei modalități minimale de a ordona această permutare, care poate fi obținută fie doar prin aplicarea repetată a operației 1, fie doar prin aplicarea repetată a operației 2, cât timp deque-ul nu este încă ordonat crescător. Valoarea cerută este minimul dintre numărul de aplicări ale operației 1 și ale operației 2.

Exemplu: `deque = {6, 7, 1, 2, 3}` poate fi ordonată crescător printr-un număr minim de 2 operații de tipul 1. 

Prima aplicare: `deque = {7, 1, 2, 3, 6}`. 

A doua aplicare: `deque = {1, 2, 3, 6, 7}`.

Algoritmul pentru această particularitate are complexitate O(n), iar inserarea în capete se face în O(1).

## Problema III - Reordonarea Alternantă a Listei Înlanțuite

### Enunț

Având o listă înlănțuită simplu, rearanjează nodurile astfel încât ordinea finală să fie: primul nod, ultimul nod, al doilea nod, penultimul nod, al treilea nod, etc.
Exemplu: Pentru lista 1 → 2 → 3 → 4 → 5, soluția ar fi 1 → 5 → 2 → 4 → 3.

### Abordare cu foaie și pix

Considerăm o listă, de exemplu `1 -> 2 -> 3 -> 4 -> 5`.

- Pasul I: Se memorează adresa lui 2 -> 3 -> 4 -> 5.
- Pasul II: Se parcurge această nouă listă. Avem posibilitatea să determinăm ultimul element fără a îl accesa, deci se poate rupe legătura de acesta dintr-un punct inferior. 
- Pasul III: Se pleacă din 1 până la ultimul element din listă și se schimbă orientarea astfel: first->next = last, iar last rămâne legat într-un singur loc.
- Pasul IV: Inserăm acest first->next = last într-o coadă, iar peste first suprapunem adresa lui 2 -> 3 -> 4. (pe 5 l-am rupt)

Și se repetă :)

Ultimul pas: First devine nul. Extragem pointerii din coadă și îi legăm pe cei consecutivi.

### [Soluție](alternating_list.cpp)

```
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
```

Algoritmul are (pe lângă memory leaks) complexitatea O(n<sup>2</sup>), deoarece loop-urile imbricate pot parcurge în worst-case toată lista.

## Problema 4 - Pointer-jumping sum

### Enunț

Fiecare nod al unei liste înlănțuite are, pe lângă pointerul „next”, și un pointer suplimentar numit „jump” care poate indica oricare alt nod (sau poate fi nul). Pornind de la capul listei, urmează în mod repetat pointerul „jump” și calculează suma valorilor nodurilor vizitate. Dacă se detectează o repetiție (nodul a fost vizitat deja), oprește procesul și returnează suma acumulată.

### Soluție

```
struct node {
	bool visited;
	int value;
	node* jump;
	node* next;
};

int main(){

    /* Secvența de inițializare */

    while (current 
        && current->jump 
        && !current->jump->visited) {

        sum += current->value;
        current->visited = true;
        current = current->jump;
    }
}
```

Complexitatea algoritmului este O(n) (worst-case: pointerii de jump sunt noduri consecutive, echivalență cu p.jump = p.next)

## Problema 5 - Maximum Subarray Sum cu ștergerea unui element

### Enunț

Având un vector de numere întregi, determină suma maximă a unei subsecvențe contigue (subarray) în care este permisă ștergerea unui singur element (opțional). Dacă nu este necesară ștergerea, se consideră și soluția fără eliminare.

### Soluție

_Prima intenție a fost să folosesc Algoritmul lui Kadane optimizat. De asemenea, acesta se comportă favorabil pentru cazurile pe care vrem să le tratăm (în special, legate de numerele negative)._

_Ar fi ales doar numerele pozitive pentru a forma un subarray, iar dacă numerele erau negative, se alegea mereu cel mai mic dintre ele. Dacă la final suma formată este negativă, putem să o transformăm în 0 printr-o singură scădere / eliminare._

Dar acea versiune nu ține cont de contiguitatea subsevențelor. Putem folosi o versiune modificată a Algoritmul lui Kadane, cu sliding windows.

Putem ține doi vectori de sume, <code>no_remove</code> și <code>remove</code> și să alegem la fiecare pas cazul cel mai favorabil.

Overall, această implementare are complexitate O(n), fiind suficient să parcurgem vectorul o singură dată, asemănător ca la o problemă de sume parțiale.

## Problema 6 - Cel mai lung subvector binar echilibrat

### Enunț

Având un vector care conține doar valorile 0 și 1, găsește lungimea celui mai lung subvector (secvență continuă) care are un număr egal de 0 și 1.

### Soluție

Putem folosi o implementare sliding windows cu <code>deque</code>, dacă ar fi vorba despre secvențe alternante de 0 și 1. Dar problema se referă la orice structurare a unui subarray contiguu cu valori de 0 și 1 frecvente de un număr egal de ori.

Pentru a face problema mai ușor de înțeles, am ales să îl tratez pe 0 ca -1. Astfel, problema presupune _găsirea celei mai lungi subsecvențe cu suma 0_.

În map-ul <code>sum</code> regăsim perechi \<suma , i>, unde <code>i = primul index de unde s-a format respectiva sumă</code>.

Dacă, pe parcurs, aceeași sumă se poate forma pe un index <code>j</code> ulterior, lungimea unei secvențe care respectă cerința este diferența <code>j - i</code>.
```
#include <iostream>
#include <vector>
#include <random>
#include <unordered_map>

int random_value() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> range(0, 1);
    return range(gen);
}
int main() {
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    std::unordered_map<int, int> sum;

    for (int i = 0; i < n; ++i) {
        A[i] = random_value();
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    int prefix_sum = 0, length = 0;

    for (int i = 0; i < n; i++) {
        prefix_sum += A[i] == 0 ? -1 : 1;

        if (prefix_sum == 0) {
            length = i + 1;
        }
      
        if (sum.find(prefix_sum) != sum.end()) {
            length = std::max(length, i - sum[prefix_sum]);
        }
        else {
            sum[prefix_sum] = i;
        }
    }
    
    std::cout << length;
    return 0;
}
```

Soluția prezentată are complexitate O(n), deoarece sum.find() aplicat pe unordered_map se realizează în O(1).