#include <bits/stdc++.h>
short d[2][5][3000];
void add(short a[], short b[])
{
    short t = 0;
    a[0] = a[0] < b[0] ? b[0] : a[0];

    for (int i = 1; i <= a[0]; ++i, t /= 10)
    {
        t = a[i] + b[i] + t;
        a[i] = t % 10;
    }

    if (t) a[++a[0]] = t;
}
int main()
{
    int n;
    FILE* f = fopen("culori3.in", "r");
    fscanf(f, "%d", &n);
    fclose(f);
    for (short i = 0; i < 5; ++i)
    {
        d[0][i][0] = 1;
        d[0][i][1] = 1;
    }

    for (int i = 2; i <= n; ++i)
    {
        memcpy(d[1][0], d[0][1], sizeof(d[0][1])); // + d[0][2]
        memcpy(d[1][1], d[0][0], sizeof(d[0][0]));
        memcpy(d[1][2], d[0][0], sizeof(d[0][0])); // + d[0][3]
        memcpy(d[1][3], d[0][2], sizeof(d[0][2])); // + d[0][4]
        memcpy(d[1][4], d[0][3], sizeof(d[0][3]));
        add(d[1][0], d[0][2]);
        add(d[1][2], d[0][3]);
        add(d[1][3], d[0][4]);
        for (int j = 0; j <= 4; ++j)
            memcpy(d[0][j], d[1][j], sizeof(d[1][j]));
    }
    for (int i = 1; i < 5; ++i)
        add(d[1][0], d[1][i]);

    FILE* g = fopen("culori3.out", "w");
    for (int i = d[1][0][0]; i > 0; --i)
        fprintf(g, "%d", d[1][0][i]);
    fclose(g);
    return 0;
}