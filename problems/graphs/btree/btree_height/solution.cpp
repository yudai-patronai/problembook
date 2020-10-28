#include <cmath>
#include <iostream>
#include <algorithm>
#include <type_traits>

template<class T>
struct Node {
    Node *l, *r;
    T v;
    
    template<class... Args, class = typename std::enable_if<std::is_constructible<T, Args...>::value>::type>
    Node(Args&&... a) : l(nullptr), r(nullptr), v(std::forward<Args>(a)...) {}
    
    Node(const Node& rhs) {
        v = rhs.v;
        if (rhs.l != nullptr) {
            l = new Node(*rhs.l);
        }
        
        if (rhs.r != nullptr) {
            r = new Node(*rhs.l);
        }
    }
    
    Node& operator=(const Node& rhs) {
        if (this != &rhs) {
            v = rhs.v;
            
            Node t{rhs};
            std::swap(l, t.l);
            std::swap(r, t.r);
        }
        
        return *this;
    }
    
    Node(Node&& rhs) {
        v = std::move(rhs.v);
        delete l;
        delete r;
        
        l = rhs.l;
        r = rhs.r;
        
        rhs.l = nullptr;
        rhs.r = nullptr;
    }
    
    Node& operator=(Node&& rhs) {
        v = std::move(rhs.v);
        delete l;
        delete r;
        
        l = rhs.l;
        r = rhs.r;
        
        rhs.l = nullptr;
        rhs.r = nullptr;
        
        return *this;
    }
    
    ~Node() {
        delete l;
        delete r;
    }
};

using TN = Node<int32_t>;

size_t height(const TN* n) {
    size_t res = 1;
    if (n->l) {
        res = height(n->l) + 1;
    }
    
    if (n->r) {
        size_t rh = height(n->r) + 1;
        res = ((res < rh) ? rh : res);
    }
    
    return res;
}

int main() {
    int32_t t;
    
    std::cin >> t;
    TN* root = new TN(t);
    
    while (1) {
        std::cin >> t;
        
        if (!std::cin.good()) {
            break;
        }
        
        TN* cur = root;
        while (1) {
            if (cur->v < t) {
                if (cur->l != nullptr) {
                    cur = cur->l;
                    continue;
                } else {
                    cur->l = new TN(t);
                    break;
                }
            } else {
                if (cur->r != nullptr) {
                    cur = cur->r;
                    continue;
                } else {
                    cur->r = new TN(t);
                    break;
                }
            }
        }
    }
    
    std::cout << height(root) << "\n";
    delete root;
} 
