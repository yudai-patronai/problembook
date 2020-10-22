---
id: d6b61691-9c7e-4a73-a865-c61eb9783f82
longname: Ассоциативный массив с поддержанием порядка вставки
languages: [cpp]
tags: [cpp,containers]
checker: cmp_int_seq
source_footer: footer.cpp
time_limit: 1
real_time_limit: 2
max_vm_size: 64M
---
Евангелина Тигрян работает на станции приёма спутниковых данных. По специальному каналу связи в центр приходят данные из разных источников в строгом порядке. Программа Евангелины хранит приходящие данные во временном хранилище -- векторе пар: ``std::vector<KeyValuePair>``. В некоторые моменты времени к программе приходят запросы на данные от определённых спутников, которые можно узнать по ключу. Достаточно быстро она поняла, что линейный поиск по вектору и удаление приводят к катастрофическому замедлению в работе программы. Евангелина знает, что для ускорения поиска можно использовать хеш-таблицы, но такие таблицы хранят данные в произвольном порядке, а выдавать и удалять данные по запросам нужно строго в том же порядке, в котором они поступали в программу.

Представьте для Евангелины Тигрян класс, моделирующий структру данных, которая будет так же эффективна по поиску и удалению с известным ключом, как хеш-таблица, но одновременно обладает возможностью обходить данные в порядке их добавления.

Ожидаемый класс представляет из себя шаблон с тремя параметрами, один из которых имеет значение по умолчанию. Класс предоставляет конструктор по умолчанию для создания пустого массива. Класс предоставляет методы вставки и удаления. Метод вставки должен возвращать итератор обхода на добавленный элемент, а метод удаления - итератор обхода на элемент следующий за удалённым. Метод поиска должен возвращаеть итератор на существующий элемент, либо ``past-the-end`` итератор. Также итератор должен быть совместим со стандартной библиотекой алгоритмов, но не более чем ``forward_iterator``. Евангелина отметила, что данные очень тяжёлые для копирования и класс должен поддерживать хранение ``noncopyable``: данные не копируются, но гарантируется, что данные будут ``move-constructable`` и ``move-assignable``. Для ключей гарантировано и ``copy-constructable``, и ``copy-assignable``.
Евангелина набросала для Вас заготовку класса:

<pre>
#include <functional>

template <typename K, typename V, typename H = std::hash<K>>
class AssociativeArray {
public:
    /* необходимо для стандартных алгоритмов */
    using value_type = std::pair<K const, V>; 
    using reference = std::pair<K const, V>&;
    using const_reference = std::pair<K const, V> const &;
    using pointer = std::pair<K const, V>*;
    using iterator = /* ??? */; //укажите необходимый тип итератора
    using const_iterator = /* ??? */ //укажите необходимый тип итератора на неизменяемый элемент

    AssociativeArray(); //реализуйте самостоятельно

    iterator insert(/* ??? */); //метод вставки, см. примеры кода
    iterator find(/* ??? */); //метод поиска, см. примеры кода
    const_iterator find(/* ??? */) const; //метод поиска в неизменяемом объекте, см. примеры
    iterator erase(/* ??? */); //метод удаления, см. примеры кода

    //использование см. в примерах кода
    iterator begin();
    iterator end(); 
    const_iterator begin() const;
    const_iterator end() const;
private:
    /* ??? */ //расположите необходимые внутренние данные
};
</pre>

### Формат входных данных

Вам не нужно беспокоиться о входных данных, тестирующая программа обрабатывает их самостоятельно.

### Формат выходных данных

Вам не нужно беспокоиться о выходных данных, тестирующая программа выводит ответ самостоятельно.

### Примеры
Примеры кода, к которому может быть присоединён ваш класс:

<pre>
void list_all(AssociativeArray<KeyType, DataType> const &marked_data) {
    std::for_each(marked_data.begin(), marked_data.end(), [] (DataType const &d) { std::cout << d << ' ';});
}
</pre>

<pre>
void insert_all(AssociativeArray<KeyType,DataType> &marked_data, std::vector<std::pair<KeyType,DataType>> &vec) {
    for (auto &p : vec)
        marked_data.insert(p.first, std::move(p.second));
}
</pre>

<pre>
void list_n_from(AssotiativeArray<KeyType,DataType> const &marked_data, size_t size, KeyType const &first_key) {
    auto it = marked_data.find(first_key);
    for (size_t cnt = 0; cnt != size and marked_data.end() != it; ++cnt, ++it)
       std::cout << it->first << ' ' << it->second << std::endl; 
}
</pre>

<pre>
AssociativeArray<KeyType,DataType>::iterator remove_key(AssotiativeArray<KeyType,DataType> &marked_data, KeyType const &key) {
    return marked_data.erase(key);
}
</pre>

<pre>
AssociativeArray<KeyType,DataType>::iterator remove_n_from(AssociativeArray<KeyType,DataType> &marked_data, size_t size, KeyType const &first_key) {
    auto it = marked_data.find(first_key);
    for (size_t cnt = 0; cnt != size and marked_data.end() != it; ++cnt)
        it = marked_data.erase(it);
    return it;
}
</pre>
