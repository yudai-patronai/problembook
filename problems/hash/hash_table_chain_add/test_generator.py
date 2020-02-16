from lib.testgen import TestSet

# тесты создавались для параметров: модуль 100, основание 91, размер таблицы 10


tests = TestSet()

tests.add(
"""8
YULIA I-course
PAVEL II-course
ANASTASIYA III-course
DMITRIY PhD
MARIYA VI-course
IVAN IV-course
NOBODY academ
MARIYA PhD
""",
"""0
90 ANASTASIYA III-course
1
91 MARIYA PhD
2
42 IVAN IV-course
6
16 PAVEL II-course
6 DMITRIY PhD
8
28 YULIA I-course
9
59 NOBODY academ
"""
)

tests.add(
"""3
PHYSICS thermodynamics
INFORMATICS network_architecture
MATH number_theory
""",
"""1
61 INFORMATICS network_architecture
7
67 PHYSICS thermodynamics
8
48 MATH number_theory
"""
)

# тест на перезапись
tests.add(
"""3
IVAN IVANOV 
LINUS POLLING
IVAN KRUZENSHTERN
"""
,
"""2
42 IVAN KRUZENSHTERN
5
55 LINUS POLLING
"""
)

# тест с коллизиями (от решения требует доп. проверку по ключу)
tests.add(
"""25
ONLY value
RELEASE value
WHEN value
WAS value
INDUSTRY value
ALSO value
TO value
LETRASET value
THE value
LIKE value
TEXT value
BEEN value
A value
PRINTING value
SOFTWARE value
IS value
INCLUDING value
EVER value
PASSAGES value
GALLEY value
MAKE value
BUT value
REMAINING value
OF value
BOOK value
"""
,
"""2
32 ONLY value
62 INDUSTRY value
72 LETRASET value
32 BEEN value
3
3 RELEASE value
3 ALSO value
23 TO value
3 LIKE value
5
45 WAS value
25 THE value
45 TEXT value
65 A value
65 BUT value
6
66 WHEN value
26 IS value
26 EVER value
6 GALLEY value
26 MAKE value
6 REMAINING value
9
69 PRINTING value
79 SOFTWARE value
69 INCLUDING value
69 PASSAGES value
59 OF value
49 BOOK value
"""
)