
int main() {
    FrequencyTree ftree;

    unsigned n;
    std::cin >> n;

    unsigned value;
    for (unsigned i = 0; i < n; i++) {
        std::cin >> value;
        ftree.addValue(value);
    }

    ftree.printValues();

    return 0;
}
