---
id: 1f54efd2-07c6-4398-ba9c-d605b41dc586
longname: StackWithMin
languages: [cpp, class]
tags: [medium, io]
checker: cmp_yesno
time_limit: 3
real_time_limit: 3
max_vm_size: 128M
---

Реализовать класс stack, который поддреживат следующие операции:

1. `push` - положить элемент на верхушку
2. `pop` - вытолкнуть верхний элемент 
3. `top` - посмотреть верхний элемент
4. `getMin` - посмотреть минимальный элемент в стеке(стек не изменяется , значение остается там)
5. `print`  - распечатать содержимое стека

Элемент стека - целое число типа `int`

**Важно:**

- если минимальный элемент удалили из стека, getMin возвращает
следующий минимальный элемент.
- где и как будут хранится элементы - ваш выбор.
- гарантируется что не будет операций над пустым стеком.

Ваше решение должно иметь вид:

```
class MinStack {
    //ваш код
    public:
    MinStack() {
        //ваш код
    }
    ~MinStack() {
        //ваш код
    }
    void print() {
        //ваш код
    };
    void push(int x) {
        //ваш код
    };
    void pop() {
        //ваш код
    };
    int top() {
        //ваш код
        return value;
    };
    int getMin() {
        //ваш код
        return value;
    };
}
```

Примеры использования:
`MinStack *mstack = new MinStack;`
`mstack->push(3);`
`mstack->push(2);`
`mstack->top();`
`mstack->getMin()`
`<-- 2 2`
