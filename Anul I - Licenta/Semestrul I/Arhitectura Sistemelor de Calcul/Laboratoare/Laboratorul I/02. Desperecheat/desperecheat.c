// executați în terminal (aveți grijă să fie deschis pe path-ul sursei)
// gcc -m32 desperecheat.c -o desperecheat
// ./desperecheat.c
#include <stdio.h>
int main(int argc, char* argv[], char* arge[]){
    const char* filename = "desperecheat.in";
    FILE *file = fopen(filename, "r");

    if (file == NULL){
        perror("Fisierul nu poate fi deschis in modul de citire");
        return 1;
    }

    // value ^ value = 0 (nu va rezulta dublură)
    // value ^ 0 = value (va rezulta dublură)
    int x, ans = 0;
    while (fscanf(file, "%d", &x) != EOF) {
        ans ^= x;
    }

    printf("%d", ans); return 0;
}