# Problema [Trepte](https://www.pbinfo.ro/probleme/1798/trepte)
<i>Soluția problemei este, de fapt, o implementare a Șirului lui Fibonacci</i>

## Stare
- d[i] - Numărul total de moduri în care se poate ajunge de pe scara <b>0</b> pe scara <b>i</b>

## Stare inițială
- d[1] = 1 - Un singur mod: <b>0 > 1</b>)
- d[2] = 2 - Două moduri: <i>I) <b>0 > 2</b></i> și <i>II) <b>0 > 1, 1 > 2</b></i>

## Relația de recurență
`d[i] = d[i - 1] + d[i - 2]`
- Pe scara <b>i</b> se poate ajunge de pe scara <b>i - 1</b> sau <b>i - 2</b>

## Soluție
```
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
```
