# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('5\nLanfear 1.3 23.6 1000\nAnnoura 2.5 1.6 20\nAtuan 1.6 0.6397 15\nLeane 1.7 0.684 3\nLiandrin 2.6 0.257 165\n', 'Lanfear Annoura Atuan Leane Liandrin\n')
tests.add('6\nLoial 152.6 2.3 0\nMerise 0.3 0.1 13\nFaeldrin 1.2 0.6 35\nBera 1.3 6.13 16\nSeaine 1.6 0.66 5\nHurin 3.5 4.3 14\n', 'Loial Merise Faeldrin Bera Seaine Hurin\n')  
tests.add('0\n', '\n')
tests.add('1\nEben 2.3 0.6 4294967295\n', 'Eben\n')
