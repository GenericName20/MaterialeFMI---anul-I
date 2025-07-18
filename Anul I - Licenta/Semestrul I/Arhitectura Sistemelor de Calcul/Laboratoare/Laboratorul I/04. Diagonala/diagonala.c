// executați în terminal (aveți grijă să fie deschis pe path-ul sursei)
// gcc -m32 diagonala.c -o diagonala
// chmod x 
// ./diagonala
// 5
#include <stdlib.h>
int main(){
    int n; scanf("%d", &n);
    int** matrix = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i){
        matrix[i] = (int*)malloc(n * sizeof(int));
        // putem să inițializem matricea cu valori pe toate pozițiile, dar nu este specificat
        // for (int j = 0; j < n; ++j) {
        //     matrix[i][j] = 0;
        // }
        matrix[i][i] = i + 1;
    }

    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n; ++j){
            printf("%d ", matrix[i][j]);
        }
        puts("\n");
    }
    free(matrix);
    return 0;
}