# Structuri de Date - Tema de Laborator 3

## Problema I - [Strămoși](https://www.infoarena.ro/problema/stramosi)

### Soluție

Problema pleacă de la premiza că sunt cunoscute tupluri de forma (copil, părinte). Pe baza acestora, se cere răspunsul la întrebarea `'Care este al P-lea copil al nodului Q?'`.

Am rezolvat problema folosind Binary Lifting. Astfel, în tabloul `anc` definim:
- `anc[i][j] = al 2<sup>j</sup>-lea ancestor/strămoș al nodului i`.
- `anc[i][j] = anc[anc[i][j-1]][j-1] (sau 0, dacă anc[i][j-1] nu este definit / nu are strămoș la distanța 2<sup>j-1</sup>)`.

Ulterior, pentru a răspunde la întrebări, verificăm pentru fiecare valoare din intervalul [0, LOG_MAX ~ 18] (cu iterator `j`, de la mare la mic) compatibilitatea cu reprezentarea binară a numărului P.
Dacă bit-ul lui P de pe poziția `2<sup>j</sup>` este activ, se face un salt cel de-al `2<sup>j</sup>`-lea strămoș. Astfel, răspunsurile sunt date în O(logP) ~ O(logN) | p <= n.

Formula recursivă prin care se realizează salturile este:
- `q = anc[q][j], dacă P are bit-ul j activ în reprezentare`

### Sursă - [infoarena.ro](https://www.infoarena.ro/job_detail/3297682?action=view-source) (100p)

```
#include <fstream>
using namespace std;
ifstream f("stramosi.in");
ofstream g("stramosi.out");

#define NLIM 250000
#define LOG 18

int anc[NLIM + 1][LOG + 1], n, m;
int main() {
	f >> n >> m;

	for (int i = 1; i <= n; ++i) {
		f >> anc[i][0];
	}

	for (int j = 1; j <= LOG; ++j) {
		for (int i = 1; i <= n; ++i) {
			int m = anc[i][j - 1];
			anc[i][j] = anc[i][j - 1] ? anc[m][j - 1] : 0;
		}
	}

	while (m--) {
		int p, q;
		f >> q >> p;
		
		for (int j = LOG; j >= 0 && q; --j) {
			if (p & (1 << j)) {
				q = anc[q][j];
			}
		}
		
		g << q << '\n';
	}
	
	f.close();
	g.close();
	return 0;
}
```

## Problema II - [Timbre](https://www.infoarena.ro/problema/timbre)

Problema constă într-o alegere optimă a câte maxim K timbre de paginare pentru toate cele N pagini, alese din subsecvențe ale M intervale.

Plecăm de la premiza că avem informația despre capătul superior al fiecărui interval și costul unei secvențe din acesta.

Fiecare tuplu de forma `[capăt, cost]` este introdus într-un 'heap de maxim' implementat prin `priority_queue`, prioritatea fiind dată de capătul superior, motiv pentru care numerotăm de la mare la mic.

Ulterior, se evaluzează toate intervalele despre care știm că au capătul superior mai mare sau egal cu N-ul curent (ultimele N pagini de numerotat) prin folosirea unui min-heap, implementat prin `priority queue`, prioritatea fiind dată de această dată de cost. Odată cu evaluarea, se elimină tuplul din coada inițială.

Dintre aceste intervale, se alege cel ce are cel mai mic cost. Se alege o secvență de K timbre din acest interval. Costul se adaugă la suma finală și numărul paginilor de numerotat scade cu K.

### Soluție [infoarena.ro](https://www.infoarena.ro/job_detail/3297834) (100p)

```
#include <fstream>
#include <queue>
using namespace std;

ifstream f("timbre.in");
ofstream g("timbre.out");

priority_queue<pair<int, int>> units;
priority_queue<int, vector<int>, greater<>> costs;

int main() {
    int n, m, k;
    f >> n >> m >> k;

    for (int i = 0; i < m; ++i) {
        int upper_bound, price;
        f >> upper_bound >> price;
        units.emplace(upper_bound, price);
    }

    int answer = 0;

    while (n > 0) {
        while (!units.empty() && units.top().first >= n) {
            costs.push(units.top().second);
            units.pop();
        }

        answer += costs.top();
        costs.pop();
        n -= k;
    }

    g << answer;
    return 0;
}
```

## Problema III - [Dacians vs. Samurais](https://codeforces.com/gym/103999/problem/I)

