---
id: 7fe5b98b-7fcc-4209-9f0d-13dc473aa56a
longname: Реализация классов с заданным интерфейсом
languages: [cpp]
tags: [classes]
checker: cmp_file
time_limit: 1
real_time_limit: 1
source_footer: footer.cpp
max_vm_size: 64M
---


Написать классы с заданными интерфейсами, которые реализуют часть логики многопользовательской игры: Предмет интвентаря, Инвентарь, Игрок, Группа игроков.

```cpp
/**
 * Класс предмета в инвентаре
 */
class Item {
 public:
    /**
     * Конструктоp
     * @param name название
     * @param weight вес
     * @param price цена
     */
    Item(const std::string& name, unsigned weight, unsigned price);

    /**
     * Получить название предмета
     * @return название
     */
    const std::string& get_name() const;

    /**
     * Получть вес предмета
     * @return вес
     */
    unsigned get_weight() const;

    /**
     * Узнать цену предмета
     * @return цена
     */
    unsigned get_price() const;

    /**
     * Напечатать информацию о предмете в формате ": название вес цена"
     * @param os поток вывода
     */
    void print(std::ostream& os) const;
};

/**
 * Класс инвентаря.
 */
class Inventory {
 public:
    /**
     * Конструктоp
     * @param size вместимость (максимальный вес всех предметов) равен силе игрока
     */
    explicit Inventory(unsigned size);

    /**
     * Положить предмет в инвентарь, если для него есть место
     * @param item предмет
     * @return true в случае успеха
     */
    bool put(const Item& item);

    /**
     * Распечатать все предметы в порядке получения игроком
     * @param os поток вывода
     */
    void print(std::ostream& os) const;
};

/**
 * Класс, описывает отдельного игрока
 */
class Player {
 public:
    /*
     * Конструктоp
     * @param name имя
     * @param strength сила
     */
    Player(const std::string& name, unsigned strength);

    /**
     * Узнать имя игрока
     * @return имя
     */
    const std::string& get_name() const;

    /**
     * Взять предмет
     * @param item предмет
     * @return true если он поместился в инвентарь
     */
    bool take(const Item& item);

    /**
     * Распечатать на первой строке имя игрока, а на следующих содержимое его инвентаря
     * @param os поток вывода
     */
    void print(std::ostream& os) const;
};

/**
 * Класс, описывающий группу игроков
 */
class Party {
 public:
    /*
     * Добавить игрока в группу, если игрока с таким имененм в ней ещё нет
     * @param player игрок
     * @return true если игрок был успешно добавлен
     */
    bool add(const Player& player);

    /*
     * Дать предмет игроку
     * @param player_name имя игрока
     * @param item предмет
     * @return true если игрок успешно положил его в инвентарь
     */
    bool give(const std::string& player_name, const Item& item);

    /*
     * Распечатаь всех игроков в алфавитном порядке
     * @param os поток вывода
     */
    void print(std::ostream& os) const;
};
```

Нужно дописать классы и реализацию методов.
Остальная игра уже написана и публичный интерфейс менять нельзя.


### Пример использования


```cpp
int main()
{
    Party p;
    p.add(Player("Anti-Mage", 15));
    p.add(Player("Razor", 18));
    p.give("Razor", Item("Necronomicon", 1, 5));
    p.give("Anti-Mage", Item("Refresher_Orb", 2, 2));
    p.print(cout);

    return 0;
}
```

### Результат выполнения

Anti-Mage
:Refresher_Orb 2 2
Razor
:Necronomicon 1 5


