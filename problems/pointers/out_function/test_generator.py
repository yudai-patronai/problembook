from lib.random import choice
from lib.testgen import TestSet

def get_case(values, size):

    q_str = ''
    a_str = ''
    for _ in range(size):
        char = choice(values)
        q_str += char
        if char != ' ':
            a_str += char

    return q_str, a_str

tests = TestSet()

tests.add("Hello vasia,     how are you?", "hellovasia,howareyou?");
tests.add("                             ", "");
tests.add("  va  sia   ", "vasia");

tests.add(*get_case(list("abcdefghijk "), 60))
tests.add(*get_case(list("abcdefghijk       "), 60))
tests.add(*get_case(list("abcdefqu    "), 500))