### Soluție - [Codeforces.com](./dacians_vs_samurai.cpp) (100p)

Am folosit tehnica `Sliding Window`. Pentru început, am stocat într-un vector de perechi cele două numere din fiecare intrare, ținând cont de indexul acesteia. Ulterior, le-am sortat crescător după valoare, indexul fiind irelevant în acest moment.

Fereastra se formează de la `left = right = 0`, încercând să o extind cât mai mult în dreapta, respectiv cu dimensiunea vectorului de perechi `= (2n)`.

Pentru a monitoriza câte elemente de pe fiecare poziție sunt incluse în fereastră la o anumită dimensiune, folosesc un `map de frecvență`. De asemenea, urmăresc mereu ca fereastra să aibă maxim `n` elemente, dintre cele `2n`.

Atunci când ating acest maxim, calculez distanța minimă dintre cea calculată până în acest moment și capetele ferestrei. Ulterior, dacă am acoperit toate pozițiile dintre cele `n`, mut capătul din stânga cu o poziție la dreapta.

Răspunsul este dat de cea mai mică distanță găsită.

```
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
vector<pair<int, int>> poll;
unordered_map<int, int> freq;
int main() {
    int n, a, b;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> a >> b;
        poll.emplace_back(a, i);
        poll.emplace_back(b, i);
    }

    sort(poll.begin(), poll.end());

    int total(0), left(0), answer(INT_MAX);

    for (int right = 0; right < poll.size(); ++right) {
        ++freq[poll[right].second];
        if (freq[poll[right].second] == 1) {
            ++total;
        }

        while (total == n) {
            int current_diff = poll[right].first - poll[left].first;
            answer = min(answer, current_diff);

            --freq[poll[left].second];
            if (freq[poll[left].second] == 0) {
                --total;
            }
            ++left;
        }
    }

    cout << answer;
    return 0;
}
```

## Problema IV - [Schi](https://www.infoarena.ro/problema/schi)

Pentru fiecare poziție descoperită, considerăm clasamentul intermediar format doar din primii `i + 1` concurenți. Astfel, concurenții aflați pe aceeași poziție în clasamentul intermediar vor fi amplasați în locații consecutive în vectorul care reprezintă clasamentul final.

### Soluție - [infoarena.ro](https://www.infoarena.ro/job_detail/3297877?action=view-source) (100p)
```
#include <vector>
#include <fstream>
using namespace std;
ifstream f("schi.in");
ofstream g("schi.out");
vector <int> v;
int main()
{
    int n, pos;
    f >> n;
    for (int i = 0; i < n; i++)
    {
        f >> pos;
        v.insert(v.begin() + pos - 1, i + 1);
    }

    for (int i = 0; i < v.size(); ++i) {
        g << v[i] << endl;
    }

    f.close();
    g.close();
    return 0;
}
```

## Problema V - Bleach(https://www.infoarena.ro/problema/bleach)

Pentru a rezolva problema, am folosit un `min-heap`, implementat ca `priority_queue`. În primă fază, am ținut cont de permutarea limitată la `K` poziții, așadar am adăugat primele `k` puteri în heap.

Odată cu avansarea în heap, eliminăm cel mai slab inamic. Dacă diferența dintre puterea acestuia și puterea totală a caracterului este mai mare decât răspunsul calculat până la acest moment, îl actualizăm cu noua diferență. În același timp, puterea totală a caracterului crește cu cea mai slabă descoperită.

În continuare, adaugăm restul valorilor în acest `min-heap`. La fiecare pas vom folosi cele mai mici valori pe care le avem la dispoziție.

### Soluție - [infoarena.ro](https://www.infoarena.ro/job_detail/3298018?action=view-source) (100p)
```
#include <fstream>
#include <queue>
using namespace std;
ifstream f("bleach.in");
ofstream g("bleach.out");
int main() {
	int n, k, temp, lowest;
	long long total(0), answer(0);
	f >> n >> k;

	priority_queue<int, vector<int>, greater<>> pws;

	for (int i = 0; i <= k; ++i) {
		f >> temp;
		pws.push(temp);
	}

	while (!pws.empty()) {
		lowest = pws.top(); pws.pop();

		if (lowest - total > answer) {
			answer = lowest - total;
		}

		total += lowest;

		if (++k < n) {
			f >> temp;
			pws.push(temp);
		}
	}

	g << answer;

	f.close();
	g.close();
	return 0;
}
```