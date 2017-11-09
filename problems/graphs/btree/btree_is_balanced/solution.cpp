#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>

struct Node
{
    Node(int data)
    {
        this->left = NULL;
        this->right = NULL;
        this->data = data;
    }

    int height()
    {
        int hl = left ? left->height() : 0;
        int hr = right ? right->height() : 0;

        return 1 + std::max(hl,hr);
    }

    Node *left;
    Node *right;
    int data;
};

bool is_balanced(Node *node, int *h)
{
    if (!node)
    {
        *h = 0;
        return true;
    }

    int lh = 0; 
    int rh = 0;
    bool lb = is_balanced(node->left, &lh);
    bool rb = is_balanced(node->right, &rh);

    *h = 1 + std::max(lh, rh);
    return lb && rb && (abs(lh - rh) <= 1);
}

struct Tree
{
    Tree(std::vector<int> *vect)
    {
        h = 0;
        root = NULL;

        if (vect)
            for(auto iter = vect->begin(); iter != vect->end(); ++iter)
                add(*iter);
    }

    ~Tree()
    {
        free_children(root);
    }

    void free_children(Node *node)
    {
        if (node->left)
            free_children(node->left);

        if (node->right)
            free_children(node->right);

        delete node;
    }

    void add(int data)
    {
        if (!root)
        {
            root = new Node(data);
            return;
        }

        add_at(root, data);
    }

    void add_at(Node *node, int data)
    {
        if (node->data == data)
            return;

        if (data < node->data)
        {
            if (!node->left)
                node->left = new Node(data);
            else
                add_at(node->left, data);
        }
        else 
        {   
            if (!node->right)
                node->right = new Node(data);
            else
                add_at(node->right, data);
        }
    }

    bool IsBalanced()
    {
        return is_balanced(root, &h);
    }

    int h;
    Node *root;
    std::vector<int> vect;
};

int main()
{
    std::vector<int> vect;
    vect.reserve(10000);

    std::string input;
    std::getline(std::cin, input);
    std::stringstream stream(input);
    while(1) 
    {
        int num;
        stream >> num;
        if(!stream)
            break;

        vect.push_back(num);
    }

    Tree obj(&vect);

    std::cout << (obj.IsBalanced() ? "YES" : "NO") << std::endl;

    return 0;
}