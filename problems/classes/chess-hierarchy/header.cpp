
class Cell {
public:
    char v;
    unsigned short int h;

    Cell(): Cell('A',1) {}
    Cell(char v, unsigned short int h): v(v), h(h) {}
};