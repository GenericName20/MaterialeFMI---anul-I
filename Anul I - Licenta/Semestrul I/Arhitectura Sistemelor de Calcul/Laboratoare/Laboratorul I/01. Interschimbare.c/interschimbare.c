// executați în terminal (aveți grijă să fie deschis pe path-ul sursei)
// gcc -m32 interschimbare.c -o interschimbare
// ./interschimbare.exe
// 2 7
#include <stdio.h>
int main(int argc, char* args[], char* arge[])
{
    int x, y; scanf("%d %d", &x, &y);

    x = x ^ y;
    y = x ^ y;
    x = x ^ y;

    printf("%d %d", x, y); return 0;
}