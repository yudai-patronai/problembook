# пустые тесты, чтобы problembook не ругался
# простите за костыль, нет времени на редактирование problembook'а

from lib.testgen import TestSet

tests = TestSet()
for _ in range(3):
    tests.add('foo', 'bar')
