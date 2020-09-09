---
id: 6313accd-19c0-4524-a3df-13f977b0e0f3
longname: FourSum
languages: [cpp]
tags: [vector,twopointers]
checker: cmp_yesno
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Дан массив чисел(vector<int>) и заданное число.	
вернуть вектор из 4х элементов, сумма которых равна заданному.	
nums[i] + nums[j] + nums[k] +nums[z] == target. 	
+ c++: `findArrayQuadruplet(vector<int> &nums, int s)`,	

где `nums` -- исходный массив, `N` -- заданное чисо.	

Вернуть первый подходящий вектор, состояий из таких чисел.
`vector<int> {nums[i], nums[j],nums[k],nums[z]}`. 	

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