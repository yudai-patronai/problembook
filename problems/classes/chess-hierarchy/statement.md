---
id: 6cc10081-0882-4201-9c11-47b48c5619c2
longname: Шахматные фигуры
languages: [cpp]
tags: [cpp]
source_header: header.cpp
source_footer: footer.cpp
checker: cmp_int_seq
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---

Требуется написать иерархию классов, представляющих собой некоторые шахматные фигуры.
Напомним, что шахматное поле - это клетчатая доска 8x8 клеток. Вертикали обозначаются буквами латинского алфавита, от A до H. Горизонтали обозначаются цифрами, от 1 до 8. Напоминалки про правила ходов ниже по тексту задачи.
Задан следующий класс, представляющий собой клетку шахматного поля:
<pre>
class Сell final {
public:
    char v; 					                         // Вертикаль, от 'A' до 'H'
    unsigned short int h;		                         // Горизонталь, от '1' до '8'
    Cell(): Cell('A',1) {}			                     // Конструктор клетки по умолчанию
    Cell(char v, unsigned short int h): v(v), h(h) {}	 // Конструктор заданной клетки поля с параметрами
};
</pre>

В программе существует функция, которая позволяет для набора классов, наследующих Piece проверить достижимость определённой клетки:
<pre>
std::vector<bool> are_available(Cell c, std::vector<Piece*> const &pieces) {
    std::vector<bool> answ;
    for (auto p : pieces)
        answ.push_back(p->available(c));
    return answ;
}
</pre>

Ваша задача состоит в том, чтобы правильно объявить класс Piece и его наследников: King, Bishop, Rock и Queen.
Каждая фигура всегда находится в какой-либо клетки. Метод avaliable возвращает true или false в зависимости от того, может ли фигура достичь запрошенную клетку из текущего положения за один ход.
King -- ходит ровно на одну клетку в любом направлении.
Bishop -- ходит на любое количество клеток по диагонали.
Rock -- хоит на любое количиство клеток по горизонтали и вертикали.
Queen -- ходит на любое количество клеток как по диагонали, так и по вертикали, и горизонтали.

Ваш код будет присоединён к тестирующей программе следующего вида:
<pre>
std::vector<bool> are_available(Cell c, std::vector<Piece*> const &pieces);

int main() {
    std::vector<Piece*> pieces;
    pieces.push_back(new King(Cell('A',1)));
    pieces.push_back(new Queen(Cell('B',2)));
    pieces.push_back(new Rock(Cell('C',3)));
    pieces.push_back(new Bishop(Cell('D',4)));

    for(auto b : are_available(Cell('A',1),pieces))
        std::cout << b << ' ';
    std::cout << std::endl;

    for (auto p : pieces)
        delete p;

    return 0;
}
</pre>

***Важно!*** Вам нужно отправить только иерархию классов: Piece, King, Bishop, Rook, Queen.

### Формат входных данных

Вам не нужно заботиться о входных данных.

### Формат выходных данных

Вам не нужно беспокоиться о выходных данных.