void solution(int *arr, int N) {
    int tmp = arr[0];
    for (int i = 0; i < N - 1; i++) {
        arr[i] = arr[i+1];
    }
    arr[N - 1] = tmp;
}

int main() {
    int n;
    std::cin >> n;
    int *array = new int[n];
    int *test = new int[n];
    for (int i=0; i < n; i++) {
        std::cin >> array[i];
        test[i] = array[i];
    }
    cycle_shift(array, n);
    solution(test, n);
    for (int i=0; i < n; i++) {
        if (array[i] != test[i]) {
            std::cerr << "Your function doesn't change";
            std::cerr << "the input array properly!\n";
            return 1;
        }
    }
    for (int i=0; i < n; i++) {
        std::cout << array[i] << ' ';
    }
    std::cout << std::endl;
    delete[] array;
    delete[] test;
    return 0;
}
