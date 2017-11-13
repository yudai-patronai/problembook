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
        class1.AddElement(number, word);
    }
    std::cin >> numberOfTests;
    for (int i = 0; i < numberOfTests; ++i) {
        int number;
        std::string word;
        std::cin >> number;
        std::cin >> word;
        class2.AddElement(number, word);
    }
    class1 += class2;
    class1.PrintStructures();
    return 0;
}
