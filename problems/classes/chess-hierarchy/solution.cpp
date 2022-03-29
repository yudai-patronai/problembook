
#include <algorithm>

class Piece {
protected:
    Cell c;
public:
    Piece(): c() {}
    Piece(Cell c): c(c) { }
    virtual ~Piece() {}

    // Вернуть текущую позицию фигуры
    virtual Cell position() const {
        return c;
    }

    virtual bool available(const Cell& q) const = 0;
};


class King : public Piece {
public:
    King(Cell c): Piece(c) { }
    virtual bool available(const Cell& q) const override
    {
        return std::max(abs(q.v - c.v), abs(q.h - c.h)) == 1;
    }
};

class Bishop : public virtual Piece {
public:
    Bishop(Cell c): Piece(c) { }
    virtual bool available(const Cell& q) const override {
        return (std::abs(q.v - c.v) == std::abs(q.h - c.h)) && (std::abs(q.v - c.v) > 0 || std::abs(q.h - c.h) > 0);
    }
};

class Rook : public virtual Piece {
public:
    Rook(Cell c): Piece(c) { }
    virtual bool available(const Cell& q) const override {
        return (q.v == c.v || q.h == c.h) && (!(q.v == c.v && q.h == c.h));
    }
};

class Queen : public Bishop, public Rook {
public:
  Queen(Cell c):  Piece(c), Bishop(c), Rook(c) { }
    virtual bool available(const Cell& q) const {
        return Bishop::available(q) || Rook::available(q);
    }
};
