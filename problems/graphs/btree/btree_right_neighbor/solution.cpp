#include <queue>
using std::queue;

void build_siblings(Node* root) {
    if (!root)
        return;
    queue<Node*> BFS;
    BFS.push(root);

    while (!BFS.empty()) {
        Node* cur = BFS.front();
        BFS.pop();
        if (!BFS.empty())
            if (BFS.front()->level == cur->level)
                cur->right_sibling = BFS.front();
        if (cur->left)
            BFS.push(cur->left);
        if (cur->right)
            BFS.push(cur->right);
    }
}
