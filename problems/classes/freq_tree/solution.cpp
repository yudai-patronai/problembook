#include <cassert>

struct TreeNode {
    unsigned value;
    unsigned freq;

    TreeNode* left;
    TreeNode* right;
};

class FrequencyTree {
 private:
    TreeNode* root = nullptr;
    void printTreeNodes(TreeNode* node) {
        if (node) {
            printTreeNodes(node->left);
            std::cout << node->value << " " << node->freq << std::endl;
            printTreeNodes(node->right);
        }
    }

    void addValueToNode(TreeNode** node, unsigned value) {
        assert(node);

        if (*node) {
            if ((*node)->value == value) {
                (*node)->freq++;
            } else if ((*node)->value < value) {
                addValueToNode(&((*node)->right), value);
            } else if ((*node)->value > value) {
                addValueToNode(&((*node)->left), value);
            }
        } else {
            TreeNode* new_node = new TreeNode({value, 1, nullptr, nullptr});
            *node = new_node;
        }
    }

    void eraseNodesRecursive(TreeNode* node) {
        if (node) {
            eraseNodesRecursive(node->left);
            eraseNodesRecursive(node->right);
            delete node;
        }
    }

 public:
    FrequencyTree() = default;

    void addValue(unsigned value) {
        addValueToNode(&root, value);
    }

    void printValues(void) {
        printTreeNodes(root);
    }

    ~FrequencyTree() {
        eraseNodesRecursive(root);
    }
};
