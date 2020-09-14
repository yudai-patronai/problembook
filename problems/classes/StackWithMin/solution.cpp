struct Node {
    int val;
    Node *next;
    Node(): val(0), next(nullptr){};
    Node(int x) : val(x), next(nullptr){};
};

class MinStack {
    Node *head;
    map <int, int> elements;
    int size;
public:
    /** initialize your data structure here. */
    MinStack() {
        head = NULL;
        size = 0;
    }
    ~MinStack() {
        Node* node = head;
        Node *ptr;
        while(node && node->next) {
            ptr = node->next;
            free(node);
            node = ptr;
        }
    }
    void print() {
        Node* node = head;
        while(node) {
            cout << node->val<< " ";
            node = node->next;
        }
        cout<<endl;
    }
    void push(int x) {
        Node* node = new Node(x);
        node->next = head;
        head = node;
        size++;
        //push element to set
        auto it = elements.find(x);
        if (it != elements.end()) {
            it->second++;
        } else {
            elements.insert({x, 1});
        }
        return;
    }

    void pop() {
        int val = head->val;
        head = head->next;
        auto it = elements.find(val);
        if (it != elements.end()) {
            if (it->second == 1) {
                elements.erase(it);
            }
            else
                it->second--;
        }
    }

    int top() {
        return head->val;
    }

    int getMin() {
        return (elements.begin()->first);
    }
};