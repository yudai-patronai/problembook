from lib.testgen import TestSet

def question(a):
    return ';'.join(a) + '\n'

def answer(a):
    return question(a)


qa = [
    (
        ['1 m/s', '2 m/s', '1 mm/s', '1 m/h', '1 cm/h', '1 m/min', '1 km/s'],
        ['1 mm/s', '1 m/h', '1 cm/h', '1 m/min', '1 m/s', '2 m/s', '1 km/s']
    ),
    (
        ['20 m/min', '200 mm/s', '300 km/h', '5 m/s', '25 cm/s', '15 m/s', '120 km/h'],
        ['200 mm/s', '25 cm/s', '20 m/min', '300 km/h', '5 m/s', '15 m/s', '120 km/h']
    ),
    (
        ['5 m/s', '20 m/min', '120 km/h', '15 m/s', '200 mm/s', '25 cm/s', '300 km/h'],
        ['20 m/min', '200 mm/s', '25 cm/s', '5 m/s', '120 km/h', '15 m/s', '300 km/h'],
    ),
    (
        ['1 mm/s', '10 mm/min', '100 mm/h', '1 cm/s', '1 cm/min', '1 cm/h', '1 m/s', '1 m/min', '1 m/h', '1 km/s', '1 km/min', '1 km/h'],
        ['10 mm/min', '100 mm/h', '1 cm/min', '1 cm/h', '1 m/h', '1 mm/s', '1 cm/s', '1 m/s', '1 m/min', '1 km/s', '1 km/min', '1 km/h'],
    ),
]

tests = TestSet()

for q, a in qa:
    tests.add(question(q), answer(a))
