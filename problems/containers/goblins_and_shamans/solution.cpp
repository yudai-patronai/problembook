#include <iostream>

struct Node {
    int v = 0;
    Node *prev = nullptr;
    Node *next = nullptr;
};

struct Queue {
    int size = 0;
    Node *head = nullptr;
    Node *tail = nullptr;
};

void push(Queue *q, int x) {
    Node *t = new Node;
    t->v = x;
    if (!q->size) {
        q->size = 1;
        q->head = t;
        q->tail = t;
        return;
    }
    q->size++;
    q->tail->next = t;
    t->prev = q->tail;
    q->tail = t;
}

int pop(Queue *q) {
    Node *t = q->head;
    q->head = t->next;
    q->head->prev = nullptr;
    q->size--;
    if (!q->size) {
        q->tail = nullptr;
    }
    int x = t->v;
    delete t;
    return x;
}

void insert_into_middle(Queue *q, int x) {
    if (q->size < 2) {
        push(q, x);
        return;
    }
    int p = q->size / 2 + q->size % 2;
    Node *t = new Node;
    t->v = x;
    int i = 0;
    Node *cur = q->head;
    while (i < p) {
        i++;
        cur = cur->next;
    }
    q->size++;
    t->next = cur;
    t->prev = cur->prev;
    cur->prev = t;
    t->prev->next = t;
}

void free_queue(Queue *q) {
    while (q->size) {
        pop(q);
    }
}

int main() {
    int n;
    std::cin >> n;
    Queue q;
    for (int i = 0; i < n; i++) {
        char c;
        std::cin >> c;
        if (c == '-') {
            std::cout << pop(&q) << '\n';
        } else if (c == '+') {
            int x;
            std::cin >> x;
            push(&q, x);
        } else {
            int x;
            std::cin >> x;
            insert_into_middle(&q, x);
        }
        std::cin >> c;
    }
    free_queue(&q);
    return 0;
}