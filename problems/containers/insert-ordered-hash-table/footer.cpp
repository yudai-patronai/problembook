#include <iostream>
#include <iterator>

namespace test {
/**
 * type + - ?
 * '+' -- добавить или обновить ключ (key -> ключ поиска; data -> новое значение)
 * '-' -- удалить ключ (key -> ключ удаления) или несколько подряд идущих ключей (data -> количество подряд идущих ключей), если они есть
 * */
struct Query final {
    char type;
    std::string key;
    unsigned data;
};

std::istream &operator>>(std::istream &is, Query &q) {
    return is >> q.type >> q.key >> q.data;
}

struct HeavyData final {
    HeavyData(unsigned id) : id(id) {}
    HeavyData(HeavyData &&src) : id(src.id) { src.id = 0; }
    HeavyData& operator=(HeavyData &&src) {
        HeavyData tmp(std::move(src));
        std::swap(id, tmp.id);
        return *this;
    }
    HeavyData(HeavyData const &src) = delete;
    HeavyData& operator=(HeavyData const &src) = delete;

    operator unsigned() const {
        return id;
    }

    unsigned id;
};

using QueryInIt = std::istream_iterator<Query>;
using QueryOutIt = std::ostream_iterator<unsigned>;

template <typename K, typename V, typename H>
void list_all(AssociativeArray<K, V, H> const &data_table, QueryOutIt &q_out) {
    for (auto &d : data_table) 
        *q_out++ = static_cast<unsigned>(d.second);
}

template <typename K, typename V, typename H>
void remove_n_from(AssociativeArray<K, V, H> &data_table, size_t n, K const &from) {
    auto it = data_table.find(from);
    for (size_t count = 0; count != n and it != data_table.end(); ++count)
        it = data_table.erase(it);
}

template <typename T>
void run_test(QueryInIt &q_it, QueryOutIt &q_out, unsigned query_size) {
    AssociativeArray<std::string, T> data_table;
    for (unsigned query_count = 0; query_count != query_size; ++query_count, ++q_it) {
        if ('+' == q_it->type)
            data_table.insert(q_it->key, T{q_it->data});
        if ('-' == q_it->type)
            remove_n_from(data_table, q_it->data, q_it->key);
    }
    list_all(data_table, q_out);
}
}  // namespace test

int main() {
    unsigned query_size;
    std::cin >> query_size;
    std::istream_iterator<test::Query> in_it(std::cin);
    std::ostream_iterator<unsigned> out_it(std::cout, " ");
    test::run_test<test::HeavyData>(in_it, out_it, query_size);

    return 0;
}