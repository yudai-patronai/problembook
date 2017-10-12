import os
import shutil

MAX_TESTS = 80

class TestSet():
    def __init__(self, tests=None):
        self._test_num = 0

        self._tests_path = os.path.join(os.getcwd(), 'tests')
        shutil.rmtree(self._tests_path, ignore_errors=True)
        os.makedirs(self._tests_path)

        if tests:
            assert hasattr(tests, '__iter__')
            for q, a in tests:
                self.add(q, a)


    def add(self, question, answer):
        assert isinstance(question, str)
        assert isinstance(answer, str)
        assert self._test_num < MAX_TESTS

        with open(os.path.join(self._tests_path, '{0:0>2}'.format(self._test_num)), 'w') as f:
            f.write(question)

        with open(os.path.join(self._tests_path, '{0:0>2}.a'.format(self._test_num)), 'w') as f:
            f.write(answer)

        self._test_num += 1
