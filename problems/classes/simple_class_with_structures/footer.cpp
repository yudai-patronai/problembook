int main() {
    MyClass simpleClass;
    int numberOfTests;
    int number;
    std::string word;
    std::cin >> numberOfTests;
    for (int i = 0; i < numberOfTests; ++i) {
        std::cin >> number;
        std::cin >> word;
        simpleClass.AddElement(number, word);
    }
    simpleClass.PrintStructures();
    return 0;
}
