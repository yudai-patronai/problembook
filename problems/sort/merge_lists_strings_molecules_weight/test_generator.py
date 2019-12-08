from lib.testgen import TestSet

def question(L, R):
    return ' '.join(L) + '\n' + ' '.join(R) + '\n'

def answer(A):
    return ' '.join(A) + '\n'

QA = [
    (
        ['H2', 'CH4', 'C2H5OH'],                # L
        ['O2', 'NO2'],                          # R
        ['H2', 'CH4', 'O2', 'C2H5OH', 'NO2']    # A
    ),
    (
        ['N2', 'CO2', 'C6H6'],
        ['C6H5CH3', 'C60'],
        ['N2', 'CO2', 'C6H6', 'C6H5CH3', 'C60']
    ),
    (
        ['H', 'N', 'N'],
        ['C', 'C', 'O'],
        ['H', 'C', 'C', 'N', 'N', 'O'] 
    ),
    (
        ['H','H2', 'N', 'N', 'CH4', 'O2', 'C2H5OH', 'NO2'],
        ['C', 'C', 'O', 'N2', 'CO2', 'C6H6', 'C6H5CH3', 'C60'],
        ['H', 'H2', 'C', 'C', 'N', 'N', 'CH4', 'O', 'N2', 'O2', 'CO2', 'C2H5OH', 'NO2', 'C6H6', 'C6H5CH3', 'C60']
    ),
]

tests = TestSet()

for qa in QA:
    L, R, A = qa
    tests.add(question(L, R), answer(A))
