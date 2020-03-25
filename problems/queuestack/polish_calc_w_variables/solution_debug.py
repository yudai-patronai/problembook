import solution

def test_varnames():
    tests = [
        (True, 'x'),
        (True, 'X'),
        (True, '_x'),
        (True, 'x12'),
        (True, '_x12'),
        (False, '12x'),
        (False, '*x'),
        (False, '-x'),
        (False, ' x'),
        (False, '+x'),
    ]
    passed = 0
    for true_ans, varname in tests:
        sol_ans = solution.is_valid_varname(varname)
        result = sol_ans == true_ans
        if not result:
            print('varname: {}, get: {}, correct: {}'.format(varname, sol_ans, true_ans))
        else:
            passed += 1

    print('[OK]' if passed == len(tests) else '[!]', 'passed', passed, 'tests from', len(tests))

if __name__ == '__main__':
    test_varnames()
