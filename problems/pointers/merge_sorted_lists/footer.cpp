
int main() {
    Node *first_list = new Node();
    Node *second_list = new Node();
    Node *result_list;

    std::string first_line;
    std::string second_line;
    std::string result_line;

    std::getline(std::cin, first_line);
    std::getline(std::cin, second_line);
    std::getline(std::cin, result_line);

    getListByLine(first_line, first_list);
    getListByLine(second_line, second_list);

    if (first_list->value == 0) first_list = nullptr;
    if (second_list->value == 0) second_list = nullptr;

    result_list = mergeLists(first_list, second_list);

    if (result_line == l2s(result_list)) {
        std::cout << "YES";
    } else {
        std::cout << "NO";
    }

    return 0;
}