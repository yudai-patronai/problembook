from lib.testgen import TestSet

tests = TestSet()

tests.add(
    '"Kto tam?" - sprosil dyadya Fyodor.\n',
    'Kto tam?\n'
)
tests.add(
    '"Eto ya!"\n',
    'Eto ya!\n'
)
tests.add(
    'Otgadayte pesnu, v kotoroy est takaya stroka: "Ty ochen tonkaya struna."\n',
    'Ty ochen tonkaya struna.\n'
)
tests.add(
    'aa"cc"bb\n',
    'cc\n'
)
