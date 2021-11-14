
#include <functional>
#include <list>
#include <unordered_map>

template <typename K, typename V, typename H = std::hash<K>>
class AssociativeArray {
public:
    using value_pair = std::pair<K const, V>;
    using value_type = value_pair;
    using reference = value_pair &;
    using const_reference = value_pair const &;
    using pointer = value_pair *;
    using iterator = typename std::list<value_pair>::iterator;
    using const_iterator = typename std::list<value_pair>::const_iterator;

public:
    iterator insert(K const &key, V &&val) {
        auto map_it = map.find(key);
        if (map.end() == map_it)
            return map.emplace(
                          key,
                          order.emplace(order.end(), key, std::move(val)))
                .first->second;
        return map_it->second->second = std::move(val), map_it->second;
    }

    const_iterator find(K const &key) const {
        auto map_it = map.find(key);
        return map.end() == map_it ? order.end() : map_it->second;
    }

    iterator find(K const &key) {
        auto map_it = map.find(key);
        return map.end() == map_it ? order.end() : map_it->second;
    }

    iterator erase(iterator it) {
        map.erase(it->first);
        return order.erase(it);
    }

    iterator erase(std::string const &key) {
        auto map_it = map.find(key);
        if (map.end() == map_it) return order.end();
        return erase(map_it->second);
    }

    iterator begin() { return order.begin(); }
    iterator end() { return order.end(); }
    const_iterator begin() const { return order.begin(); }
    const_iterator end() const { return order.end(); }

private:
    std::list<value_pair> order;
    std::unordered_map<K, iterator, H> map;
};
