#include <vector>
#include <iostream>

struct Node
{
    Node(int data) : left(NULL), right(NULL), data(data) { }

    Node *left;
    Node *right;
    int data;
};

struct Tree
{
    Tree() : root(NULL) { }

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

   	void print(Node *node)
   	{
   		if (!node)
   		{
   			if (!root)
   				return;
   			node = root;
   		}

   		if (node->left)
   			print(node->left);

   		std::cout << node->data << " ";

   		if (node->right)
   			print(node->right);
   	}

    Node *root;
    std::vector<int> vect;
};

