#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

/**
 * Класс объекта в инвентаре
 */
class Item {
    const std::string name;
    const unsigned weight;
    const unsigned price;
 public:
    Item(const std::string& name, unsigned weight, unsigned price);
    const std::string& get_name() const;
    unsigned get_weight() const;
    unsigned get_price() const;
    void print(std::ostream& os) const;
};

Item::Item(const std::string& name, unsigned weight, unsigned price) :
    name(name),
    weight(weight),
    price(price) {}

const std::string& Item::get_name() const {
    return name;
}

unsigned Item::get_weight() const {
    return weight;
}

unsigned Item::get_price() const {
    return price;
}

void Item::print(std::ostream& os) const {
    os << ":" << name << " " << weight << " " << price << std::endl;
}


/**
 * Класс инвентаря.
 * Можно обойтись и без него, но с ним нагляднее
 */
class Inventory {
    std::vector<Item> items;
    const unsigned size;
    unsigned space() const {
        unsigned free = size;
        for (const auto& item : items)
            free -= item.get_weight();
        return free;
    }
 public:
    explicit Inventory(unsigned size);
    bool put(const Item& item);
    void print(std::ostream& os) const;
};

Inventory::Inventory(unsigned size) : size(size) {}

bool Inventory::put(const Item& item) {
    if (space() >= item.get_weight()) {
        items.emplace_back(item);
        return true;
    }

    return false;
}

void Inventory::print(std::ostream& os) const {
    for (const auto& item : items)
        item.print(os);
}


/**
 * Класс описывает отдельного игрока
 */
class Player {
    const std::string name;
    Inventory inventory;
 public:
    Player(const std::string& name, unsigned strength);
    const std::string& get_name() const;
    bool take(const Item& item);
    void print(std::ostream& os) const;
};

Player::Player(const std::string& name, unsigned strength) :
    name(name),
    inventory(strength) {}

bool Player::take(const Item& item) {
    return inventory.put(item);
}

const std::string& Player::get_name() const {
    return name;
}

void Player::print(std::ostream& os) const {
    os << name << std::endl;
    inventory.print(os);
}


/**
 * Класс, описывающий группу игроков
 */
class Party {
    std::map<std::string, Player> players;
 public:
    bool add(const Player& player);
    bool give(const std::string& player_name, const Item& item);
    void print(std::ostream& os) const;
};

bool Party::add(const Player& player) {
    if (players.find(player.get_name()) == players.end()) {
        players.emplace(player.get_name(), player);
        return true;
    }
    return false;
}

bool Party::give(const std::string& name, const Item& item) {
    auto player = players.find(name);
    if (player != players.end()) {
        return player->second.take(item);
    }
    return false;
}

void Party::print(std::ostream& os) const {
    for (const auto& player : players) {
        player.second.print(os);
    }
}
