// executați în terminal (aveți grijă să fie deschis pe path-ul sursei)
// gcc -m32 argumente.c -o argumente
// ./argumente.exe "Astazi, 02.10.2024, am fost la laboratorul de ASC"
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[], char *arge[]){

    // fun fact! așa afișăm variabilele de environment
    // for (int i = 0; arge[i] != NULL; ++i){
    //     printf("%s\n", arge[i]);
    // }

    if (argc < 2){
        printf("Numar invalid de argumente!");
        return 1;
    }

    // argumentul este în argv[1]
    // printf("A primit: %s\n", argv[1]);

    // efectuam sscanf pe subsirurile determinate de strtok
    int zi, luna, an;
    char *token = strtok(argv[1], " ");
    while (token != NULL)
    {
        if (sscanf(token, "%d.%d.%d", &zi, &luna, &an) == 3){
            printf("Ziua: %d, Luna: %d, Anul: %d", zi, luna, an);
            return 0;
        }
        token = strtok(NULL, " ");
    }

    printf("Format invalid!");
    return 1;
}