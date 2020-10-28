#include<iostream>
#include<vector>

struct Node {
    int value;
    Node* left;
    Node* right;
};

struct DfsInfo {
    int min;
    int max;
    bool correct;
};

DfsInfo dfs(Node* node) {
    DfsInfo left{node -> value, node -> value, true}, right{node -> value, node -> value, true};
    if (node -> left != nullptr) {
        left = dfs(node -> left);
    }
    if (node -> right != nullptr) {
        right = dfs(node -> right);
    }
    return DfsInfo{left.min, right.max, (right.correct && left.correct && node -> value >= left.max && node -> value <= right.min)};
};

int main() {
    int nodes_num;
    std::cin >> nodes_num;
    std::vector<Node> nodes(nodes_num);
    for (int i = 0; i < nodes_num; ++i) {
        int v, l, r;
        std::cin >> v >> l >> r;
        nodes[i].value = v;
        if (l == -1) {
            nodes[i].left = nullptr;
        } else {
            nodes[i].left = &(nodes[l]);
        }
        if (r == -1) {
            nodes[i].right = nullptr;
        } else {
            nodes[i].right = &(nodes[r]);
        }
    }
    DfsInfo root_info = dfs(&(nodes[0]));
    if (root_info.correct) {
        std::cout << "YES" << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }
    return 0;
}
