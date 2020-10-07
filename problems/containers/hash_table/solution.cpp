#include<iostream>
#include<vector>
#include<list>
#include<random>
#include<utility>

class HashTable {
   public:
    HashTable() :table_(table_size_) {};
    void Insert(int key, int value) {
        int hash = ComputeHash(key, table_size_);
        for (auto kv = table_[hash].begin(); kv != table_[hash].end(); ++kv) {
            if (kv -> first == key) {
                kv -> second = value;
                return;
            }
        }
        table_[hash].push_back(std::pair<int, int>(key, value));
        elements_num_ += 1;
        if (elements_num_ >= table_size_ * threshold_load_factor_) {
            Rehash();
        }
    }

    void Erase(int key) {
        int hash = ComputeHash(key, table_size_);
        for (auto kv = table_[hash].begin(); kv != table_[hash].end(); ++kv) {
            if (kv -> first == key) {
                table_[hash].erase(kv);
                return;
            }
        }
    }

    int Find(int key, int default_value) {
        int hash = ComputeHash(key, table_size_);
        for (auto kv = table_[hash].begin(); kv != table_[hash].end(); ++kv) {
            if (kv -> first == key) {
                return kv -> second;
            }
        }
        return default_value;
    }

   private:
    int elements_num_ = 0, table_size_ = 32;
    std::vector<std::list<std::pair<int, int>>> table_;
    const float threshold_load_factor_ = 0.75;
    // const int64_t big_prime_number_ = 201326611, linear_, modulo_;

    int ComputeHash(int key, int table_size) {
        return key % table_size;
    }

    void Rehash() {
        int new_table_size = 2 * table_size_;
        std::vector<std::list<std::pair<int, int>>> temp_table(new_table_size);
        for (auto row : table_) {
            for (auto kv = row.begin(); kv != row.end(); ++kv) {
                int hash = ComputeHash(kv -> first, new_table_size);
                temp_table[hash].push_back(*kv);
            }
        }
        table_size_ = new_table_size;
        table_ = std::move(temp_table);
    }

    // void SetHashCoefficients() {};
};


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    std::cin >> n >> m;
    std::vector<HashTable> tables(n);
    for (int i = 0; i < m; ++i) {
        int t, k, v;
        char op;
        std::cin >> t >> op >> k >> v;
        if (op == '+') {
            tables[t].Insert(k, v);
        }
        if (op == '-') {
            tables[t].Erase(k);
        }
        if (op == '?') {
            std::cout << tables[t].Find(k, v) << '\n';
        }
    }
    return 0;
}
