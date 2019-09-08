void cycle_shift(int *arr, int N) {
    int beginElement = arr[0];
    for (int count = 0; count < N - 1; count++) {
        arr[count] = arr[count+1];
    }
    arr[N - 1] = beginElement;
}
