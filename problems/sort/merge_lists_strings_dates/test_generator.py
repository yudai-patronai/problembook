from lib.testgen import TestSet

def question(L, R):
    return ' '.join(L) + '\n' + ' '.join(R) + '\n'

def answer(A):
    return ' '.join(A) + '\n'

QA = [
    (
        ['1s', '1s1m', '2h'],                           # L
        ['1s1s', '2m', '8000s'],                        # R
        ['1s', '1s1s', '1s1m', '2m', '2h', '8000s']     # A
    ),
    (
        ['2m0s', '200s', '20s10m', '2s30m0h', '20s2h5m'],
        ['15s3m','10m20s', '15m15m2s','7200s1m'],
        ['2m0s', '15s3m', '200s', '20s10m', '10m20s', '2s30m0h', '15m15m2s', '7200s1m', '20s2h5m']
    ),
    (
        ['0s', '1s', '2m0h'],
        ['0s0m0h', '0h0s0m', '0m2s'],
        ['0s', '0s0m0h', '0h0s0m', '1s', '0m2s', '2m0h']
    ),
    (
        ['0s0m0h', '0h0s0m', '0m2s'],
        ['0s', '1s', '2m0h'],
        ['0s0m0h', '0h0s0m', '0s', '1s', '0m2s', '2m0h']
    ),
    (
        ['2m0s', '15s3m', '200s', '20s10m', '10m20s', '2s30m0h', '15m15m2s', '7200s1m', '20s2h5m'],
        ['0s', '0s0m0h', '0h0s0m', '1s', '0m2s', '2m0h'],
        ['0s', '0s0m0h', '0h0s0m', '1s', '0m2s', '2m0s', '2m0h', '15s3m', '200s', '20s10m', '10m20s', '2s30m0h', '15m15m2s', '7200s1m', '20s2h5m']
    )
]

tests = TestSet()

for qa in QA:
    L, R, A = qa
    tests.add(question(L, R), answer(A))
