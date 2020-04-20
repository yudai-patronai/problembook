Node *mergeLists(Node *first_node, Node *second_node) {
    if (first_node == nullptr) {
        return (second_node);
    }
    if (second_node == nullptr) {
        return (first_node);
    }
    auto *result_list = new Node();
    if (first_node->value > second_node->value) {
        result_list->value = second_node->value;
        result_list->next = mergeLists(first_node, second_node->next);
    } else if (first_node->value == second_node->value) {
        result_list->value = second_node->value;
        result_list->next = mergeLists(first_node->next, second_node->next);
    } else {
        result_list->value = first_node->value;
        result_list->next = mergeLists(first_node->next, second_node);
    }
    return result_list;
}