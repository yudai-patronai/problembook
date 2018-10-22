int main() {
    int n;
    std::cin >> n;
    int *v1 = new int[n];
    for (int i=0; i < n; i++) {
        std::cin >> v1[i];
    }
    int *v2 = new int[n];
    for (int i=0; i < n; i++) {
        std::cin >> v2[i];
    }
    std::cout << dot_product(n, v1, v2) << std::endl;
    delete[] v1;
    delete[] v2;
    return 0;
}
