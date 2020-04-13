#include <iostream>
#include <algorithm>
#include <vector>

class Person {  
public:
    Person(int64_t id, uint64_t age, uint64_t order) : id_(id), age_(age), order_(order) {}
    
    bool operator<(const Person& rhs) const {
        return ((age_ > rhs.age_) || ((age_ == rhs.age_) && (order_ < rhs.order_)));
    }
    
    bool operator==(const Person& rhs) const {
        return (id_ == rhs.id_);
    }
    
    int64_t getId() const { return id_; }
    
private:
    int64_t id_;
    uint64_t age_, order_;
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    uint64_t N;
    std::cin >> N;
    
    
    std::vector<Person> people;
    people.reserve(N);
    
    
    int64_t id_read;
    uint64_t age_read;
    
    for (uint64_t i = 0; i < N; ++i) {
        std::cin >> id_read >> age_read;
        people.emplace_back(id_read, age_read, i);
    }
    
    
    std::sort(people.begin(), people.end());
    
    for (const auto& person: people) {
        std::cout << person.getId() << "\n";
    }
    people.clear();
}

