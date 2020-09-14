---
id: 0d164571-bc82-4467-86a6-efa582790944
longname: Дроби
languages: [cpp]
tags: [classes]
checker: cmp_int_seq
source_header: header.cpp
source_footer: footer.cpp
time_limit: 1
real_time_limit: 1
max_vm_size: 64M
---


Напишите класс, который будет представлять рациональное число в виде дроби. Реализуйте в нем операторы сложения, вычитания, умножения и унарный минус. Используйте заготовку, приведенную ниже.
**Важно**: думать о входных или выходных данных не нужно, отправьте только реализацию класса.

```
class Fraction {
private:
    // Do NOT rename
    int64_t numerator;
    uint64_t denominator;

    // Do NOT delete
    template<class T>
    friend bool operator==(const Fraction& lhs, const T& rhs);

public:
    Fraction() = delete;
    Fraction(const Fraction& rhs) {}
    Fraction& operator=(const Fraction& rhs);
    Fraction(int64_t numerator, uint64_t denominator);
    //  Add operator overloads below
};

```
