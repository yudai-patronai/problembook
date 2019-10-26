#include <stdlib.h>
#include <stdio.h>
#include <inttypes.h>

int* read_array(int size) {
    int* arr = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; ++i) {
        scanf("%d", &arr[i]);
    }
    return arr;
}

int64_t dot_product(int* lhs, int* rhs, int size) {
    int64_t result = 0;
    for (int i = 0; i < size; ++i) {
        result += lhs[i] * rhs[i];
    }
    return result;
}

int main() {
    int size;
    scanf("%d", &size);
    int* a = read_array(size);
    int* b = read_array(size);
    int64_t result = dot_product(a, b, size);
    free(a);
    free(b);
    printf("%" PRId64 "\n", result);
    return 0;
}

