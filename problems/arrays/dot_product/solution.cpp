int dot_product(int n, int* vector1, int *vector2) {
    int result = 0;
    for (int i=0; i < n; i++) {
        result += vector1[i] * vector2[i];
    }
    return result;
}