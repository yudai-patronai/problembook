int main() {
    MyClass simpleClass;
    int numberOfTests;
    std::cin >> numberOfTests;
    for (int i = 0; i < numberOfTests; ++i) {
        int number;
        std::string word;
        std::cin >> number;
        std::cin >> word;
        simpleClass.AddElement(number, word);
    }
    simpleClass.PrintStructures();
    return 0;
}
