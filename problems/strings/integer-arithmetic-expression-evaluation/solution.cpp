#include <iostream>
#include <iterator>

using CharIter = std::istream_iterator<char>;

#include <cctype>

/**
 * Forward declaration of the expression evaluation function
 * is necessary due to recursive call in evaluation of terminal
 * */
bool eval_expression(CharIter &it, CharIter &end, int &expr);

/**
 * Evaluate Number
 * 
 * N ::= D N | D
 * D ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
 * */
int eval_digit_rec(CharIter &it, CharIter &end, int num) {
    if (end == it or !std::isdigit(*it)) return num;
    num *= 10;
    num += static_cast<int>(*it - '0');
    return eval_digit_rec(++it,end,num);
}

bool eval_number(CharIter &it, CharIter &end, int &num) {
    if (end == it or !std::isdigit(*it)) return false;
    return num = eval_digit_rec(it,end,0), true;
}

/**
 * Eval terminal expression
 * 
 * T ::= N | (E)
 * */
bool eval_terminal(CharIter &it, CharIter &end, int &term) {
    if (end == it) return false;
    if ('(' == *it) 
        return eval_expression(++it,end,term) and ')' == *it++;
    return eval_number(it,end,term);
}

/**
 * Eval unary minus
 * 
 * U ::= -T | T
 * */
bool eval_unary(CharIter &it, CharIter &end, int &term) {
    if (end == it) return false;
    bool negate = false;
    if ('-' == *it) {
        negate = true;
        ++it;
    }
    if (!eval_terminal(it,end,term)) return false;
    return (term = negate ? -term : term), true;
}

/**
 * Evaluate product
 * 
 * P ::= UM
 * M ::= *UM | /UM | <empty>
 * */

bool eval_multiplier_rec(CharIter &it, CharIter &end, int &term) {
    int rha;
    if ('*' == *it) {
        if (!eval_unary(++it,end,rha)) return false;
        term *= rha;
        return eval_multiplier_rec(it,end,term);
    }

   if ('/' == *it) {
        if (!eval_unary(++it,end,rha)) return false;
        term /= rha;
        return eval_multiplier_rec(it,end,term);
    }

    return true; 
}

bool eval_product(CharIter &it, CharIter &end, int &term) {
    if (!eval_unary(it,end,term)) return false;
    return eval_multiplier_rec(it,end,term);
} 

/**
 * Evaluate expression
 * 
 * E ::= PS
 * S ::= +PS | -PS | <empty> 
 * */
bool eval_summand_rec(CharIter &it, CharIter &end, int &term) {
    int rha;
    if ('+' == *it) {
        if (!eval_product(++it,end,rha)) return false;
        term += rha;
        return eval_summand_rec(it,end,term);
    }

   if ('-' == *it) {
        if (!eval_product(++it,end,rha)) return false;
        term -= rha;
        return eval_summand_rec(it,end,term);
    }

    return true;
}

bool eval_expression(CharIter &it, CharIter &end, int &term) {
    if (!eval_product(it,end,term)) return false;
    return eval_summand_rec(it,end,term);    
}

int main() {
    CharIter cin_it(std::cin);
    CharIter cin_end;

    int term;
    if (!eval_expression(cin_it,cin_end,term))
        std::cout << "ERROR" << std::endl;
    else {
        if (cin_it != cin_end)
            std::cout << "ERROR" << std::endl;
        else
            std::cout << term << std::endl;
    }
}