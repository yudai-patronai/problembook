#include <iostream>
#include <list>
#include <sstream>

struct Node {
    int64_t value;
    Node *next;
};

void push_back(Node *current_node, int64_t value) {
    if (current_node->value == 0) {
        current_node->value = value;
    } else {
        while (current_node->next != nullptr) {
            current_node = current_node->next;
        }
        auto *new_node = new Node();
        new_node->value = value;
        current_node->next = new_node;
    }

}

std::string l2s(Node *node) {
    std::string result;
    while (node != nullptr) {
        result.append(std::to_string(node->value));
        result.append(" ");
        node = node->next;
    }

    return result.substr(0, result.size() - 1);;
}

void getListByLine(std::string &line, Node *list) {
    std::stringstream strStream(line);
    std::string tmp;
    while (std::getline(strStream, tmp, ' ')) {
        push_back(list, std::stol(tmp));
    }
}
