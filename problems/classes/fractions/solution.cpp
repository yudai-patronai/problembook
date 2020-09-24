#include <cstdint>

namespace {
    inline int64_t gcd(int64_t a, uint64_t b) {
        if (a < 0) a = -a;
        while (b > 0) {
            a %= b;
            a ^= b;
            b = a ^ b;
            a ^= b;
        }
        return a;
    }
}  //  namespace

class Fraction {
private:
    int64_t numerator;
    uint64_t denominator;

    void Simplify() {
        int64_t cd = gcd(numerator, denominator);
        numerator /= cd;
        denominator /= cd;
    }

    template < class T >
    friend bool operator==(const Fraction& lhs, const T& rhs);

public:
    Fraction() = delete;

    Fraction(const Fraction& rhs)
    : numerator(rhs.numerator), denominator(rhs.denominator) {}

    Fraction& operator=(const Fraction& rhs) {
        numerator = rhs.numerator;
        denominator = rhs.denominator;
        return *this;
    }

    Fraction(int64_t num, uint64_t denom)
    : numerator(num), denominator(denom) {
        Simplify();
    }
    explicit Fraction(int64_t num) : numerator(num), denominator(1) {}

    Fraction& operator+=(const Fraction& rhs) {
        uint64_t cd = gcd(denominator, rhs.denominator);
        numerator = (numerator * (rhs.denominator / cd)) +
                    (rhs.numerator * (denominator / cd));
        denominator *= (rhs.denominator / cd);

        Simplify();

        return *this;
    }

    Fraction operator+(const Fraction& rhs) const {
        Fraction t(*this);
        t += rhs;
        return t;
    }

    Fraction operator-() const {
        return {-numerator, denominator};
    }

    Fraction& operator-=(const Fraction& rhs) {
        (*this) += (-rhs);
        return *this;
    }

    Fraction operator-(const Fraction& rhs) const {
        return (*this) + (-rhs);
    }

    Fraction& operator*=(const Fraction& rhs) {
        auto cd1 = gcd(rhs.numerator, denominator);
        auto cd2 = gcd(numerator, rhs.denominator);

        numerator /= cd2;
        numerator *= (rhs.numerator / cd1);

        denominator /= cd1;
        denominator *= (rhs.denominator / cd2);

        return *this;
    }

    Fraction operator*(const Fraction& rhs) const {
        Fraction t(*this);
        t *= rhs;
        return t;
    }
};
