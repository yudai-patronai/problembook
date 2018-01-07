int main() {
    MyClass class1;
    MyClass class2;
    int numberOfTests;
    std::cin >> numberOfTests;
    for (int i = 0; i < numberOfTests; ++i) {
        int number;
        std::string word;
        std::cin >> number;
        std::cin >> word;
        class1.addElement(number, word);
    }
    std::cin >> numberOfTests;
    for (int i = 0; i < numberOfTests; ++i) {
        int number;
        std::string word;
        std::cin >> number;
        std::cin >> word;
        class2.addElement(number, word);
    }
    class1 += class2;
    class1.printStructures();
    return 0;
}
