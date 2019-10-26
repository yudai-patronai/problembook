---
id: bbd5103b-4e19-4b30-a5ca-0253117410b7
longname: Дайсы
languages: [python]
tags: [pattern,adapter]
checker: cmp_int
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Как-то раз, после трудного дня на работе, собрались python-программисты поиграть в "Подземелья и Драконы". Только вот все свои игральные кости они забыли, а без них играть практически невозможно. К счастью, у них с собой были ноутбуки. У Ивана нашелся написанный класс, который по парам чисел генерирует случайные числа, а у Алексея нашлась программа, которая определяет количество различных костей, которые требуется бросить, но не может самостоятельно генерировать случайные числа. Посмотрим на эти программы

class Randomizer:
    
    ...
    
    def generate_by_seq(self, seq):
        from random inport randint
        _sum = 0
        for (n, mx) in seq:
            for i in range(n):
                _sum += randint(1, mx)
        return _sum


class DnDHepler:

    ...

    def add_randomizer(self, randomiser):
        self.randomiser = randomiser

    def get_dice_res(self, dice_seq):
        return self.randomiser.generate_result(dice_seq)

Выяснилось, что интерфейсы этих программ несовместимы. Вам необходимо написать класс `RandomiserAdapter` со следующим прототипом:

class RandomiserAdapter:

    def __init__(self, randomiser : Randomiser):
        raise NotImplementedError("Implementaion is missing")

    def generate_result(self, dice_seq : str) -> int:
        raise NotImplementedError("Implementaion is missing")

Функция generate_result должна по входной строке, в которой указывается, какое количество n-гранных дайсов надо бросить, чтобы получить результат.

### Формат входных данных

dice_seq -- строка вида `"5 d6 + 2d4 +5"` (может содержать пробелы, которые не должны влиять на результат), которая говорит, что надо бросить 5 шестигранников, 2 четырехгранника и добавить 5 к результату. Пробельные символы не несут никакой смысловой нагрузки. Добавочный коэффициент (если он есть) пишется в конце.

generate_by_seq() принимает последовательность вида `[(5, 6), (2, 4)]`, и возвращает сумму 5 случайных чисел а диапазоне [1-6] и 2 случайных чисел в диапазоне [1-4]

### Примеры

```
-> 3d4+5
--
<- 13
```

```
-> 2d6 + 2 d8 + 1
--
<- 17
```
