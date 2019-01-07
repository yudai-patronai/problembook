#include <stdlib.h>
#include <stdio.h>

int** read_matrix(int size) {
    int** matrix = (int**)malloc(size * sizeof(int*));
    for (int i = 0; i < size; ++i) {
        matrix[i] = (int*)malloc(size * sizeof(int));
        for (int j = 0; j < size; ++j) {
            scanf("%d", &matrix[i][j]);
        }
    }
    return matrix;
}

void free_matrix(int** matrix, int size) {
    for (int i = 0; i < size; ++i) {
        free(matrix[i]);
    }
    free(matrix);
    matrix = NULL;
}

void print_matrix(int** matrix, int size) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void rotate_matrix(int** matrix, int n) {
    int width = (n-1) / 2;
    int height = (n-2) / 2;
    for (int i = 0; i < width + 1; ++i) {
        for (int j = 0; j < height + 1; ++j) {
            // 4 it
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[n-1-j][i];
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
            matrix[j][n-1-i] = tmp;
        }
    }
}

int main() {
	int size;
    scanf("%d", &size);
    int** matrix = read_matrix(size);
    rotate_matrix(matrix, size);
    print_matrix(matrix, size);
    free_matrix(matrix, size);
    return 0;
}

