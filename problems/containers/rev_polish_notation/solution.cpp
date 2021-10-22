#include <iostream>
#include <string>
#include <cstdlib>

struct Node {
    int v = 0;
    Node *next = nullptr;
};

struct Stack {
    Node *p = nullptr;
};

void push(Stack *s, int x) {
    Node *t = new Node();
    t->v = x;
    t->next = s->p;
    s->p = t;
}

int pop(Stack *s) {
    Node *t = s->p;
    s->p = t->next;
    int x = t->v;
    delete t;
    return x;
}

int main() {
    Stack stack;
    while (true) {
        std::string s;
        std::cin >> s;
        if (s[0] == '=') {
            break;
        }
        if (s[0] == '+') {
            push(&stack, pop(&stack) + pop(&stack));
        } else if (s[0] == '-' && s.length() == 1) {
            auto t = -pop(&stack);
            push(&stack, t + pop(&stack));
        } else if (s[0] == '*') {
            push(&stack, pop(&stack) * pop(&stack));
        } else {
            int x = atoi(s.c_str());
            push(&stack, x);
        }
    }
    std::cout << pop(&stack) << '\n';
    return 0;
}
