---
id: 2c1f1fc4-6f3c-4232-9cdd-62563b85f8f6
longname: Группа строк
languages: [cpp]
tags: [cpp,classes]
checker: cmp_file
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Урсула Арктос занимается исследованиями в области генетики бактериофагов. Урсула нашла определённые закономерности в нуклеотидных последовательностях. Она полагает, что их можно описать особой группой:
- элементами множества яляются цепочки нуклеотидов: ``Adenine``, ``Thymine``, ``Cytosine``, ``Guanine``;
- операцией является соединение цепочек нуклеотидов;
- особенностью цепочек является то, что комплементарные нуклеотиды никогда не встречаются вместе: ``AGGTCAG`` - верная цепочка, ``AGGTCGA`` - неверная цепочка, пара ``CG`` противоречит правилу;
- при соединении двух цепочек комплементарные пары выкидываются: ``AGGTTCA + TGAACCA = AGGTTCATGAACCA = AGGTTCGAACCA = AGGTTAACCA = ... = AA``;
- операция соединения не коммутативна: ``AAC + CTT = AACCTT neq. CC = CTT + AAC``;
- нейтральным элементом является пустая цепочка.

Урсула написала небольшой класс на C++ для работы с нуклеотидами ДНК:
```
#include <cassert>

class DNANucleobase final {
public:
    static DNANucleobase make_adenine() { return DNANucleobase(NucleobaseSymbol::A); }
    static DNANucleobase make_thymine() { return DNANucleobase(NucleobaseSymbol::T); }
    static DNANucleobase make_cytosine() { return DNANucleobase(NucleobaseSymbol::C); }
    static DNANucleobase make_guanine() { return DNANucloebase(NucleobaseSymbol::G); }

    DNANucleobase compliment() const {
        switch(s) {
            case NucleobaseSymbol::A: return make_thymine();
            case NucleobaseSymbol::C: return make_guanine();
            case NucleobaseSymbol::G: return make_cytosine();
            case NucleobaseSymbol::T: return make_adenine();
        }
        assert(false); //unreachable code
    }

    char as_symbol() const {
        switch(s) {
            case NucleobaseSymbol::A: return 'A';
            case NucleobaseSymbol::C: return 'C';
            case NucleobaseSymbol::G: return 'G';
            case NucleobaseSymbol::T: return 'T';
        }
        assert(false); //unreachable code
    }

    bool operator==(DNANucleobase base) const { return s == base.s; }
    bool operator!=(DNANucleobase base) const { return s != base.s; }

private:
    enum class NucleobaseSymbol {A, C, G, T};
    DNANucleobase(NucleobaseSymbol s): s(s) { }
    NucleobaseSymbol const s;
};
```

Класс ``DNANucleobase`` защищает вас от ошибок неверного вывода символов нуклеотидов или неверного вычисления комплиментарного нуклеотида. Урсуле для работы требуется новый класс ``DNA``, который будет моделировать цепочку нуклеотидов ДНК. Создайте класс ``DNA``, удовлетворив следующим требованиям:
- класс должен содержать конструктор без параметров для создания пустой цепочки;
- класс должен содержать конструктор с одним параметром для создания цепочки из одного нуклеотида ``DNA(DNANucleobase base)``;
- класс должен содержать метод ``bool empty() const``, возвращающий ``true`` на пустой цепочке, иначе ``false``;
- класс должен содержать оператор ``+=``, заменяющий цепочку в текущем объекте на сумму текущей цепочки и цепочки, переданной в качестве параметра ``DNA& operator+=(DNA const &rha)`` (аргумент оператора - это правый операнд суммы цепочек);
- класс должен содежать метод ``DNA& invert()``, который превращает цепочку в оратную справа, т.е. для любого ``obj`` верно ``(DNA(obj) += obj.invert()).empty()``;
- класс должен содержать метод ``std::string as_string() const``, возвращающий строку из символов нуклеотидов в соответсвии с цепочкой, заключённую в квадратные скобки (пустой цепочке соответствует ``[]``);
- класс должен содержать операторы ``==`` и ``!=``, возвращающие ``true`` и ``false`` для одинаковых последовательностей нуклеотидов, соответственно;
- предусмотрите защиту внутренних данных класса от случайного изменения;
- внутренние данные должны быть устроены таким образом, чтобы допускать создаваемые компилятором *конструктор копирования* и *оператор копирующего присваивания*;
- добавьте глобальный оператор ``+``, который возвращает **новый** экземпляр класса ``DNA`` и не изменяет входящие данные ``DNA operator+(DNA const &lha, DNA const &rha)``.

***Важно!*** При написании класса ``DNA`` следует использовать заданный класс ``DNANucleobase``, но последний не нужно включать в код решения. Отправляйте на проверку только класс ``DNA``, снабдив код необходимыми заголовками. Названия класса и сигнатуры методов должны быть ровно такими, как указано в описании! Ваш класс и функции будут присоединены к тестирующему коду.

### Формат входных данных

Входные и выходные данные тестирующая программа обрабатывает самостоятельно.

### Формат выходных данных

Входные и выходные данные тестирующая программа обрабатывает самостоятельно.

### Примеры

Примеры кодов, использующих класс DNA:
```
DNA d1, d2(DNANucleobase::make_adenine()), d3(DNANucleobase::make_adenine().compliment());
DNA new_dna = d1 + d2 + d3;
std::cout << new_dna.as_string();
--
[]
```

```
std::vector<DNA> a_lot_of_dna(3,DNANucleobase::make_cytosine());
std::cout << std::accumulate(a_lot_of_dna.begin(),a_lot_of_dna.end(),DNA()).invert().as_string(); 
--
[GGG]
```
