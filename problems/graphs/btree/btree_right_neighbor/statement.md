---
id: 7bb5a3b1-c3f3-43bd-b28a-7d788e9c335d
longname: Построение дерева с правым соседом
languages: [cpp]
tags: [graphs,binary,tree,btree]
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Вам дана экзотическая структура данных. Это бинарное дерево, каждый элемент которого, помимо указателей на левого и правого потомков, также хранит указатель на правого соседа. Если правого соседа нет, то этот указатель равен NULL.

	struct Node {
	    int data; // данные, которые хранятся в узле
	    Node *left, *right, *right_sibling; // указатели на потомков и правого соседа
	    int level; // уровень дерева, на котором находится узел (у корня - 0, у его потомков - 1, и т.д.)
	};

Дерево является сортирующим - значение поля data в узле строго больше, чем у его левого потомка, и строго меньше, чем у правого. Дубли при добавлении игнорируются.

Вам нужно написать функцию, которая проходит по всему дереву и корректно расставляет в нем указатели на правых соседей. 

        void build_siblings(Node* root); 

Сдавать в проверяющую систему нужно только эту функцию (и подключение дополнительных библиотек, их можно и нужно использовать). Функцию main и все прочее отправлять не нужно.

Для отладки можете использовать следующий код.

	#include <iostream>
	using std::cin;
	using std::cout;
	using std::endl;
	
	struct Node {
	    int data;
	    Node *left, *right, *right_sibling;
	    int level;
	};
	
	void insert(Node** root, int data) {
	    if (*root == NULL) {
	        *root = new Node;
	        (*root)->data = data;
	        (*root)->left = NULL;
	        (*root)->right = NULL;
	        (*root)->right_sibling = NULL;
	        (*root)->level = 0;
	        return;
	    }
	    if ((*root)->data > data)
	        insert(&((*root)->left), data);
	    if ((*root)->data < data)
	        insert(&((*root)->right), data);
	}
	
	void mark_levels(Node* root) {
	    if (!root)
	        return;
	    if (root->left) {
	        root->left->level = root->level + 1;
	        mark_levels(root->left);
	    }
	    if (root->right) {
	        root->right->level = root->level + 1;
	        mark_levels(root->right);
	    }
	}
	
	void clear(Node* root) {
	    if (!root)
	        return;
	    clear(root->left);
	    clear(root->right);
	    delete root;
	}
	
	void build_siblings(Node* root);
	
	void print_siblings(Node* root) {
	    if (!root)
	        return;
	    cout << root->data << " ";
	    print_siblings(root->right_sibling);
	}
	
	bool print_level(Node* root, int level) {
	    if (!root)
	        return false;
	    if (root->level == level) {
	        print_siblings(root);
	        cout << endl;
	        return true;
	    }
	    if (print_level(root->left, level))
	        return true;
	    if (print_level(root->right, level))
	        return true;
	    return false;
	}
	
	int main() {
	    int n;
	    cin >> n;
	    Node *root = NULL;
	    for (int i = 0; i < n; i++) {
	        int tmp;
	        cin >> tmp;
	        insert(&root, tmp);
	    }
	    mark_levels(root);
	    build_siblings(root);
	    int level;
	    cin >> level;
	    print_level(root, level);;
	    clear(root);
	    return 0;
	}


### Формат входных данных

У вашей функции, которую вы сдаете в систему, ровно один аргумент - указатель на корень дерева, в котором нужно корректно расставить ссылки на правых соседей.

В коде для отладки на вход подается количество элементов, потом последовательность целых чисел, потом еще одно целое число - уровень дерева, который будет выведен.

### Формат выходных данных

Ваша функция ничего не возвращает и (!) не выводит на экран. Это важно, потому что если вы забудете закомментировать отладочный вывод, то проверяющая система примет это за неправильный ответ.

В коде для отладки выводится соответствующий уровень дерева.

### Примеры

```
-> 8
-> 10 7 15 3 8 13 18 9
-> 2
--
<- 3 8 13 18
```

```
-> 6
-> 30 15 45 20 49 25
-> 2
--
<- 20 49
```
