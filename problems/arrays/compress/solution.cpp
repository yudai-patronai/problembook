int* compress(int** matrix, int n, int m) {
    int* res = new int[n * 3];
    int k = 0;
    for (int i = 0; i < n; i++) {
        int check = 0;
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] != 0) {
                res[k] = matrix[i][j];
                k++;
                check++;
                if (check > 3)
                    break;
            }
        }
        if (check != 3) {
            delete[] res;
            res = NULL;
            break;
        }
    }
    for (int i = 0; i < n; i++)
        delete[] matrix[i];
    delete[] matrix;
    return res;
}
