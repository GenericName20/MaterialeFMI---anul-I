// 100p - https://kilonova.ro/submissions/504891
#include <fstream>
#include <vector>
#include <algorithm>
#define x first
#define y second
using namespace std;
ifstream f("cabana.in");
ofstream g("cabana.out");
vector<pair<int, int>> p;
int n, x, y;
long long ans;
int main()
{
	// citim N puncte de coordonate (X, Y) și le adăugăm în vectorul de perechi p
	f >> n;
	for (int i = 0; i < n; i++)
	{
		f >> x >> y;
		p.push_back({ x, y });
	}

	// sortăm punctele după coordonata X, apoi după coordonata Y
	sort(p.begin(), p.end());

	for (int i = 0; i < n - 1; i++)
	{
		// nu se mai găsesc alte puncte cu X = p[i].x,
		// se trece la următoarea poziție de pe Ox
		if (p[i].x != p[i + 1].x)
			continue;
		
		// altfel, dacă sunt egale
		// alegem punctele (p[i], p[i + 1])
		// cu ele stabilim colțurile (STÂNGA JOS, STÂNGA SUS) ale dreptunghiului
		// (p[i], p[i + 1]) devin puncte de referință pentru căutările următoare

		// căutăm alte puncte, la dreapta celor alese
		for (int j = i + 2; j < n - 1; ++j)
		{	
			if ((p[j].x == p[j + 1].x)
			// încercăm să alegem punctele (p[j], p[j + 1])
			// cu ele ar trebui să stabilim colțurile (DREAPTA JOS, DREAPTA SUS) ale dreptunghiului
			// dar trebuie respectate și condițiile de jos:
			
			&& (p[i].y == p[j].y && p[i + 1].y == p[j + 1].y))
			// 1) colțul stânga-jos (p[i].x, --> p[i].y <--) 
			//	  trebuie să fie la înălțimea colțului dreapta-jos (p[j].x, --> p[j].y <--)
			
			// 2) colțul stânga-sus (p[i + 1].x, --> p[i + 1].y <--) 
			//	  trebuie să fie la înălțimea colțului dreapta-sus (p[j + 1].x, --> p[j + 1].y <--)
			{
				// dacă se respectă condițiile, calculăm aria și actualizăm maximul
				long long area = 1LL * (p[j].x - p[i].x) * (p[i + 1].y - p[i].y);
				//                   (dr. jos - st. jos) * (st. sus - st. jos)
				ans = max(ans, area);
			}

			// dacă se găsește punct cu (înălțimea >= colț stânga-jos și
			//				       <= colț stânga-sus)
			// înseamnă că nu se poate forma un dreptunghi mai mare
			// ( mai /~lung) decât cel maximal găsit până acum
			else if (p[j].y >= p[i].y &&
						p[j].y <= p[i + 1].y) break;
		}
	}
	g << ans;
	f.close();
	g.close();
	return 0;
}
