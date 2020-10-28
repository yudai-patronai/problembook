#include <iostream>
#include <string>
#include <sstream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

struct TreeNode *fill(struct TreeNode *root, std::vector<int> myNumbers, int i, int n) {
    if (i < n) {
        TreeNode *temp = new TreeNode(myNumbers[i]);
        root = temp;
        root->left = fill(root->left, myNumbers, 2 * i + 1, n);
        root->right = fill(root->right, myNumbers, 2 * i + 2, n);
    }
    return root;
}

void go_tree(TreeNode *node, int level, std::vector<std::vector<int>> &res) {
    if (node == NULL)
        return;
    if (level < res.size()) {
        res[level].push_back(node->val);
    } else {
        std::vector<int> line;
        line.push_back(node->val);
        res.push_back(line);
    }
    go_tree(node->left, level + 1, res);
    go_tree(node->right, level + 1, res);
    return;
}

std::vector<std::vector<int>> levelOrder(TreeNode *root) {
    std::vector<std::vector<int>> res;
    int level = 0;
    go_tree(root, level, res);
    return res;
}

int main() {
    std::string line;
    std::getline(std::cin, line);
    std::stringstream iss(line);
    int number;
    std::vector<int> myNumbers;
    while (iss >> number)
        myNumbers.push_back(number);

    struct TreeNode *root;
    root = fill(root, myNumbers, 0, myNumbers.size());

    std::vector<std::vector<int>> level_order = levelOrder(root);
    for (int i = 0; i < (int) level_order.size(); i++) {
        for (int j = 0; j < (int) level_order[i].size(); j++) {
            std::cout << level_order[i][j] << " ";
        }
    }
    return 0;
}
