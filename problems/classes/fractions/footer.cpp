template <class T>
bool operator==(const Fraction& lhs, const T& rhs);

template <>
bool operator==(const Fraction& lhs, const Fraction& rhs) {
    return (lhs.numerator == rhs.numerator) &&
           (lhs.denominator == rhs.denominator);
}

// Bad practice, but makes code simpler here
template<>
bool operator==(const Fraction& lhs, const int64_t& rhs) {
    return (lhs.denominator == 1) &&
           (lhs.numerator == rhs);
}

struct SuperEqual {};

template<>
bool operator==(const Fraction& /*lhs*/, const SuperEqual& /*rhs*/) {
    return true;
}

/*
 * As for outputing bool's via std::cout
 * It may seem more reliable to check them by hand.
 * However, the behaviour we rely on here is guaranteed:
 * 1. std::noboolalpha unsets the format flag
 * 2. basic_ostream relies on std::num_put
 * 3. num_put converts bool's to int
 * 4. bool converted to int is guaranteed to be 0 or 1 by C++ standard
 */
int main() {
    std::cout << std::noboolalpha;
    {
        Fraction a(1, 2);
        Fraction b(1, 6);

        Fraction c = a + b;
        std::cout << (c == Fraction(1, 3)) << " "
                  << (c == Fraction(2, 3)) << " ";  //  0 1
    }

    {
        //  Just to say hello to non-64bit types users
        //  And to those, who multiply denominators directly
        Fraction a(1, 1000000000039ull);
        Fraction b(1, 3000000000117ull);

        a += b;

        std::cout << (a == Fraction(4, 3000000000117ull)) << " "
                  << (a == Fraction(4, 1000000000039ull)) << " ";  //  1 0
    }

    {
        Fraction a(1, 2);
        Fraction b(1, 6);

        Fraction c = a - b;
        std::cout << (c == Fraction(1, 3)) << " "
                  << (c == Fraction(2, 3)) << " ";  //  1 0
    }

    {
        Fraction a(1, 2);
        Fraction b(1, 6);

        Fraction c = a * b;
        std::cout << (c == Fraction(1, 12)) << " "
                  << (c == Fraction(1, 24)) << " ";  //  1 0
    }

    {
        //  Again 'bout type width & direct multiplication
        Fraction a(1000000000547ull, 1000000000039ull);
        Fraction b(1000000000039ull, 1000000000211ull);

        Fraction c = a * b;
        std::cout << (c == Fraction(1000000000547ull, 1000000000211ull)) << " "
                  << (c == Fraction(1, 1)) << " ";  //  1 0
    }

    {
        Fraction a(3, 9);
        Fraction b(2, 6);
        Fraction c(-4, 12);
        std::cout << (a == b) << " ";  //  1
        std::cout << (-c == b) << " ";  //  1
    }

    {
        //  1
        std::cout << ((Fraction(2, 7) + Fraction(12, 7)) == (int64_t)2) << " ";
    }

    {
        std::cout << (Fraction(1, 7) == SuperEqual()) << " "
                  << (Fraction(2, 7) == SuperEqual()) << std::endl;  //  1 1
    }
}
