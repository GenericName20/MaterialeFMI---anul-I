// Soluția problemei este, de fapt, o implementare a șirului lui Fibonacci
// Starea: d[i] - Numarul total de moduri in care poti sa ajunge de pe scara 0 la scara i
// Stari initiale: d[1] = 1 (Un singur mod: 0 > 1)
//                 d[2] = 2 (Doua moduri: I) 0 > 2 | II) 0 > 1, 1 > 2)
// Relatia de recurenta: d[i] = d[i - 1] + d[i - 2] - Se ajunge de pe scara i de pe scara i - 1 sau i - 2
#include <algorithm>
using namespace std;
int main()
{
    int n; scanf("%d", &n); int* d = (int*)malloc(n * sizeof(int));
    d[1] = 1; d[2] = 2;
    
    for (int i = 3; i <= n; ++i) 
        d[i] = d[i - 1] + d[i - 2];
    
    printf("%d", d[n]);
    return 0;
}