#include <iostream>

int main() {
    unsigned N, M;
    int* matrix;
    int **rows;

    std::cin >> N >> M;

    unsigned len = N*N;
    matrix = new int[len];
    rows = new int*[N];
    for (unsigned i = 0; i < N; ++i)
        rows[i] = matrix + i*N;

    for (unsigned i = 0; i < len; ++i) {
        std::cin >> matrix[i];
    }

    unsigned max_row = 0;
    int max_diagonal = rows[max_row][max_row];

    for (unsigned i = 1; i < N; ++i) {
        if (rows[i][i] > max_diagonal) {
            max_row = i;
            max_diagonal = rows[max_row][max_row];
        }
    }

    if (max_row != M) {
        int* tmp = rows[max_row];
        rows[max_row] = rows[M];
        rows[M] = tmp;
    }

    for (unsigned i = 0; i < N; ++i) {
        for (unsigned j = 0; j < N; ++j)
            std::cout << rows[i][j] << " ";
        std::cout << std::endl;
    }

    delete[] rows;
    delete[] matrix;

    return 0;
}

