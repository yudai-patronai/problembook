#include <stdlib.h>
#include <stdio.h>

int* read_array(int size) {
    int* arr = (int*)malloc(size * sizeof(int));
    for (size_t i = 0; i < size; ++i) {
        scanf("%d", &arr[i]);
    }
    return arr;
}

void print_array(int* array, int size) {
	for (size_t i = 0; i < size; ++i) {
		printf("%d ", array[i]);
	}
}

int get_average(int a, int b, int c) {
	return (a + b + c) / 3;
}

void make_smoothing(int** arr, int size) {
	int* array = *arr;
	int* smoothing = (int*)malloc(size * sizeof(int));

	smoothing[0] = get_average(array[size-1], array[0], array[1]);
	smoothing[size - 1] = get_average(array[size-2], array[size-1], array[0]);
	for (size_t i = 1; i < size-1; ++i) {
		smoothing[i] = get_average(array[i-1], array[i], array[i+1]);
	}
	free(array);
	*arr = smoothing;
}

int main() {
	int size;
    scanf("%d", &size);
    int* array = read_array(size);
    make_smoothing(&array, size);
    print_array(array, size);
    printf("\n");
    free(array);
    return 0;
}
