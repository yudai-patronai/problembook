id: a76fad54-cee5-40fb-b295-f4e36c5b7439
longname: Сумма 4х
tags: [arrays, functions]
languages: [cpp]
checker: cmp_int_seq
time_limit: 2
real_time_limit: 5
max_vm_size: 64M
---

Дан массив чисел(vector<int>) и заданное число.
вернуть вектор из 4х элементов, сумма которых равна заданному.
nums[i] + nums[j] + nums[k] +nums[z] == target. 
+ c++: `findArrayQuadruplet(vector<int> &nums, int s)`,

где `nums` -- исходный массив, `N` -- заданное чисо.

В результате работы необходимо вернуть вектор состоящий из индексов двух подходящих элементов. 

**Внимание! Вернуть первый подходящий результат**

### Формат входных данных

Функция должна принимать на вход 3 аргумента:
  `размер vector<int> nums`, `vector<int> nums`, `N`.

### Формат выходных данных
`vector<int>`. 

### Примеры

```
-> 8
[2, 7, 4, 0, 9, 5, 1, 3],
20

--
<- [0, 4, 7, 9]
```